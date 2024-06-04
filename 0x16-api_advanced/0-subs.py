#!/usr/bin/python3
"""
A script that will return no of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """function to return num of subscribers for a subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    requ = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subers = requ.get("data", {}).get("subscribers", 0)
    return subers
