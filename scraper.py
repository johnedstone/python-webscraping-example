# scrapy.py
"""
Getting started with Selenium
    https://www.zenrows.com/blog/selenium-python-web-scraping#wait-for-element
    https://medium.com/ymedialabs-innovation/web-scraping-using-beautiful-soup-and-selenium-for-dynamic-page-2f8ad15efe25

To do: follow up on wait time for rendering to DOM
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless=new')

driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options)

driver.get('https://scrapingclub.com')
driver.quit()

# vim: ai et ts=4 sts=4 sw=4 nu
