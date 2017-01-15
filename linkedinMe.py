# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import urllib

# Initialize variables
firstNames = ["Mohamed", "Mohammed", "Mohamad", "Mohammad", "Muhamad", "Muhammad", "Muhamed", "Muhammed", "Moohammed", "Mahmad", "Mehmed", "Mahamed", "Mahammed", "Muhamet", "Muhammet", "Mahammud", "Mehmet", "Mohd", "Muh", "Mahamid", "Md"]
lastNames = ["Moussa", "Mousa", "Musa"]
totalCount = 0

def processName(firstName, lastName):
	global totalCount
	friendlyFirstName = urllib.quote(firstName.encode('utf8'))
	friendlyLastName = urllib.quote(lastName.encode('utf8'))
	driver.get("https://www.linkedin.com/pub/dir/" + friendlyFirstName + "/" + friendlyLastName)
	htmlSource = driver.page_source
	soup = BeautifulSoup(htmlSource, "lxml")
	if len(soup.findAll("div", {"class": ["professionals", "section"]})) == 1:
		matchesField = soup.findAll("div", {"class": "content"})[-1]
		matchCountText = matchesField.select(".hide-mobile")[0].get_text()
		number = re.search(r'\d+', matchCountText).group()
		totalCount += int(number)
		print firstName + " " + lastName + ": " + str(number)
	elif len(soup.findAll("div", {"id": "profile"})) == 1:
		totalCount += 1
		print firstName + " " + lastName + ": 1"
	else:
		print firstName + " " + lastName + ": 0"

# Set up selenium webdriver
driver = webdriver.Firefox()
# Prime linkedin to avoid signup page
driver.get("https://www.linkedin.com/pub/dir/Mohamed/Moussa")
time.sleep(1)

processName(u"محمد", u"موسى")

for firstName in firstNames:
	for lastName in lastNames:
		processName(firstName, lastName)

print "\nTotal: " + str(totalCount)
