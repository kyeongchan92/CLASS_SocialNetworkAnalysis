# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:20:15 2020

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
def get_singer(t):
    
    try:
        pattern1 = re.compile('\[(.+)\]')
        result = re.search(pattern1, t)
        pattern2 = re.compile(':(.+)')
        result2 = re.search(pattern2, result.group(1))
        answer = result2.group(1)
        
    except AttributeError as e:
        answer = ''
        
    return answer

#%%############################################################################
def get_launching_date(t):
    
    try:
        pattern = re.compile('\d{4}[-]\d{2}[-]\d{2}')
        result = re.search(pattern, t)
        answer = result.group()
    except AttributeError as e:
        answer = ''
    
    return answer

#%%############################################################################
def get_title(t):
    try:
        result = re.search(r'[]](.+)[-]', t)
        answer = result.group(1).strip()
    except AttributeError as e:
        answer = ''
        
    return answer

#%%############################################################################
driver = webdriver.Chrome('D:/GoogleDriveSync/16_github_repos/Crawling/chromedriver.exe')
driver.get('https://www.komca.or.kr/srch2/srch_01.jsp')

#%%############################################################################
def update_singer(singer_nm):
    driver.find_element_by_css_selector('#singer').clear() #id clear하기
    driver.find_element_by_css_selector('#singer').send_keys('{}'.format(singer_nm)) #id 넣기
    driver.find_element_by_css_selector('.btn.black').click()

#%%############################################################################
def remove_comma(t):
    return t.replace(',', '')

#%%############################################################################
# 크롤

# tag1, tag2
# tag1 tag2 => 자손 (find_all(recursive=True))
# tag1 > tag2 => 자식 (find_all(recursive=False))
# tag1 + tag2 => 형제(다음노드) => tag2

def get_data():
    dom = BeautifulSoup(driver.page_source, 'html.parser')
    total_song_n = int(remove_comma(dom.select_one('.result_total > span').text))
    if total_song_n % 10 == 0:
        pagenum = total_song_n // 10
    else:
        pagenum = total_song_n // 10 + 1
        
    for page in range(1, pagenum+1):
        # print('****************************************page : {}'.format(page))
        dom = BeautifulSoup(driver.page_source, 'html.parser')
        i = 1
        for box in dom.select('.result_article'):
            title = get_title(box.select_one('.tit2').text.strip())
            singer = get_singer(box.select_one('.works_info dd > p:nth-of-type(2)').text.strip())
            date = get_launching_date(box.select_one('.metadata').text.strip())
            # print('저작물명 : {}'.format(title))
            # print('가수명 : {}'.format(singer))
            # print('공표일자 : {}'.format(date))
            d['저작물명'].append(title)
            d['가수명'].append(singer)
            d['공표일자'].append(date)
            #작사가, 작곡가
            l = ''
            c = ''
            for tr in box.select('tbody > tr'):
                if tr.select_one('td').text.strip() == 'A':
                    lyricist = tr.select_one('td:nth-of-type(2)').text.strip()
                    # print('lyricist : {}'.format(lyricist))
                    if l == '':
                        l += lyricist
                    else:
                        l += ', ' + lyricist
                elif tr.select_one('td').text.strip() == 'C':
                    composer = tr.select_one('td:nth-of-type(2)').text.strip()
                    # print('composer : {}'.format(composer))
                    if c == '':
                        c += composer
                    else:
                        c += ', ' + composer
            d['작사가'].append(l)
            d['작곡가'].append(c)
            # print('------------------------------{}'.format(i))
            i+=1
        print('page : {} / {}'.format(page, pagenum))
        #다음 페이지 클릭
        if page%10 == 0:
            driver.find_element_by_css_selector('.pagination > a:nth-of-type({})'.format(3)).click()        
        elif page == pagenum:
            # print('page : {}'.format(page))
            # print('pagenum : {}'.format(pagenum))
            break
        else:
            driver.find_element_by_css_selector('.pagination > span > a:nth-of-type({})'.format(page % 10 + 1)).click()    
        time.sleep(1)        
#%%############################################################################
d = {
     '가수명' : [],
     '저작물명' : [],
     '공표일자' : [],
     '작곡가' : [],
     '작사가' : []
     }

#%%############################################################################
singer_n = len(singers)
for idx, singer in enumerate(singers):
    print('singer = {}, index = {}/{}'.format(singer, idx, singer_n))
    update_singer(singer)
    time.sleep(1)
    get_data()

#%% 박건 빼고 다시, 박정민빼고 다시, 비 부터 다시 #################################

for idx, singer in enumerate(singers[35:]):
    print('singer = {}, index = {}/{}'.format(singer, idx+124, singer_n))
    update_singer(singer)
    time.sleep(3)
    get_data()

#%% 데이터 저장 ################################################################
df = pd.DataFrame(d)
df.to_csv('data/저작물데이터.csv')


#%%
for _ in range(17):
    d['가수명'].pop()
    d['저작물명'].pop()
    d['공표일자'].pop()
    d['작곡가'].pop()
    d['작사가'].pop()

