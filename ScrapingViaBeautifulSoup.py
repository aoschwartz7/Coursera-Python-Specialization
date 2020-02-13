# Scraping data from HTML using BeautifulSoup:
# Use urllib to read an HTML page and then use BeautifulSoup to extract the
# href attributes from the anchor tags

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Prompt for a web address
url = input('Enter - ')
# Open web page, read data
html = urllib.request.urlopen(url, context=ctx).read()
# Pass data to BeautifulSoup parser
soup = BeautifulSoup(html, "html.parser")
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
