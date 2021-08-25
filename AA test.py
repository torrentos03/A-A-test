#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd
import seaborn as sns
import numpy as np
import scipy.stats as st
import statsmodels.stats.multicomp as sm
from scipy.stats import norm, mannwhitneyu
import matplotlib.pyplot as plt
from tqdm.auto import tqdm
plt.style.use('ggplot')
df = pd.read_csv('https://stepik.org/media/attachments/lesson/396012/hw_aa.csv', sep =';')
df


# In[92]:


sg = df.groupby(['experimentVariant', 'version'],as_index= False).agg({'purchase' : 'sum', 'uid' : 'count'})
sg['conv'] = round(sg['purchase'] / sg['uid'] * 100, 2)
sg


# In[45]:


df.shape[0]
df.dtypes


# In[60]:


var = df.query("experimentVariant == 1")
var1 = df.query("experimentVariant == 0")
var1


# In[ ]:





# In[ ]:





# In[133]:


n = df.shape[0]
simulations = 1000
n_s = 1000
res = []

# Запуск симуляций A/A теста
for i in tqdm(range(simulations)):
    s1 = var.purchase.sample(n_s, replace = False).values
    s2 = var1.purchase.sample(n_s, replace = False).values
    res.append(st.ttest_ind(s1, s2, equal_var = False)[1]) # сохраняем pvalue

plt.hist(res, bins = 50)
plt.style.use('ggplot')
plt.xlabel('pvalues')
plt.ylabel('frequency')
plt.title("Histogram of ttest A/A simulations ")
plt.show()

# Проверяем, что количество ложноположительных случаев не превышает альфа
sum(np.array(res) <0.05) / simulations


# In[65]:


ver = df.query("version == 'v2.8.0'" and "experimentVariant == 1" )
ver1 = df.query("version == 'v2.9.0'" and "experimentVariant == 1")


# In[66]:


n = df.shape[0]
simulations = 1000
n_s = 1000
res = []

# Запуск симуляций A/A теста
for i in tqdm(range(simulations)):
    s1 = ver.purchase.sample(n_s, replace = False).values
    s2 = ver.purchase.sample(n_s, replace = False).values
    res.append(st.ttest_ind(s1, s2, equal_var = False)[1]) # сохраняем pvalue

plt.hist(res, bins = 50)
plt.style.use('ggplot')
plt.xlabel('pvalues')
plt.ylabel('frequency')
plt.title("Histogram of ttest A/A simulations ")
plt.show()

# Проверяем, что количество ложноположительных случаев не превышает альфа
sum(np.array(res) <0.05) / simulations


# In[67]:


fas = df.query("version == 'v2.8.0'" and "experimentVariant == 0" )
fas1 = df.query("version == 'v2.9.0'" and "experimentVariant == 0")


# In[68]:


n = df.shape[0]
simulations = 1000
n_s = 1000
res = []

# Запуск симуляций A/A теста
for i in tqdm(range(simulations)):
    s1 = fas.purchase.sample(n_s, replace = False).values
    s2 = fas1.purchase.sample(n_s, replace = False).values
    res.append(st.ttest_ind(s1, s2, equal_var = False)[1]) # сохраняем pvalue

plt.hist(res, bins = 50)
plt.style.use('ggplot')
plt.xlabel('pvalues')
plt.ylabel('frequency')
plt.title("Histogram of ttest A/A simulations ")
plt.show()

# Проверяем, что количество ложноположительных случаев не превышает альфа
sum(np.array(res) <0.05) / simulations


# In[70]:


nul = df.query("version == 'v2.8.0'" and "experimentVariant == 1" )
nul1 = df.query("version == 'v2.8.0'" and "experimentVariant == 0")


# In[71]:


n = df.shape[0]
simulations = 1000
n_s = 1000
res = []

# Запуск симуляций A/A теста
for i in tqdm(range(simulations)):
    s1 = nul.purchase.sample(n_s, replace = False).values
    s2 = nul1.purchase.sample(n_s, replace = False).values
    res.append(st.ttest_ind(s1, s2, equal_var = False)[1]) # сохраняем pvalue

plt.hist(res, bins = 50)
plt.style.use('ggplot')
plt.xlabel('pvalues')
plt.ylabel('frequency')
plt.title("Histogram of ttest A/A simulations ")
plt.show()

# Проверяем, что количество ложноположительных случаев не превышает альфа
sum(np.array(res) <0.05) / simulations


# In[74]:


mol = df.query("version == 'v2.9.0'" and "experimentVariant == 1" )
mol1 = df.query("version == 'v2.9.0'" and "experimentVariant == 0")


# In[75]:


n = df.shape[0]
simulations = 1000
n_s = 1000
res = []

# Запуск симуляций A/A теста
for i in tqdm(range(simulations)):
    s1 = mol.purchase.sample(n_s, replace = False).values
    s2 = mol1.purchase.sample(n_s, replace = False).values
    res.append(st.ttest_ind(s1, s2, equal_var = False)[1]) # сохраняем pvalue

plt.hist(res, bins = 50)
plt.style.use('ggplot')
plt.xlabel('pvalues')
plt.ylabel('frequency')
plt.title("Histogram of ttest A/A simulations ")
plt.show()

# Проверяем, что количество ложноположительных случаев не превышает альфа
sum(np.array(res) <0.05) / simulations


# In[129]:


sb = df.query("version != 'v2.8.0'").reset_index()
sb


# In[130]:


sv = sb.groupby(['experimentVariant', 'version'],as_index= False).agg({'purchase' : 'sum', 'uid' : 'count'})
sv['conv'] = round(sv['purchase'] / sv['uid'] * 100, 2)
sv


# In[131]:


vas = sb.query("experimentVariant == 1")
vas1 = sb.query("experimentVariant == 0")


# In[132]:


n = df.shape[0]
simulations = 1000
n_s = 1000
res = []

# Запуск симуляций A/A теста
for i in tqdm(range(simulations)):
    s1 = vas.purchase.sample(n_s, replace = False).values
    s2 = vas1.purchase.sample(n_s, replace = False).values
    res.append(st.ttest_ind(s1, s2, equal_var = False)[1]) # сохраняем pvalue

plt.hist(res, bins = 50)
plt.style.use('ggplot')
plt.xlabel('pvalues')
plt.ylabel('frequency')
plt.title("Histogram of ttest A/A simulations ")
plt.show()

# Проверяем, что количество ложноположительных случаев не превышает альфа
sum(np.array(res) <0.05) / simulations


# In[ ]:


Проведя A-A тест по всем данным, мы получили значение, которое > значения a.
Из этого делаем вывод что где-то имеется ошибка. После этого сгруппуруем данные
по версси и тесту и вычисляем процент конверсии

