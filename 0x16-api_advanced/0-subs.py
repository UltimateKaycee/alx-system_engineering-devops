#!/usr/bin/python3
"""
A script that will return no of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """function to return num of subscribers for a subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    requ = requests.get('https://www.reddit.com/dev/api/r/{}/about.json'.format(subreddit),
                    
    subers = requ.get("data", {}).get("subscribers", 0)
    return subers
