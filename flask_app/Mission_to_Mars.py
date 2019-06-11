#!/usr/bin/env python
# coding: utf-8

# # Setting UP 

# In[15]:


# Import BeautifulSoup
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd


# In[20]:


# Set Executable Path & Initialize Chrome Browser
#MAC
executable_path = {"executable_path": "/Users/HayesMartens/Downloads/chromedriver"}
browser = Browser('chrome', **executable_path, headless=False)


# # Visit the NASA mars NEW SITES

# In[21]:


# Visit the mars nasa new site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[22]:


html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')

# print(news_soup)

# slide element everythin in the 
# <ul class="item_list">
#     <li class="slide">
#     ....
# </ul>
slide_element = news_soup.select_one('ul.item_list li.slide')


# In[23]:


slide_element.find("div", class_="content_title")


# In[24]:


# Use the parent element to find the first a tag and save it as news_title
news_title = slide_element.find('div', class_="content_title").get_text()
news_title 


# In[25]:


news_paragraph = slide_element.find('div', class_="article_teaser_body").get_text()
news_paragraph


# # JPL SPACE IMAGES FEATURED IMAGE

# In[27]:


# Visit URL
executable_path = {"executable_path": "/Users/HayesMartens/Downloads/chromedriver"}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[28]:


# Asking splinter to go to the site hit a button with class name full_image
# <button class="full_image">Full Image</button>
full_image_button = browser.find_by_id('full_image')
full_image_button.click()


# In[29]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_element = browser.find_link_by_partial_text('more info')
more_info_element.click()


# In[30]:


# Parse the results html with soup
html = browser.html
image_soup = BeautifulSoup(html, 'html.parser')


# In[31]:


img_url = image_soup.select_one('figure.lede a img').get('src')
img_url


# In[32]:


# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url}'
img_url


# # MARS WEATHER

# In[35]:


executable_path = {"executable_path": "/Users/HayesMartens/Downloads/chromedriver"}
browser = Browser('chrome', **executable_path)
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)


# In[36]:


html = browser.html
weather_soup = BeautifulSoup(html, 'html.parser')


# In[38]:


# First find a tweet with the data-name `Mars Weather`
mars_weather_tweet = weather_soup.find('div', 
                                       attrs={
                                           "class": "tweet", 
                                            "data-name": "Mars Weather"
                                        })
print(mars_weather_tweet)


# In[39]:


# Next search within the tweet for p tag containing the tweet text
mars_weather = mars_weather_tweet.find('p', 'tweet-text').get_text()
mars_weather


# In[40]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[41]:


hemisphere_image_urls = []

# First get a list og all the hemisphers
links = browser.find_by_css('a.product-item h3')
for item in range(len(links)):
    hemisphere = {}
    
    # We have to find the element on each loop to avoid a stale element exception
    browser.find_by_css('a.product-item h3')[item].click()
    
    # Next we find the Sample Image anchor tage and extract the href
    sample_element = browser.find_link_by_text('Sample').first
    hemisphere['img_url'] = sample_element['href']
    
    
    # Get Hemispher title 
    hemisphere['title'] = browser.find_by_css('h2.title').text
    
    #Append hemisphere object to list
    hemisphere_image_urls.append(hemisphere)
    
    # Finally, we navigate backwards
    browser.back()
    
    
    
    


# In[50]:


hemisphere_image_urls


# # MARS FACTS 

# In[42]:


import pandas as pd
df = pd.read_html('https://space-facts.com/mars/')[0]
print(df)
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[43]:


df.to_html()


# In[44]:


browser.quit()


# In[ ]:




