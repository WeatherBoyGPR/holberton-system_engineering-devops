#!/usr/bin/python3
""" Returns TODO list progress for given employee ID """

import requests
import sys
import json

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    stmt = 'Employee {} is done with tasks({}/{}):'

    users = (requests.get(url + 'users/' + sys.argv[1])).json()
    todo = (requests.get(url + 'todos/?userId=' + sys.argv[1])).json()

    tot = 0

    for i in todo:
        if i['completed']:
            tot += 1
    print(stmt.format(users['name'], tot, len(todo)))
    for i in todo:
        if i['completed']:
            print('\t {}'.format(i['title']))
