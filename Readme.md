### Reference
* [Web Scraping with Beautiful Soup](https://realpython.com/beautiful-soup-web-scraper-python/#challenges-of-web-scraping)
* [requests_html](https://github.com/kennethreitz/requests-html)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

### Getting started coding

```
$ python3 -m venv .venv
$ source .venv/bin/activate

$ python3
    Python 3.10.6 (main, May 29 2023, 11:10:38) [GCC 11.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.

>>> from requests_html import HTMLSession
>>> from bs4 import BeautifulSoup

>>> session = HTMLSession()
>>> r = session.get('https://www.facebook.com')

>>> r.status_code
200

>>> r.html.render()
>>> soup = BeautifulSoup(r.html.html, "html.parser")
>>> soup.find('button', string='Log In')
>>> result = soup.find('button', string='Log In')
>>> result.text
```
