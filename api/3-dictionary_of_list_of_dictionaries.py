#!/usr/bin/python3
"""
Module 3-dictionary_of_list_of_dictionaries
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    res = requests.get(
        "https://jsonplaceholder.typicode.com/todos/"
    )
    tsks = json.loads(res.text)
    usrs = requests.get("https://jsonplaceholder.typicode.com/users")
    us = json.loads(usrs.text)
    res_us = {}
    res_us.setdefault("users", [])
    nid = 1
    json_dict = {}
    usns = []
    count = 0

    for line in us:
        res_us["users"].append(line)

    #print(res_us)
    name_us = res_us["users"]
    while True:
        usns.append(name_us[count]["username"])
        count += 1
        if count == 10:
            break

    my_tsks = [
        (i["completed"], i["title"], i["userId"]) for i in tsks
        if "completed" or "title" or "userId" in i
    ]

    for i, j, k in my_tsks:
        json_dict.setdefault(k, [])
        if i is True:
            json_dict[k].append(dict(task=j,
                                       completed=True, username=usns[k - 1]))
        else:
            json_dict[nid].append(dict(task=j,
                                       completed=False, username=usns[k - 1]))

    ob_json = json.dumps(json_dict)
    with open("todo_all_employees.json", "w") as fp:
        fp.write(ob_json)
