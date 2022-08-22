#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Data Visualization Lab**
# 

# Estimated time needed: **45 to 60** minutes
# 

# In this assignment you will be focusing on the visualization of data.
# 
# The data set will be presented to you in the form of a RDBMS.
# 
# You will have to use SQL queries to extract the data.
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# *   Visualize the distribution of data.
# 
# *   Visualize the relationship between two features.
# 
# *   Visualize composition of data.
# 
# *   Visualize comparison of data.
# 

# <hr>
# 

# ## Demo: How to work with database
# 

# In[14]:


get_ipython().run_line_magic('pip', 'install wget')


# Download database file.
# 

# In[1]:





# In[ ]:





# Connect to the database.
# 

# In[4]:


import sqlite3
conn = sqlite3.connect("G:/My Drive/NpowerCanada/IBM Data/m4_survey_data.sqlite") # open a database connection


# Import pandas module.
# 

# In[5]:


import pandas as pd


# ## Demo: How to run an sql query
# 

# In[6]:


# print how many rows are there in the table named 'master'
QUERY = """
SELECT COUNT(*)
FROM master
"""

# the read_sql_query runs the sql query and returns the data as a dataframe
df = pd.read_sql_query(QUERY,conn)
df.head()


# ## Demo: How to list all tables
# 

# In[52]:


# print all the tables names in the database
QUERY = """
SELECT name as Table_Name FROM
sqlite_master WHERE
type = 'table'
"""
# the read_sql_query runs the sql query and returns the data as a dataframe
pd.read_sql_query(QUERY,conn)


# ## Demo: How to run a group by query
# 

# In[8]:


QUERY = """
SELECT Age,COUNT(*) as count
FROM master
group by age
order by age
"""
pd.read_sql_query(QUERY,conn)


# ## Demo: How to describe a table
# 

# In[53]:


table_name = 'master'  # the table you wish to describe

QUERY = """
SELECT sql FROM sqlite_master
WHERE name= '{}'
""".format(table_name)

df = pd.read_sql_query(QUERY,conn)
print(df.iat[0,0])


# # Hands-on Lab
# 

# ## Visualizing distribution of data
# 

# ### Histograms
# 

# Plot a histogram of `ConvertedComp.`
# 

# In[56]:


# your code goes here
import matplotlib as mpl
import matplotlib.pyplot as plt


QUERY = """
SELECT *
FROM master
"""

# the read_sql_query runs the sql query and returns the data as a dataframe
df = pd.read_sql_query(QUERY,conn)
#Scaling by 1000 to make the graphs and numbers ease of visibility
df['ConvertedComp']=df['ConvertedComp']/1000
#Display Size chaning Default has limited visibility for visualization
plt.figure(figsize=(15, 15))

df['ConvertedComp'].plot(kind='hist')
plt.title('Histogram of Distribution of Converted Compensation  Annually')
plt.xlabel("Converted Currency Compensation in Thousand USD")
plt.ylabel("Total Number of Occurences (Frequency)")


# In[39]:


f=(df['ConvertedComp'].describe()*1000)
print(f)


# In[26]:


df['ConvertedComp'].isnull().sum()


# In[21]:


df["Age"].describe()


# In[27]:


#df.columns.values.tolist()
df["Age"].isnull().sum()


# ### Box Plots
# 

# Plot a box plot of `Age.`
# 

# In[22]:


# your code goes here
plt.figure(figsize=(15, 15))
df['Age'].plot(kind='box')
plt.title('Boxplot of Age')
plt.grid()


# ## Visualizing relationships in data
# 

# ### Scatter Plots
# 

# In[ ]:





# In[ ]:





# Create a scatter plot of `Age` and `WorkWeekHrs.`
# 

# In[26]:


# your code goes here
plt.figure(figsize=(15, 15))
plt.scatter(df['Age'],df['WorkWeekHrs'])
plt.title('Scatter plot of age and workweek hours')
plt.show()


# In[29]:


df['Age'].corr(df['WorkWeekHrs'])


# ### Bubble Plots
# 

# In[ ]:





# Create a bubble plot of `WorkWeekHrs` and `CodeRevHrs`, use `Age` column as bubble size.
# 

# In[14]:


# your code goes here

#bubble_size=df['Age']
plt.figure(figsize=(15, 15))
plt.scatter(df['WorkWeekHrs'],df['CodeRevHrs'],s=df['Age'],alpha=0.99)
plt.title('Bubble plot of workweek hours, codeRevHrs and age')
plt.show()


# ## Visualizing composition of data
# 

# ### Pie Charts
# 

# Create a pie chart of the top 5 databases that respondents wish to learn next year. Label the pie chart with database names. Display percentages of each database on the pie chart.
# 

# In[ ]:


# your code goes here


# ### Stacked Charts
# 

# Create a stacked chart of median `WorkWeekHrs` and `CodeRevHrs` for the age group 30 to 35.
# 

# In[ ]:


# your code goes here


# ## Visualizing comparison of data
# 

# ### Line Chart
# 

# Plot the median `ConvertedComp` for all ages from 45 to 60.
# 

# In[40]:


# your code goes here

QUERY = """
SELECT Age,ConvertedComp
FROM master
WHERE Age BETWEEN 45 AND 60
"""
df_ac = pd.read_sql_query(QUERY,conn)

df_gr=df_ac.groupby('Age').median()

df_gr.plot(kind='line')
plt.title('Median salary in 45-60 age group')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()


# ### Bar Chart
# 

# Create a horizontal bar chart using column `MainBranch.`
# 

# In[ ]:


# your code goes here


# Close the database connection.
# 

# In[ ]:


conn.close()


# ## Authors
# 

# Ramesh Sannareddy
# 

# In[49]:


import random

number_list = ['helen', 'Hailay', 'Gordon', 'fatemah', 'Elizabeth']

print(random.choice(number_list))


# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
# | ----------------- | ------- | ----------------- | ---------------------------------- |
# | 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |
# 

# Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2022-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
