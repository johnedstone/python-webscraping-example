# simple_fb_test.py
"""
References:
    https://realpython.com/beautiful-soup-web-scraper-python/
"""

from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()
r = session.get('https://www.facebook.com')

print(r.status_code)

r.html.render()
soup = BeautifulSoup(r.html.html, "html.parser")

results = soup.find('button', string='Log In')
print(results)
print(results.text)

