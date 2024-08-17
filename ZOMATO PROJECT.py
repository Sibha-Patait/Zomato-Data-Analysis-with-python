#!/usr/bin/env python
# coding: utf-8

# # Zomato data anlaysis project 

# # Step 1 - Importing Libraries 

# In[ ]:


pandas is used for data manipulation and analysis.
numpy is used for numerical operations.
matplotlib.pyplot and seaborn are used for data visualization.


# In[2]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 


# # Step 2 - create the data frame

# In[4]:


dataframe = pd.read_csv("Zomato data .csv")
print(dataframe)


# In[5]:


dataframe


# # convert the data type of column - rate

# In[7]:


def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())
                                           


# In[8]:


dataframe.info()


# # Type of Resturant 

# In[9]:


dataframe.head()


# In[10]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("type of resturant")


# # conclusion - majority of the resturant falls in dining category 

# In[11]:


dataframe.head()


# In[14]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c="green", marker="o")
plt.xlabel("Type of resturant", c="red", size=20)
plt.ylabel("Votes", c="red",size =20)


# # conclusion - dinning resturant has recieved maximum votes

# In[15]:


dataframe.head()


# In[16]:


plt.hist(dataframe['rate'],bins=5)
plt.title("ratings distribution")
plt.show()


# # conclusion - the majority resturants recieved ratings from 3.5 to 4

# # Average order spending by couples

# In[17]:


dataframe.head()


# In[18]:


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# # conclusion - the majority of couples prefer resturants with an approximate cost of 300 rupees

# # which mode receives maximum rating

# In[19]:


dataframe.head()


# In[20]:


plt.figure(figsize=(6,6))
sns.boxplot(x='online_order',y = 'rate' , data =dataframe)


# # conclusion - offline order received lower rating in comparison to online order
