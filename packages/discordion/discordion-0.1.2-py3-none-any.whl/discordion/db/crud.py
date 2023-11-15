import sqlitedict
import json
import uuid


class ModelRegistry:
    registry = {}

    @classmethod
    def register(cls, model):
        cls.registry[model.__name__] = model

    @classmethod
    def get(cls, name):
        return cls.registry.get(name, None)


class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        if name != 'Model':  # Skip the base Model class
            new_class._defaults = {k: v for k, v in attrs.items() if not k.startswith('_')}

            def _model(cls):
                return ModelContextManager(name.lower())
            setattr(new_class, '_model', classmethod(_model))
        return new_class


class Model(metaclass=ModelMeta):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        ModelRegistry.register(cls)

    def __init__(self, id=None, **kwargs):
        self.related_ids = {}
        self.__dict__.update({'id': id if id else str(uuid.uuid4())} | kwargs)

    @classmethod
    def create(cls, **kwargs):
        defaults = getattr(cls, '_defaults', {}).copy()
        defaults.update(kwargs)  # Override defaults with provided kwargs
        with cls._model() as model:
            id = model.create(**defaults)
        return cls(id=id, **defaults)

    @classmethod
    def find(cls, id):
        with cls._model() as model:
            record = model.read(id)
        if record:
            return cls(**record)
        return None

    def update(self, **kwargs):
        with self._model() as model:
            model.update(self.id, **kwargs)
        self.__dict__.update(kwargs)

    def delete(self):
        with self._model() as model:
            model.delete(self.id)

    def attach(self, other_model_instance):
        if other_model_instance.__class__.__name__ not in self.related_ids:
            self.related_ids[other_model_instance.__class__.__name__] = []
        self.related_ids[other_model_instance.__class__.__name__].append(other_model_instance.id)
        self.update(related_ids=self.related_ids)

        if self.__class__.__name__ not in other_model_instance.related_ids:
            other_model_instance.related_ids[self.__class__.__name__] = []
        other_model_instance.related_ids[self.__class__.__name__].append(self.id)
        other_model_instance.update(related_ids=other_model_instance.related_ids)

    def detach(self, other_model_instance):
        model_name = other_model_instance.__class__.__name__
        if model_name in self.related_ids and other_model_instance.id in self.related_ids[model_name]:
            self.related_ids[model_name].remove(other_model_instance.id)
            self.update(related_ids=self.related_ids)

        model_name = self.__class__.__name__
        if model_name in other_model_instance.related_ids and self.id in other_model_instance.related_ids[model_name]:
            other_model_instance.related_ids[model_name].remove(self.id)
            other_model_instance.update(related_ids=other_model_instance.related_ids)

    def link(self, other_model_instance):
        self.related_ids[other_model_instance.__class__.__name__] = [other_model_instance.id]
        self.update(related_ids=self.related_ids)

        other_model_instance.related_ids[self.__class__.__name__] = [self.id]
        other_model_instance.update(related_ids=other_model_instance.related_ids)

    def get(self):
        record = self.__dict__.copy()
        for model_name, ids in self.related_ids.items():
            plural_model_name = model_name.lower() + 's'  # Pluralize
            model_class = ModelRegistry.get(model_name)
            record[plural_model_name] = [model_class.find(id) for id in ids]
        return record

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getattr__(self, name):
        attributes = self.get()
        print('attr', attributes)
        if name in attributes:
            return attributes[name]
        raise AttributeError(f"{self.__class__.__name__} object has no attribute '{name}'")

    def __contains__(self, key):
        return key in self.get()

    def __str__(self):
        attributes = [f"{key}={value}" for key, value in self.__dict__.items() if not key.startswith("_") and key != 'id']
        return f"{self.__class__.__name__}({', '.join(attributes)})"

    @classmethod
    def flush(cls):
        with cls._model() as model:
            model.flush()

    @classmethod
    def all(cls):
        with cls._model() as model:
            return [cls(**json.loads(record)) for record_id, record in model.all()]

    @classmethod
    def where(cls, **kwargs):
        with cls._model() as model:
            return [cls(**json.loads(record)) for record_id, record in model.where(**kwargs)]

    # Implement related logic here based on your specific needs
    @classmethod
    def _model(cls):
        pass


class ModelContextManager:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db_path = f"{self.table_name}.db"
        self.db = None

    def __enter__(self):
        self.db = sqlitedict.SqliteDict(self.db_path)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.db:
            self.db.close()

    def create(self, **kwargs):
        kwargs = {'id': str(uuid.uuid4())} | kwargs
        id = kwargs.get('id')
        print('creating with id', id, kwargs.get("id"))
        kwargs["related_ids"] = kwargs.get("related_ids", {})
        self.db[id] = json.dumps(kwargs)
        self.db.commit()
        return id

    def read(self, id):
        for key, item in self.db.items():
            print(f'{key}: {item}')
        data = self.db.get(str(id), None)
        if data:
            return json.loads(data)
        return None

    def update(self, id, **kwargs):
        existing = self.read(id)
        if existing:
            existing.update(kwargs)
            self.db[str(id)] = json.dumps(existing)
            self.db.commit()

    def delete(self, id):
        if str(id) in self.db:
            del self.db[str(id)]
            self.db.commit()

    def flush(self):
        self.db.clear()
        self.db.commit()

    def all(self):
        # Check that the database is connected
        if self.db is None:
            raise Exception("Database must be connected before performing operations")

        # Retrieve all records
        for key, value in self.db.items():
            yield key, value

    def where(self, **kwargs):
        if self.db is None:
            raise Exception("Database must be connected before performing operations")

            # Retrieve records that match the given kwargs
        for key, value in self.db.items():
            record = json.loads(value)
            if all(record.get(k) == v for k, v in kwargs.items()):
                yield key, value


# Example usage
if __name__ == '__main__':

    class UserTest(Model):
        lastName = 'doe'


    class OrderTest(Model):
        pass

    UserTest.flush()
    OrderTest.flush()
    # Create users
    user1 = UserTest.create(username="John", age=30)
    user2 = UserTest.create(username="Jane", age=25)

    print(user1, user2)

    # Create orders
    order1 = OrderTest.create(product="Laptop", price=1000)
    order2 = OrderTest.create(product="Phone", price=800)

    # Update user1
    user1_found = UserTest.find(user1.id)
    if user1_found:
        user1_found.update(username="Jonathan", age=31)

    # Delete user2
    user2_found = UserTest.find(user2.id)
    if user2_found:
        user2_found.delete()

    # Attach order1 to user1
    order1_found = OrderTest.find(order1.id)
    print(OrderTest.all())
    print([(x.get()) for x in OrderTest.all()])
    print(order1_found.get())
    print(user1_found.get())
    if order1_found:
        order1_found.attach(user1_found)
        print(order1_found.get())

        print(user1_found.username)
        print(user1_found.notFound if 'notFound' in user1_found else 'nope!')
        user1_found.notFound = 'now found!'
        print(user1_found.notFound if 'notFound' in user1_found else 'nope!')
        print(user1_found['username'])
        print([x.get() for x in user1_found.ordertests])
        print([x.get() for x in order1_found.usertests])

    print("lists")
    print([x.get() for x in OrderTest.all()])
    print([x.get() for x in OrderTest.where(product='Phone')])
