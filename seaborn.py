#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
df=sns.load_dataset('iris')
df.head()


# In[9]:


df.corr()


# In[4]:


sns.heatmap(df.corr(),vmin=0,annot=True,center=0)


# In[8]:


sns.jointplot(x='petal_length',y='sepal_length',data=df,kind='hex')


# In[33]:


sns.jointplot(x='sepal_width',y='petal_width',data=df,kind='reg')


# In[41]:


sns.pairplot(df)


# In[42]:


sns.pairplot(df,hue='species',palette=None,height=3)


# In[45]:


sns.distplot(df['petal_length'])


# In[6]:


sns.distplot(df['sepal_length'],kde=False,bins=20)


# In[18]:


sns.countplot('petal_width',data=df)


# In[24]:


sns.barplot(x='sepal_length',y='sepal_width',data=df,palette='rainbow')


# In[25]:


sns.boxplot('sepal_length','petal_length',data=df)


# In[29]:


sns.boxplot(data=df,orient='v')


# In[32]:


sns.violinplot(data=df,orient='v',palette='rainbow')


# In[37]:


df1=sns.load_dataset('titanic')
df1.head()


# In[42]:


sns.boxplot(data=df1,x='survived',y='fare',hue='sex')

