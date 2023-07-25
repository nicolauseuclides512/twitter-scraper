import time
import csv
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
base_Url = u'https://twitter.com/search?q='

query = u'ma\'aruf amin'
url = base_Url + query

browser.get(url)
time.sleep(2)

body = browser.find_element_by_tag_name('body')

for _ in range(2000):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

search_results = browser.find_elements_by_xpath("//div[@class='content']")

scraped_data = []
username = []
tweet = []
for search_result in search_results:
    usernames = search_result.find_elements_by_css_selector('div.stream-item-header > a > span.FullNameGroup > strong')
    tweets = search_result.find_elements_by_class_name('tweet-text')
    for usernamei in usernames:
        username = usernamei.text
    for tweeti in tweets:
        tweet = tweeti.text
    scraped_data.append((username, tweet))  # put in tuples

df = pd.DataFrame(data=scraped_data, columns=["Username", "Tweet"])
df.to_csv("tweet-maaruf.csv")

browser.quit()
