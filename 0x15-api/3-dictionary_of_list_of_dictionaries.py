#!/usr/bin/python3
""" Returns TODO list progress for given employee ID in json format"""

import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    ky = ["username", "completed", "title"]
    filename = "todo_all_employees.json"

    f = open(filename, "w")

    users = (requests.get(url + 'users/')).json()
    todo = (requests.get(url + 'todos/')).json()

    res = {}
    for user in users:
        num = user["id"]
        res[num] = []
        for i in todo:
            if i["userId"] == num:
                buf = {"task": i[ky[2]], ky[1]: i[ky[1]], ky[0]: user[ky[0]]}
                res[num].append(buf)

    f.write(json.dumps(res))
    f.close()
