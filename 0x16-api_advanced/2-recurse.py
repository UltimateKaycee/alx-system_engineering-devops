#!/usr/bin/python3
"""Script to query API for title of hot articles"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Function to return list of titles of hot posts on a subreddit."""
    url = "https://www.reddit.com/dev/api/r/{}/hot/.json".format(subreddit)
    
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
