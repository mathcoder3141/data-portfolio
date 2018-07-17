import requests
import re
from bs4 import BeautifulSoup


def aiPosts(max_pages):
	page = 1
	while page <= max_pages:
		url = 'http://aiweirdness.com/page/' + str(page)
		response = requests.get(url)
		content = response.content
		parser = BeautifulSoup(content, 'html.parser')
		for post in parser.find_all('article', class_=re.compile('^post type-text')):
			print(post.h2.string)
		page += 1
		
aiPosts(5)