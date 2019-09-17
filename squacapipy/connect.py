import json
import requests
import os

_API_TOKEN = "token " + os.getenv('SQUAC_API_TOKEN')
_API_BASE = os.getenv('SQUAC_API_BASE')

headers = {'Content-Type': 'application/json',
           'Authorization': _API_TOKEN }


def url(resource):
    print(_API_BASE + resource)
    return _API_BASE + resource

