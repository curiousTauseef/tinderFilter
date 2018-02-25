import config
from urllib import request
import requests
import json

headers = {
    'app_version': '6.9.4',
    'platform': 'ios',
    "content-type": "application/json",
    "User-agent": "Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)",
}

def get_authorized():
    try:
        req = requests.post(config.host + '/auth',
                        headers=headers,
                        data=json.dumps(
                            {'facebook_token': config.fb_access_token, 'facebook_id': config.fb_user_id})
                        )
        tinder_auth_token = req.json()["token"]
        headers.update({"X-Auth-Token": tinder_auth_token})
    except:
        print("Sorry, unable to grab your Tinder token, did you fill in the config file?")

def get_reccomendations():
    try:
        # Get id of first recommendation
        req = requests.get(config.host + '/user/recs', headers=headers)
        return req.json()["results"]
    except:
        print('Sorry, could not grab requests')

def like(person_id):
    try:
        url = config.host + '/like/%s' % person_id
        r = requests.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not like:", e)


def dislike(person_id):
    try:
        url = config.host + '/pass/%s' % person_id
        r = requests.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not dislike:", e)

def get_user_urls(person_id):
    try:
        url = config.host + '/user/%s' % person_id
        r = requests.get(url, headers=headers)
        r = r.json()["results"]
        user_urls = []
        for photo in r["photos"]:
            user_urls.append(photo["url"])
        return user_urls
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not get images:", e)
    return
