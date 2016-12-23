#browser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import time


browser = webdriver.Firefox()

#scrape youtube urls
def search(msg,msgTitle):

	time.sleep(5)

	browser.get("https://www.youtube.com/")
	time.sleep(10)
	vid = browser.find_element_by_name("search_query")
	vid.send_keys(msg+" "+msgTitle)
	time.sleep(8)
	vid.send_keys(Keys.RETURN)


	file2 = open('playlistfinal.txt','w')

	file2.write(linkLocation)
	file2.write("\n")
	file2.close()
	file2 = open('playlistfinal.txt')
	return file2.read()
	
file = open('playlist11.txt','r')

#list format
# Singer1 - SongTitle1
# Singer2 - SongTitle2

for line in file:
	para = line.split(" - ")
	para[1] = para[1].rstrip()
	
	
	search(para[0],para[1])
