from bs4 import BeautifulSoup as bs
import requests
import time
import os

def shout(msg):
	while True:
		os.system('say ' + msg)
while True:
	page = requests.get("https://in.bookmyshow.com/buytickets/avengers-infinity-war-hyderabad/movie-hyd-ET00053419-MT/20180505")
	soup = bs(page.content, 'html.parser')
	venues = soup.find_all('a', class_='__venue-name')
	for venue in venues:
		strong = venue.find('strong')
		print(strong.contents[0])
		cinemaName = strong.contents[0]
		if "prasad" in cinemaName.lower():
			shout("Oh fuck, Oh Fuck, IMAX has been added")

	time.sleep(180)
