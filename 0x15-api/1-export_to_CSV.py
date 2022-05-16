#!/usr/bin/python3
""" Will dump employee todo list from given ID into CSV file"""

from sys import argv
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    ID = argv[1]
    params = {'userId': ID}
    params2 = {'id': ID}
    form = "\"{}\",\"{}\",\"{}\",\"{}\"\n"

    # Will get every task associated with the employee id
    r = requests.get(url + "/todos", params=params)
    data = r.json()

    # Will just get the employee username
    r2 = requests.get(url + "/users", params=params2)
    name = r2.json()[0].get('username')

    # Writes data to file in format
    f = open("{}.csv".format(ID), 'w')
    for i in data:
        f.write(form.format(ID, name, i['completed'], i['title']))
