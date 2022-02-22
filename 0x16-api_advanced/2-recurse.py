#!/usr/bin/python3
""" Contains Recurse Function """

import json
import requests


def recurse(subreddit, hot_list=[], lim=100, aft=None, cnt=0):
    """ Will return list of all titles of all hot articles for a subreddit """
    url = "https://www.reddit.com/r/{}/hot.json"
    headers = {'User-Agent': 'HolbertonGPR'}
    params = {
        'limit': lim,
        'after': aft,
        'count': cnt
    }

    subred = requests.get(url.format(subreddit), headers=headers,
                          params=params, allow_redirects=False)
    if subred.status_code == 404:
        return None
    data = subred.json().get('data')
    params['after'] = data.get('after')
    params['count'] += data.get('dist')
    for i in data['children']:
        hot_list.append(i['data']['title'])
    if params['after'] is not None:
        return recurse(subreddit, hot_list, params['limit'],
                       aft=params['after'], cnt=params['count'])
    return hot_list
