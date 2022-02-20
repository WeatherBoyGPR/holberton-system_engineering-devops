#!/usr/bin/python3
""" Contains number_of_subscribers function """

import requests
import json


def number_of_subscribers(subreddit):
    """ Will return total amount of users subscribed to a subreddit """
    url = 'https://www.reddit.com/r/{}/about.json'
    headers = {'User-Agent': 'HolbertonGPR'}
    res = (requests.get(url.format(subreddit), headers=headers))
    data = (res.json())
    if res.status_code == 404 or data['kind'] != 't5':
        return 0
    return(data['data']['subscribers'])
