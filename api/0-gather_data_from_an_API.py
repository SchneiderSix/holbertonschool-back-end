#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID,
returns information about his/
her TODO list progress.
"""
import requests
import json
from sys import argv


if __name__ == '__main__':

        res = requests.get("https://jsonplaceholder.typicode.com/todos/?userId={}".format(argv[1]))
        tsks = json.loads(res.text)
        usrs = requests.get("https://jsonplaceholder.typicode.com/users")
        us = json.loads(usrs.text)

        res_us  = {}
        counter = 0
        counter_tsks = 0
        nid = int(argv[1])

        for line in us:
                counter += 1
                res_us.update(line)
                if counter  == nid:
                        break

        name_us = res_us['name']

        my_tsks = [(i['completed'], i['title']) for i in tsks if "completed" or "title" in i]

        for i, j in my_tsks:
                if i == True:
                        print(j)
                        counter_tsks += 1

        print("Employee {} is done with tasks({}/20):".format(name_us, counter_tsks))

        for i, j in my_tsks:
                if i == True:
                        print("\t {}".format(j))
