#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API
"""
import requests
import json
from sys import argv


res = requests.get("https://jsonplaceholder.typicode.com/todos")
data = json.loads(res.text)

print(data)