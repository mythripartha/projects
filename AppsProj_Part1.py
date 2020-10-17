#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib as plt
#import from scipi
from scipy import stats
import random


# In[17]:


Google = pd.read_excel('googleplaystore.xlsx')
Google.head(3)


# In[15]:


Apple = pd.read_excel('AppleStore.xlsx')
#extracting the columns needed
Apple.head(3)


# In[20]:


# Subset our DataFrame object Google by selecting just the variables ['Category', 'Rating', 'Reviews', 'Price']
google_cols = Google[['Category', 'Rating','Reviews', 'Price']]
google_cols.head(3)


# In[22]:


apple_cols = Apple[['prime_genre', 'user_rating', 'rating_count_tot', 'price']]
apple_cols.head(3)

