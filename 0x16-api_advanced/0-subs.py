#!/usr/bin/python3
""" Contains number_of_subscribers function """
import requests


def number_of_subscribers(subreddit):
    """ Will return number of subscribers for a given subreddit """
    url = 'https://www.reddit.com/r/{}/about.json'
    headers = {'User-Agent': 'holberton-0x16-2022'}

    r = requests.get(url.format(subreddit), headers=headers)
    data = r.json()
    if r.status_code != 200 or data['kind'] != 't5':
        return 0
    return (data['data']['subscribers'])
