#!/usr/bin/python3
"""
Module 1-export_to_CSV
"""
import csv
import requests
import json
from sys import argv


if __name__ == "__main__":

    res = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId={}".format(argv[1])
    )
    tsks = json.loads(res.text)
    usrs = requests.get("https://jsonplaceholder.typicode.com/users")
    us = json.loads(usrs.text)
    res_us = {}
    counter = 0
    csv_list = []
    nid = int(argv[1])

    for line in us:
        counter += 1
        res_us.update(line)
        if counter == nid:
            break
    name_us = res_us["username"]

    my_tsks = [
        (i["completed"], i["title"]) for i in tsks
        if "completed" or "title" in i
    ]

    for i, j in my_tsks:
        if i is True:
            csv_list.append("{}".format(str(nid)))
            csv_list.append("{}".format(name_us))
            csv_list.append("True")
            csv_list.append("{}".format(j))
        else:
            csv_list.append("{}".format(str(nid)))
            csv_list.append("{}".format(name_us))
            csv_list.append("False")
            csv_list.append("{}".format(j))

    print(name_us)
    print(csv_list)

    with open('{}'.format(nid), 'w') as fp:
        writer = csv.writer(fp)
        writer.writerow(csv_list)
