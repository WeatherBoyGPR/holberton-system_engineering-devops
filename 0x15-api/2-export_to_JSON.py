#!/usr/bin/python3
""" Will dump employee todo list from given ID into JSON file"""

from sys import argv
import requests
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    ID = argv[1]
    params = {'userId': ID}
    params2 = {'id': ID}

    # Will get every task associated with the employee id
    r = requests.get(url + "/todos", params=params)
    data = r.json()

    # Will just get the employee username
    r2 = requests.get(url + "/users", params=params2)
    username = r2.json()[0].get('username')

    # Writes data to file in format
    f = open("{}.json".format(ID), 'w')
    res = {ID: []}
    for i in data:
        task = {}
        task['task'] = i['title']
        task['completed'] = i['completed']
        task['username'] = username
        res[ID].append(task)
    f.write(json.dumps(res))
