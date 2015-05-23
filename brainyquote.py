from bs4 import BeautifulSoup
import urllib2

URL = "http://www.brainyquote.com/quotes_of_the_day.html"

def get_quote(url):
	# Avoid 403 - Forbidden error
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = urllib2.Request(url, headers=hdr)
	
	html = urllib2.urlopen(req).read()
	soup = BeautifulSoup(html, 'html.parser')
	quote_image = soup.find("img", class_ ="bqPhotoDefault")
	quote = quote_image['alt']
	print "QOTD: ", quote	

get_quote(URL)
	
	