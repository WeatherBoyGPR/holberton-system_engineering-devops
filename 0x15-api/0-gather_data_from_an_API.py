#!/usr/bin/python3
""" Will return employee todo list progress from given ID """

from sys import argv
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    ID = argv[1]
    params = {'userId': ID}
    params2 = {'id': ID}
    form = "Employee {} is done with tasks({}/{}):"

    # Will get every task associated with the employee id
    r = requests.get(url + "/todos", params=params)
    data = r.json()

    # Will just get the employee name
    r2 = requests.get(url + "/users", params=params2)
    name = r2.json()[0].get('name')

    # Processes employee tasks
    doneTasks = []
    total = 0
    doneN = 0
    for i in data:
        if i['completed']:
            doneTasks.append(i['title'])
            doneN += 1
        total += 1

    # Output
    print(form.format(name, doneN, total))
    for i in doneTasks:
        print("\t {}".format(i))
