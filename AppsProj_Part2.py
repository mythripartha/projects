#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib as plt
#import from scipi
from scipy import stats
import random


# In[71]:


google = 'googleplaystore.csv'
Google = pd.read_csv(google)

# Using the head() pandas method, observe the first three entries.
Google.head(3)


# In[74]:


apple = 'AppleStore.csv'

Apple = pd.read_csv(apple)
Apple.head(3)


# In[20]:


# Subset our DataFrame object Google by selecting just the variables ['Category', 'Rating', 'Reviews', 'Price']
google_cols = Google[['Category', 'Rating','Reviews', 'Price']]
google_cols.head(3)


# In[22]:


apple_cols = Apple[['prime_genre', 'user_rating', 'rating_count_tot', 'price']]
apple_cols.head(3)


# In[29]:


# Using the dtypes feature of pandas DataFrame objects, check out the data types within our Apple dataframe.
# Are they what you exporting
Apple.dtypes


# In[30]:


Google.dtypes


# In[75]:


Google['Price'].unique()


# In[95]:


# Let's check which data points have the value 'Everyone' for the 'Price' column by subsetting our Google dataframe.
Google[Google['Price']=='Everyone']


# In[97]:


#Eliminating that row
Google = Google[Google['Price'] != 'Everyone']
#Check the unique values 
Google['Price'].unique()


# In[98]:


# Let's create a variable called nosymb.
# This variable will take the Price column of Google and apply the str.replace() method. 
# Remember: we want to find '$' and replace it with nothing, so we'll have to write approrpiate arguments to the method to achieve this. 
nosymb = Google['Price'].str.replace('$','')

# Now we need to do two things:
# i. Make the values in the nosymb variable numeric using the to_numeric() pandas method.
# ii. Assign this new set of numeric, dollar-sign-less values to Google['Price']. 
# You can do this in one line if you wish.
Google['Price'] = pd.to_numeric(nosymb)


# In[99]:


# Use the function dtypes. 
Google.dtypes


# In[101]:


# Convert the 'Reviews' column to a numeric data type. 
# Use the method pd.to_numeric(), and save the result in the same column.
Google['Reviews'] = pd.to_numeric(Google['Reviews'])


# In[102]:


Google.dtypes


# In[103]:


# Create a column called 'platform' in both the Apple and Google dataframes. 
# Add the value 'apple' and the value 'google' as appropriate. 
Apple['platform'] = 'apple'
Google['platform'] = 'google'


# In[108]:


# Create a variable called old_names where you'll store the column names of the Apple dataframe. 
# Use the feature .columns.
old_names = Apple.columns

# Create a variable called new_names where you'll store the column names of the Google dataframe. 
new_names = Google.columns
# Use the rename() DataFrame method to change the columns names. 
# In the columns parameter of the rename() method, use this construction: dict(zip(old_names,new_names)).
Apple = Apple.rename(columns = dict(zip(old_names,new_names)))


# In[109]:


# Let's use the append() method to append Apple to Google. 
# Make Apple the first parameter of append(), and make the second parameter just: ignore_index = True.
df = Google.append(Apple, ignore_index = True)

# Using the sample() method with the number 12 passed to it, check 12 random points of your dataset.
df.sample(12)


# In[ ]:


# Lets check first the dimesions of df before droping `NaN` values. Use the .shape feature. 
print(df.shape)

# Use the dropna() method to eliminate all the NaN values, and overwrite the same dataframe with the result. 
# Note: dropna() by default removes all rows containing at least one NaN. 
df =  df.dropna()

# Check the new dimesions of our dataframe. 
print(df.shape)


# In[106]:


# Subset your df to pick out just those rows whose value for 'Reviews' is equal to 0. 
# Do a count() on the result. 
df[df['Reviews'] == 0].count()


# In[ ]:


# Eliminate the points that have 0 reviews.
# An elegant way to do this is to assign df the result of picking out just those rows in df whose value for 'Reviews' is NOT 0.
df = df[df['Reviews'] != 0]


# In[110]:


# To summarize analytically, let's use the groupby() method on our df.
# For its parameters, let's assign its 'by' parameter 'platform', and then make sure we're seeing 'Rating' too. 
# Finally, call describe() on the result. We can do this in one line, but this isn't necessary. 
df.groupby(by = 'platform')['Rating'].describe()


# In[111]:


# Call the boxplot() method on our df.
# Set the parameters: by = 'platform' and column = ['Rating'].
df.boxplot(by= 'platform', column = ['Rating'], grid=False, rot=45, fontsize=15)

