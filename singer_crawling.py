# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:37:37 2020

@author: Admin
"""
#%%############################################################################
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from requests.compat import urlparse, urljoin
from urllib.request import urlopen, Request
import requests
from requests.exceptions import HTTPError
import time
import re
import pandas as pd

#%%############################################################################
def canfetch(url, agent='*', path='/'):
    robot = RobotFileParser(urljoin(url, '/robots.txt'))
    robot.read()
    return robot.can_fetch(agent, urlparse(url)[2])


def download(url, params={}, headers={}, method='GET', limit=3):
    if canfetch(url) is False:
        print('[Error] ' + url)
#     else:
    try:
        resp = requests.request(method,
                                url,
                                params=params if method == 'GET' else {},
                                data=params if method == 'POST' else {},
                                headers=headers)
        resp.raise_for_status()
    except HTTPError as e:
        if limit > 0 and e.response.status_code >= 500:
            print(limit)
            time.sleep(1)  # => random
            resp = download(url, params, headers, method, limit-1)
        else:
            print('[{}] '.format(e.response.status_code) + url)
            print(e.response.status_code)
            print(e.response.reason)
            print(e.response.headers)
    return resp


#%%############################################################################
def get_pure_nm(t):
    pattern = re.compile(r'([가-힣\w \.]+)\(*')
    result = re.search(pattern, t)
    
    return result.group(1).replace(" ", "")

#%%############################################################################
resp = download('https://namu.wiki/w/%EA%B0%80%EC%88%98/%ED%95%9C%EA%B5%AD')
dom = BeautifulSoup(resp.text, 'html.parser')

#%%############################################################################
singers = []
for jaeum_list in dom.select('.wiki-list'):
    for line in jaeum_list.select('a'):
        print(get_pure_nm(line.text))
        singers.append(get_pure_nm(line.text))

#%%############################################################################
# 이름 전처리 테스트

t = '에디 킴(sadf)'
pattern = re.compile(r'([가-힣\w \.]+)\(*')
result = re.search(pattern, t)
result.group(1).replace(" ", "")


