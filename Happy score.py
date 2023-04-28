#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


happy=pd.read_csv("C:\\Users\\Super\\Downloads\\happyscore_income.csv",index_col="country")


# In[5]:


happy


# In[6]:


happy.plot.scatter("avg_income","happyScore")
plt.grid()


# In[ ]:





# In[7]:





# In[ ]:





# In[ ]:





# In[ ]:




