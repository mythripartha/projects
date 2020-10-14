#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


pets = pd.DataFrame({'sex': np.array(['M', 'M', 'F', 'M', 'F', 'F', 'F', 'M', 'F', 'M']),
                   'age': np.array([21, 45, 23, 56, 47, 70, 34, 30, 19, 62]),
                   'pets': np.array([['cat', 'dog'],
                                    ['hamster'],
                                    ['cat', 'gerbil'],
                                    ['fish', 'hamster', 'gerbil'],
                                    ['cat'],
                                    ['dog'],
                                    ['dog'],
                                    ['cat'],
                                    ['rabbit', 'cat'],
                                    ['dog']])})


# In[3]:


#youngest respondent
pets.loc[pets['age'] == min(pets['age']), 'sex']


# In[4]:


#finding age of person with most pets
#creating num_pets to find the number of pets in each array
pets['num_pets'] = pets['pets'].apply(lambda x: len(x))


# In[9]:


#check that the new column was added
pets


# In[8]:


#locate the number of pets and the highest age of pet owner
pets.loc[pets['num_pets'] == max(pets['num_pets']), 'age']


# In[10]:


#finding most popular pet
pet_series = pets['pets'].apply(pd.Series).stack().reset_index(drop=True)
#print pet series to show 
pet_series


# In[16]:


#count the pets and sort
pet_series.value_counts()


# In[18]:


('dog' in ['dog', 'cat'], 'dog' in ['rabbit'])


# In[19]:


#locate dogs in the list and then find the mean
pets.loc[pets['pets'].apply(lambda x: 'dog' in x), 'age'].mean()

