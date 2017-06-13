#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 23:12:39 2017

@author: kyujin
"""

# Adding soft wrap
#wrong access
# https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=view_politics&pool=cbox5&_callback=jQuery112401627809877692319_1497271834908&lang=ko&country=KR&objectId=news025%2C0002692654&categoryId=&pageSize=10&indexSize=10&groupId=&listType=OBJECT&page=1&sort=FAVORITE&_=1497271834911


import json
import requests
import re
from time import sleep

f = open('comments.txt',"w",encoding="utf8")
f.write("USER" + "\t" + "LIKE COUNT" + "\t" + "DISLIKE COUNT" + "\t" + "COMMENT" + "\t" + "TIME" + "\t" + "PLATFORM" + "\n")


my_referer = "http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=memo_week&oid=025&aid=0002692654&date=20170308&type=1&rankingSectionId=000&rankingSeq=1"
url = re.split('&|=',my_referer)
oid_index = url.index('oid')+1
oid = url[oid_index]
aid_index = url.index('aid')+1
aid = url[aid_index]
pageSize=100
page=1

while(True):

    url = "https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=view_politics&pool=cbox5&lang=ko&country=KR&objectId=news" + oid + "%2C" + aid + "&categoryId=&pageSize=" + str(pageSize) + "&indexSize=10&groupId=&page=" + str(page) + "&initialize=true&useAltSort=true&replyPageSize=30&moveTo=&sort=favorite"

    resp = requests.get(url, headers={'referer': my_referer})

    result = resp.text
    result = result.replace("_callback","")
    result = result.replace("(","[")
    result = result.replace(")","]")
    result = result.replace(";","")
    result = result.replace("\n","")

    data = json.loads(result)
    res = data[0]['result']
    comments = res['commentList']

    for each_comment in comments: 
        user = each_comment['userName']
        like_count = each_comment['sympathyCount']  
        dislike_count = each_comment['antipathyCount']
        content = each_comment['contents']
        content = content.replace("\t","")
        content = content.replace("\n","")
        time = each_comment['regTimeGmt']
        platform = each_comment['profileType']
    
        f.write(user + "\t" + str(like_count) + "\t" + str(dislike_count) + "\t" + content + "\t" + time + "\t" + platform + "\n")
    
    if (page == 20): 
        break
    
    page += 1
    sleep(10)
    print("printing page " + str(page))

f.close()
