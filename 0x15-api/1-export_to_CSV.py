#!/usr/bin/python3
""" Returns TODO list progress for given employee ID in CSV format"""

import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    line = '\"{}\",\"{}\",\"{}\",\"{}\"\n'
    key = ["userId", "username", "completed", "title"]
    filename = sys.argv[1] + ".csv"

    f = open(filename, "w")

    users = (requests.get(url + 'users/' + sys.argv[1])).json()
    todo = (requests.get(url + 'todos/?userId=' + sys.argv[1])).json()

    buf = ""

    for i in todo:
        buf += (line.format(i[key[0]], users[key[1]], i[key[2]], i[key[3]]))
    f.write(buf)
    f.close()
