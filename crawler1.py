#!/usr/bin/python

from HTMLParser import HTMLParser
import urllib2

class Parser1(HTMLParser):
	def handle_starttag(self,tag,attrs):
		if (tag=='a'):
			for a in attrs:
				if (a[0]=='href'):
					 if (a[1].find('http')>=0):
						print(a[1])
				
def func1():
	try:
		url='https://www.python.org'
		request=urllib2.Request(url)
		response=urllib2.urlopen(request)
		parser=Parser1()
		parser.feed(response.read())
	except:
		print('Error occured!\nCould not fetch links') 

func1()
