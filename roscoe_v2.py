# roscoe.py
"""
References:
    https://realpython.com/beautiful-soup-web-scraper-python/
    https://requests.readthedocs.io/projects/requests-html/en/latest/

"""

from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re
from pprint import pprint
import sys

HOST = '192.168.1.1'
SCHEME = 'http'      # http or https
TIMEOUT = 30000      # milliseconds to wait to load the page, 30000=30secs
SLEEP = 30           # seconds to render the page (create the DOM)
USE_HEADERS = False  # True or False

headers = {
    'host': HOST,
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'connection': 'keep-alive',
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    'accept-encoding': 'gzip, deflate, br',
    'accept-language':'en-US,en;q=0.5',
}

try:
    session = HTMLSession()

    if USE_HEADERS:
        r = session.get(SCHEME + '://' + HOST, headers=headers)
    else:
        r = session.get(SCHEME + '://' + HOST)

    print(r.status_code)

    r.html.render(timeout=TIMEOUT, sleep=SLEEP)

    #pprint(r.html.html)
    #sys.exit()
    soup = BeautifulSoup(r.html.html, "html.parser")

    results = soup.find(string=re.compile('Enter'))
    print(results)

    results = soup.find('a', string=re.compile('^\d+%$'))
    print(results)

    if results.string:
        number_only = int(results.string.rstrip('%'))
        if number_only > 50:
            print(f'Great, you have {number_only}% battery left!')
        else:
            print(f'Yikes, you have only {number_only}% battery left!')
    else:
        print('The anchor tag with the battery level was not found')

except Exception as e:
    print(f'Exception: {e}')


# vim: ai et ts=4 sw=4 sts=4 nu
