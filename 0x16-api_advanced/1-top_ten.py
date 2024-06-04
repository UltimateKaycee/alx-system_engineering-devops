#!/usr/bin/python3
"""Script to print top_ten post for asubreddit"""
import requests


def top_ten(subreddit):
    """Function to print title of top 10 hot posts on a subreddit."""
    url = "https://www.reddit.com/dev/api/r/{}/hot/.json".format(subreddit)
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
