# def scrape_this():
#     #get_ipython().system('jupyter nbconvert --to script mission_to_mars.ipynb --output scrape_mars')
#     ###return dictList_image_urls
#     hemisphere_image_urls = {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"}
#     # {"title": "Cerberus Hemisphere", "img_url": "/Users/shikhapurohit/Desktop/butterfly.png"},
#     # {"title": "Schiaparelli Hemisphere", "img_url": "/Users/shikhapurohit/Desktop/butterfly.png"},
#     # {"title": "Syrtis Major Hemisphere", "img_url": "/Users/shikhapurohit/Desktop/butterfly.png"}}
#     return hemisphere_image_urls

import nbconvert
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from selenium import webdriver
import splinter
from splinter import Browser
import pprint

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


url = 'https://mars.nasa.gov/news/'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# Retrieve the parent div for the latest News article
news_title = soup.find('div', class_='content_title').a.text

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

featured_image_url = soup.find('img', class_="fancybox-image")

url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')


mars_weather = soup.find('p', 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
fact_string = pd.read_html('http://space-facts.com/mars/')[0]
#print(fact_string)


html_facts_string = fact_string.to_html()
soup = BeautifulSoup(html_facts_string, 'html.parser')

dict_temp = {}
titles = []
image_urls = []
dictList_image_urls = []

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[267]:


#Finding all the titles for the hemispheres from the website:
hemisphere_descriptions = soup.find_all('div', class_='description')
for description in hemisphere_descriptions:
    hemisphere_title = description.a.h3.text
    titles.append(hemisphere_title)
    print(hemisphere_title)

url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced?open=true'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

imageSrc = soup.find('img',class_='wide-image')['src']

#Add this url to the original image url list:
image_urls.append(imageSrc)
#--------------
# Add the above image urls and the hemisphere names to the list of dictionaries.
dict_temp['title'] = titles[0]
dict_temp['image_url'] = imageSrc

dictList_image_urls.append(dict_temp.copy())

url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

imageSrc = soup.find('img',class_='wide-image')['src']

#Add this url to the original image url list:
image_urls.append(imageSrc)

#--------------
# Add the above image urls and the hemisphere names to the list of dictionaries.
dict_temp['title'] = titles[1]
dict_temp['image_url'] = imageSrc

dictList_image_urls.append(dict_temp.copy())

url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

imageSrc = soup.find('img',class_='wide-image')['src']

#Add this url to the original image url list:
image_urls.append(imageSrc)
#--------------
# Add the above image urls and the hemisphere names to the list of dictionaries.
dict_temp['title'] = titles[2]
dict_temp['image_url'] = imageSrc

dictList_image_urls.append(dict_temp.copy())

url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

imageSrc = soup.find('img',class_='wide-image')['src']

#Add this url to the original image url list:
image_urls.append(imageSrc)
#--------------
# Add the above image urls and the hemisphere names to the list of dictionaries.

dict_temp['title'] = titles[3]
dict_temp['image_url'] = imageSrc

dictList_image_urls.append(dict_temp.copy())

# Print the resulting List of Dictionaries containing Mars hemisphere titles and the associated image url:
from pprint import pprint
#pprint(dictList_image_urls)
print(dictList_image_urls)


# In[273]:


# Write a method to convert this notebook to a .py file
def scrape_this():
    result_dict = {}
    result = zip(titles, image_urls)
    result_dict = dict(result)
    #get_ipython().system('jupyter nbconvert --to script mission_to_mars.ipynb --output scrape_mars')
    ###return dictList_image_urls --- this doesn't show as it is a list of dictionaries????
    return result_dict
    
    # hemisphere_image_urls = [
    # {"title": "Valles Marineris Hemisphere", "img_url": "/Users/shikhapurohit/Desktop/butterfly.png"},
    # {"title": "Cerberus Hemisphere", "img_url": "/Users/shikhapurohit/Desktop/butterfly.png"},
    # {"title": "Schiaparelli Hemisphere", "img_url": "/Users/shikhapurohit/Desktop/butterfly.png"},
    # {"title": "Syrtis Major Hemisphere", "img_url": "/Users/shikhapurohit/Desktop/butterfly.png"}]
    # # hemisphere_image_urls = {"title": "Valles Marineris Hemisphere", "img_url": "/Users/shikhapurohit/Desktop/butterfly.png"}
    # return hemisphere_image_urls
