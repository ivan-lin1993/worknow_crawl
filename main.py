#!/usr/bin/python 
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib as url
import requests
from bs4 import BeautifulSoup as bfs
posts=[]
keyword="網頁"

for page in range(1,30,1):
	site="https://worknowapp.com/regions/台北/page/"+str(page);
	result=requests.get(site)
	soup=bfs(result.text)
	articles=soup.findAll(class_='article')
	for i in range(len(articles)):
		article=articles[i]
		if keyword in article.find('h3').get_text():
			print article.find('h3').get_text(),article.find('time').getText(),article.a['href']
	print "page",page
