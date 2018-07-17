import requests
import re
from bs4 import BeautifulSoup


def Uncubed(max_pages):
	page = 1
	while page <= max_pages:
		url = 'https://uncubed.com/jobs/category/analytics_data_science/search?keyword=data+scientist&page=' + str(page)
		response = requests.get(url)
		content = response.content
		parser = BeautifulSoup(content, 'html.parser')
		for company in parser.find_all('p'):
			print(company.string)
		# for post in parser.find_all('div', class_ = 'job-info-container'):
			# job_title = post.find('p', class_ = 'title').string
			# location = post.find('span', class_ = 'location').string[3:]

			# print(company + " is looking for a " + job_title + " in " + location)
		page += 1
		
Uncubed(1)


# <div class="job-info-container">
# <p class="title">
              # Insight Data Engineering Fellows Program - New York
            # </p>
# <p>
  #            Insight Fellows Programs
   #           <span class="location"> - Starting September 10, 2018 (Accepting Late Applications) - New York</span>
# </p>
# </div>
