#!/usr/bin/python3
""" Will dump all employee todo lists into JSON file"""

from sys import argv
import requests
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    # Will get every task associated with every employee
    r = requests.get(url + "/todos")
    data = r.json()

    # Will just get the employee usernames
    r2 = requests.get(url + "/users")
    users = r2.json()

    # Writes data to file in format
    f = open("todo_all_employees.json", 'w')
    res = {}
    for user in users:
        ID = user['id']
        res[ID] = []
        for i in data:
            if i['userId'] == ID:
                task = {}
                task['task'] = i['title']
                task['completed'] = i['completed']
                task['username'] = user['username']
                res[ID].append(task)
    f.write(json.dumps(res))
