#!/usr/bin/python3
""" Returns TODO list progress for given employee ID in json format"""

import json
import requests
import sys

if __name__ == "__main__":
    num = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    key = ["username", "completed", "title"]
    filename = num + ".json"

    f = open(filename, "w")

    users = (requests.get(url + 'users/' + num)).json()
    todo = (requests.get(url + 'todos/?userId=' + num)).json()

    res = {num: []}
    for i in todo:
        buf = {"task": i[key[2]], key[1]: i[key[1]], key[0]: users[key[0]]}
        res[num].append(buf)

    f.write(json.dumps(res))
    f.close()
