#!/usr/bin/python3
""" Contains top_ten function """

import requests


def top_ten(subreddit):
    """ Will print the top ten hottest posts of any given subreddit """
    url = 'https://reddit.com/r/{}/hot.json'
    params = {'sort': 'popular'}
    headers = {'User-Agent': 'holberton-0x16-2022'}

    r = requests.get(url.format(subreddit), params=params, headers=headers)
    if r.status_code != 200:
        print('None')
        return
    data = r.json()
    if data['data']['dist'] == 0:
        print('None')
        return
    for i in range(0, 10):
        print(data['data']['children'][i]['data']['title'])
