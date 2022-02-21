#!/usr/bin/python3
""" Contains top_ten function """

import json
import requests


def top_ten(subreddit):
    """ Will print the titles of the first 10 hot posts for a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?sort=popular'
    headers = {'User-Agent': 'HolbertonGPR'}
    res = (requests.get(url.format(subreddit), headers=headers))
    data = (res.json())
    if res.status_code == 404 or data['data']['dist'] == 0:
        print(None)
        return
    for i in range(0, 10):
        print(data['data']['children'][i]['data']['title'])
