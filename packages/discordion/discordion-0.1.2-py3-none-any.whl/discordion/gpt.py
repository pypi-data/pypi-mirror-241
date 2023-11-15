import os
import openai
import json
from hashlib import md5
import importlib
import re


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.organization = 'org-ehFJel4pn7hkAYdl3HHe4zxd'
openai.api_key = OPENAI_API_KEY


def best_match(raw, candidates):
    candidate_string = ';'.join(candidates)
    return openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'system',
                'content': 'You are a classifying system, you will receive a an expression or word and pick the best match from a list of possible answers.'
            },
            {
                'role': 'user',
                'content': f'Here are a list of all the candidates separated by ";": {candidate_string}'
            },
            {
                'role': 'assistant',
                'content': f'Awesome, I have identified {len(candidates)} candidates, from now on I will only answer with a possible candidate e.g. "{candidates[0]}"'
            },
            {
                'role': 'user',
                'content': f'What candidate fits best for: {raw}'
            },
        ]
    )['choices'][0]['message']['content']


def best_matches(raw, candidates):
    candidate_string = ';'.join(candidates)
    if len(candidates) < 2:
        return candidates[0]
    return openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'system',
                'content': 'You are a classifying system, you will receive a an expression or word and pick the best matches from a list of possible answers. You can select however many matches you think make sense. keep in mind the input may be contextual as "everything but X" which should return everything but that X.'
            },
            {
                'role': 'user',
                'content': f'Here are a list of all the candidates separated by ";": {candidate_string}'
            },
            {
                'role': 'assistant',
                'content': f'Awesome, I have identified {len(candidates)} candidates, from now on I will only answer with a possible candidates in a comma-separated list (if more matches are identified) e.g. "{candidates[0]}" or "{candidates[0]},{candidates[1]}".'
            },
            {
                'role': 'user',
                'content': f'What candidate fits best for: {candidates[0]}ss'
            },
            {
                'role': 'assistant',
                'content': candidates[0]
            },
            {
                'role': 'user',
                'content': f'What candidate fits best for: {raw}'
            },
        ]
    )['choices'][0]['message']['content'].split(',')


def consume_api(raw, template, unique_name=None):
    unique_name = f't_{md5(template.encode()).hexdigest()}' if unique_name is None else unique_name
    print(f'unique_name: {unique_name}')
    module = importlib.import_module('generated.transformers')
    if hasattr(module, unique_name):
        print('using transformer')
        transformer = getattr(module, unique_name)
    else:
        print('creating transformer')
        with open('generated/transformers.py', 'a', encoding='utf-8') as file:
            resp = generate_api_transformer(raw, template)
            matches = re.search(r'```python(.*?)```', resp, re.DOTALL)

            if matches:
                code = matches.group(1).strip()
            else:
                print('no code found!')

            code = code.replace('def transformer(', f'def {unique_name}(')
            file.write(code + '\n\n\n')

        module = importlib.reload(module)
        if hasattr(module, unique_name):
            transformer = getattr(module, unique_name)
        else:
            print('nope')

    replacement_iter = iter(transformer(raw))

    def replacer(match):
        return str(next(replacement_iter, ''))

    return re.sub(r'{[^}]*}', replacer, template)


def extract_json_into_template(raw, template):
    print(json.dumps(raw, indent=2))
    response = openai.ChatCompletion.create(
        model='gpt-4-1106-preview',
        messages=[
            {
                'role': 'system',
                'content': 'You are a system that takes a json object and populates variables within a template with the relevant data'
            },
            {
                'role': 'user',
                'content': 'Let us start with a simple example: INPUT: {"firstName": "Peter", "age": 14} TEMPLATE: Hi {name}'
            },
            {
                'role': 'assistant',
                'content': 'Hi Peter'
            },
            {
                'role': 'user',
                'content': f'perfect, another one INPUT: {json.dumps(raw)} TEMPLATE: {template}'
            },
        ]
    )['choices'][0]['message']['content']

    return response


def generate_api_transformer(raw, template):
    print(json.dumps(raw))
    response = openai.ChatCompletion.create(
        model='gpt-4-1106-preview',
        messages=[
            {
                'role': 'system',
                'content': 'You are a system that takes a json object and populates variables within a template with the relevant data. You job is write a python transformer function `def transformer(response):` that takes 1 variable `response` (dictionary of same structure as JSON) and returns a list with the values of all of the variables that should be injected in the template in the order they are being injected. You will ONLY respond with the code wrapped in a code block. The code should be as short and concise as possible and without any comments or example usage. Do not use packages that requires pip install'
            },
            {
                'role': 'user',
                'content': 'INPUT: {"first_name": "Svend", "last_name": "Johnson"} TEMPLATE: Hi {full name}'
            },
            {
                'role': 'assistant',
                'content': "```python\ndef transformer(response):\n    return [f\"{response.get('first_name')} {response.get('last_name')}\"]\n```"
            },
            {
                'role': 'user',
                'content': 'INPUT: {"current_units": {"time": "iso8601", "interval": "seconds", "temperature_2m": "\u00b0C", "wind_speed_10m": "km/h"}, "current": {"time": "2023-11-11T19:30", "interval": 900, "temperature_2m": 6.5, "wind_speed_10m": 6.3}} TEMPLATE: Current Temperature: {temperature with units} and and current wind {wind with units}'
            },
            {
                'role': 'assistant',
                'content': "```python\ndef transformer(response):\n    return [\n        f\"{response.get('current', {}).get('temperature_2m', '??'} {response.get('current_units', {}).get('temperature_2m', '??'}\",\n        f\"{response.get('current', {}).get('wind_speed_10m', '??'} {response.get('current_units', {}).get('wind_speed_10m', '??'}\",\n    ]\n```"
            },
            {
                'role': 'user',
                'content': f'INPUT: {json.dumps(raw)} TEMPLATE: {template}'
            },
        ]
    )['choices'][0]['message']['content']

    return response


