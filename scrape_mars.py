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

# Main dictionary
combined_dict = {}

url = 'https://mars.nasa.gov/news/'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# Retrieve the parent div for the latest News article
news_title = soup.find('div', class_='content_title').a.text

#Add this value to the main dictionary:
combined_dict['newsTitle'] = news_title

# Retrieve the parent div for the latest News text
news_text = soup.find('div', class_='article_teaser_body').text
news_text
#Add this value to the main dictionary:
combined_dict['newsParagraph'] = news_text

url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

featured_image_url = soup.find('img')['src']
#featured_image_url = featured_image['src']

#Add this value to a dictionary:
combined_dict['featuredImage'] = featured_image_url

url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')


mars_weather = soup.find('p', 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
#Add this value to a dictionary:
combined_dict['twitterMarsWeather'] = mars_weather

fact_string = pd.read_html('http://space-facts.com/mars/')[0]
#print(fact_string)

html_facts_string = fact_string.to_html()
soup = BeautifulSoup(html_facts_string, 'html.parser')

#Add this value to a dictionary:
combined_dict['marsFactsHTML'] = html_facts_string

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
    #Add this value to the main dictionary:
    combined_dict[hemisphere_title] = hemisphere_title
    titles.append(hemisphere_title)
    print(hemisphere_title)

# The following are two parts to the url we are going to create for the hemisphere images:
url_part1 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/'
url_part3 = '.tif/full.jpg'

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

#extracting and making an image url:
url_temp = imageSrc.split("_",1)[1]
url_part2 = url_temp.split(".",1)[0]
new_url = url_part1+url_part2+url_part3
print(url_part2)
print(new_url)

#Add this value to a dictionary:
#combined_dict['url_1'] = imageSrc
combined_dict['url_1'] = new_url

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

#extracting and making an image url:
url_temp = imageSrc.split("_",1)[1]
url_part2 = url_temp.split(".",1)[0]
new_url = url_part1+url_part2+url_part3
print(url_part2)
print(new_url)

#Add this value to a dictionary:
#combined_dict['url_1'] = imageSrc
combined_dict['url_2'] = new_url

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

#extracting and making an image url:
url_temp = imageSrc.split("_",1)[1]
url_part2 = url_temp.split(".",1)[0]
new_url = url_part1+url_part2+url_part3
print(url_part2)
print(new_url)

#Add this value to a dictionary:
#combined_dict['url_1'] = imageSrc
combined_dict['url_3'] = new_url

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

#extracting and making an image url:
url_temp = imageSrc.split("_",1)[1]
url_part2 = url_temp.split(".",1)[0]
new_url = url_part1+url_part2+url_part3
print(url_part2)
print(new_url)

#Add this value to a dictionary:
#combined_dict['url_1'] = imageSrc
combined_dict['url_4'] = new_url

# Print the resulting List of Dictionaries containing Mars hemisphere titles and the associated image url:
from pprint import pprint
#pprint(dictList_image_urls)
print(dictList_image_urls)


# In[273]:


# Write a method to convert this notebook to a .py file
def scrape_this():
    return combined_dict
    #---- PREVIOUS CODE SHOWING ONLY HEMISPHERES --------
    # result_dict = {}
    # result = zip(titles, image_urls)
    # result_dict = dict(result)
    # #get_ipython().system('jupyter nbconvert --to script mission_to_mars.ipynb --output scrape_mars')
    # ###return dictList_image_urls --- this doesn't show as it is a list of dictionaries????
    # return result_dict
    #--------------------------------------------------------
    # hemisphere_image_urls = [
    # {"title": "Valles Marineris Hemisphere", "img_url": "/Users/shikhapurohit/Desktop/butterfly.png"},
    # {"title": "Cerberus Hemisphere", "img_url": "/Users/shikhapurohit/Desktop/butterfly.png"},
    # {"title": "Schiaparelli Hemisphere", "img_url": "/Users/shikhapurohit/Desktop/butterfly.png"},
    # {"title": "Syrtis Major Hemisphere", "img_url": "/Users/shikhapurohit/Desktop/butterfly.png"}]
    # # hemisphere_image_urls = {"title": "Valles Marineris Hemisphere", "img_url": "/Users/shikhapurohit/Desktop/butterfly.png"}
    # return hemisphere_image_urls
