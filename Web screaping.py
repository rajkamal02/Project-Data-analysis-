#!/usr/bin/env python
# coding: utf-8

# In[72]:


import pandas as pd
import requests
import os
import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
import time


# In[73]:


url = "https://insights.blackcoffer.com/rising-it-cities-and-its-impact-on-the-economy-environment-infrastructure-and-city-life-by-the-year-2040-2/"

page=requests.get(url)


# In[74]:


page.content


# In[75]:


soup =BeautifulSoup(page.content, 'html.parser')


# In[76]:


soup


# In[77]:


title = soup.findAll('h1',attrs = {'class': 'entry-title'})


# In[78]:


title[0].text


# In[79]:


title2 = soup.findAll('div',attrs = {'class': 'td-post-content tagdiv-type'})


# In[80]:


title2


# In[84]:


title2[0].text


# In[85]:


replace_text = title2[0].text.replace('\n'," ")


# In[89]:


replace_text


# In[90]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




