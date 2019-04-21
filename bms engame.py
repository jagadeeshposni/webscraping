from bs4 import BeautifulSoup as bs
import requests
import time
import os

def shout(msg):
	while True:
		os.system('say ' + msg)
while True:
	page = requests.get("https://in.bookmyshow.com/hyderabad/movies/avengers-endgame/ET00090482")

	#page = requests.get("https://in.bookmyshow.com/hyderabad/movies/kalank/ET00074273")
	soup = bs(page.content, 'html.parser')
	showtimes = soup.find_all('a', class_='showtimes btn _cuatro')
	for showtime in showtimes:
		shout("Boom, Boom, Boom, Boom, Boom")
		#strong = venue.find('strong')
		#print(strong.contents[0])
		#cinemaName = strong.contents[0]
		#if "prasad" in cinemaName.lower():
			#shout("Boom, Boom, Boom, Boom, Boom")

	time.sleep(10)
