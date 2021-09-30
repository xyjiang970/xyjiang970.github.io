#!/usr/bin/env python
# coding: utf-8

# # COVID-19 Analysis
# 
# Purpose of this project is to look into some covid statistics. We will see what the correlation between human development index (HDI) and mortality rate (total deaths attributed to COVID-19). 
# 

# In[5]:


# Importing needed libraries for data analysis.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[6]:


# Loading "Our World in Data's" Covid csv file into a dataframe.

df = pd.read_csv('owid-covid-data.csv')


# In[14]:


# Taking a look at what our dataframe looks like.

df


# In[8]:


# Taking a look at the summary of our datafram (specifically the values and columns).

df.info(verbose = True)


# In[9]:


# Filtering by the most recent date when this project is started, which is Aug. 15th, 2021

most_recent_date = df[df['date'] == '2021-08-30']

# Top tourist destinations and most populus countries in Asia, Europe, and North America
countries = ['France','Spain','United States','Italy','Turkey', 'Malaysia',
             'Mexico','Taiwan','Germany','United Kingdom','Cuba','Canada',
             'Japan','South Korea','Netherlands','India','Guatemala','Haiti',]

countries_of_interest = most_recent_date[most_recent_date['location'].isin(countries)]


# In[10]:


# Let's see what that looks like (only looking into the first 5 rows):

countries_of_interest.head()


# In[11]:


# Creating a new DF with only the columns needed for now.

# The specific columns we are looking to use are:

# 1 -> continent
# 2 -> location (country)
# 4 -> total_cases
# 7 -> total_deaths
# 31 -> positive_rate
# 36 -> people_fully_vaccinated
# 45 -> stringency_index
# 46 -> population
# 59 -> life_expectancy
# 60 -> human_development_index

data = countries_of_interest.iloc[:,[1,2,4,7,36,31,45,46,59,60]] 

# Using iloc here because it is more efficient than typing out each name of the column.


# In[12]:


# Sorting in alphabetical order by continent.

data.sort_values('continent')


# In[13]:


# Filling in NaN values manually with the most recent info. on that datapoint online.

data.at[104556,"stringency_index"] = 56.48 # stringency_index of Taiwan is 56.48 (2021)
data.at[104556, "human_development_index"] = 0.916 # HDI of Taiwan is  (201)
#data.at[65524, "positive_rate"] =  #

data.sort_values('continent')


# In[ ]:




