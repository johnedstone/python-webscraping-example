# simple_fb_test.py
"""
References:
    https://realpython.com/beautiful-soup-web-scraper-python/

Changes:
    17-July-2023: added HOST variable headers dictionary
    17-July-2023: tested on 32bit raspberry pi
"""

from requests_html import HTMLSession
from bs4 import BeautifulSoup

HOST = 'www.facebook.com'

headers = {
    'host': HOST,
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'connection': 'keep-alive',
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    'accept-encoding': 'gzip, deflate, br',
    'accept-language':'en-US,en;q=0.5',
}

session = HTMLSession()
r = session.get('https://' + HOST, headers=headers)

print(r.status_code)

r.html.render()
soup = BeautifulSoup(r.html.html, "html.parser")

results = soup.find('button', string='Log In')
print(results)
print(results.text)

# vim: ai et ts=4 sw=4 sts=4 nu
