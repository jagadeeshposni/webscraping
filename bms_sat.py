from bs4 import BeautifulSoup as bs
import requests
import time
import os

def shout(msg):
	while True:
		os.system('say ' + msg)
while True:
	page = requests.get("https://in.bookmyshow.com/buytickets/avengers-endgame-hyderabad/movie-hyd-ET00100559-MT/20190427")
	soup = bs(page.content, 'html.parser')
	venues = soup.find_all('a', class_='__venue-name')
	print("============================================================")
	for venue in venues:
		strong = venue.find('strong')
		print(strong.contents[0])
		cinemaName = strong.contents[0]
		if "amb cinemas" in cinemaName.lower():
			shout("Saturday, AMB Cinemas is available")
		if "sujana" in cinemaName.lower():
			shout("Saturday,  Forum mall is available")
		
		#if "malkajgiri" in cinemaName.lower():
		#	shout("malkajgiri")

	time.sleep(60)
