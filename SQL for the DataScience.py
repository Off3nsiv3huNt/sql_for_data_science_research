#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install sqlalchemy')
get_ipython().system('pip install pymysql')


# In[2]:


from sqlalchemy import create_engine
import pandas as pd


# In[3]:


db_host = '18.13.56.18:3306'
username = 'Black_hawk'
user_pass = 'black_hawk%202023#'
db_name = 'blackhawk_sql'


# In[4]:


conn = create_engine('mysql+pymysql://'+username+':'+user_pass+'@'+db_host+'/'+db_name)
conn.table_names()


# In[ ]:


query = 'select * from orders'
orders = pd.read_sql(query,conn)
print(orders.shape)


# In[ ]:




