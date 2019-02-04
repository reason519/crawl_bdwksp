# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


response=requests.get('https://wenku.baidu.com/video/course/v/96341d2b75cb2b5a24dfc03debc1b4e6?autoPlay=1&channel=videounit')
response.encoding = 'gb2312'

soup=BeautifulSoup(response.text,'lxml')

chaps=soup.select('ul[class="chapter-list"]')

driver=webdriver.Chrome()

count=0
for chap in chaps[0].findAll('li'):
    count+=1
    print(count,chap.a['href'])
    spans=chap.a.findAll('span')
   # print(spans[0].string,spans[1].string)
    
    with open('E://1/'+spans[0].string+' '+spans[1].string+'.mp4','wb') as f:
        driver.get('https://wenku.baidu.com'+chap.a['href'])
        element=driver.find_element_by_tag_name('video')
        video=requests.get(element.get_attribute('src'))
        f.write(video.content)
        
    
 #   response=requests.get('https://wenku.baidu.com'+chap.a['href'])
    
#    video_soup=BeautifulSoup(response.text,'lxml')
    
#    video_url=video_soup.select('div[id="mediaSpace"]')[0]
 #   print(video_url)
 #   print(video_url.video['src'])
    
    
    
    
    