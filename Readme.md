### References
* [Web Scraping with Beautiful Soup](https://realpython.com/beautiful-soup-web-scraper-python/)
* [requests-html code](https://github.com/kennethreitz/requests-html)
* [requests-html documentation](https://requests.readthedocs.io/projects/requests-html/en/latest/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [raspberry pi 32bit fix](https://stackoverflow.com/questions/66588194/requests-html-results-in-oserror-errno-8-exec-format-error-when-calling-html)

### Some notes about rendering
* After reading a few selenium articles, [this blog](https://www.zenrows.com/blog/selenium-python-web-scraping#headless-chrome), and [this article](https://medium.com/ymedialabs-innovation/web-scraping-using-beautiful-soup-and-selenium-for-dynamic-page-2f8ad15efe25), it became clear that one should use the `sleep` parameter to give the page time to render.

### Requests-HTML vs Selenium
The following are notes for Requests-HTML.  See the Readme_Selenium.md for notes about getting started with Selenium

### Simple script
Simple example of scraping the words "Log In" on [Facebook's home page](https://www.facebook.com/)
```
(.venv) $ python simple_fb_test.py 

200
<button class="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy" data-testid="royal_login_button" id="u_0_5_gE" name="login" type="submit" value="1">Log In</button>
Log In

```
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
