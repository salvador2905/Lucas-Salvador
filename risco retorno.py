#!/usr/bin/env python
# coding: utf-8

# #Trabalho de Data science - Lucas Salvador Santos Tavares - Matricula: 2121034
# 
#     A ideia desse codigo é você fazer o Risco Retorno de um portifolio de ações registradas na B3, é você conseguir analisar o quanto um ativo teve de retorno e quanto risco você correu para com a volatilidade presente nesse ativo.
#     
#     Primeiramente importamos as bibliotecas, pandas, numpy, seaborn, yfinance, matplotlib para montar todo o cogido. Posteriormente definimos o nosso "portifolio de ativos" como "ativos" fazendo uma lista com as ações que eu quero pro estudo
#    
#     Após isso eu defini a data que será feita o estudo. Após isso eu testo para ver se consigo puxar as informações do ativo no yfinance. Faço o download de todo o historico dos ativos. 
#     
#     Com isso primeiro testamos para ver se está funcionando a compilação da lista e o grafico feito pelo matplotib, primeiro vemos a volatilidade dos ativos através de seus desvios padrões e após isso vemos o quanto de retorno que eles trouxeram nos 9 anos colocados na data do estudo 
#     
#     Fizemos um grafico de dispersão com os retornos e volatilidades mas o problema é que não mostrava quem era quem. Com isso tive que integrar o nome de cada ativo com o seu respectivo local no grafico, aumentei o tamanho do grafico e VUALA.
#     
#     
#     

# In[35]:


#!pip install yfinance


# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import yfinance as yf
import matplotlib.pyplot as plt


# In[3]:


# obtendo os dados das ações


# In[4]:


ativos = ['ABEV3.SA', 'MYPK3.SA', 'RADL3.SA', 'EGIE3.SA', 'TAEE11.SA', 'PETR4.SA', 'VALE3.SA', 'SUZB3.SA', 'WEGE3.SA', 'TAEE3.SA', 'BBDC3.SA', 'CYRE3.SA', 'ETER3.SA', 'FLRY3.SA', 'SIMH3.SA']


# In[5]:


inicio = '2014-08-01'
fim = '2022-09-01'


# In[6]:


yf.download('ETER3.SA', start = inicio, end = fim)['Adj Close']


# In[7]:


df = pd.DataFrame()


# In[8]:


for ativo in ativos:
  df[ativo] = yf.download(ativo, start = inicio, end = fim)['Adj Close']


# In[9]:


df.head();


# In[10]:


df.plot();


# In[11]:


df.plot(figsize = (10, 10));


# In[12]:


figsize = (10, 10)


# In[13]:


normalizado = df/df.iloc[0]


# In[14]:


normalizado.head()


# In[15]:


normalizado.plot();


# In[16]:


normalizado.plot(figsize = (10, 10));


# In[17]:


retornos_diarios = df.pct_change()


# In[18]:


retornos_diarios.head()


# In[19]:


retornos_diarios.dropna()


# In[20]:


retornos_diarios = retornos_diarios.dropna()


# In[21]:


# dataframe risco retorno


# In[22]:


retornos_diarios.std()


# In[23]:


volatilidade = pd.DataFrame(retornos_diarios.std(), columns=['Vol'])


# In[24]:


retornos_medios = pd.DataFrame(retornos_diarios.mean(), columns=['Retornos'])


# In[25]:


volatilidade


# In[26]:


retornos_medios


# In[27]:


risco_retorno = pd.concat([retornos_medios, volatilidade], axis = 1)


# In[28]:


risco_retorno


# In[29]:


# plotando Gráfico risco retorno 


# In[30]:


sns.scatterplot(data = risco_retorno, x = 'Vol', y = 'Retornos');


# In[31]:


risco_retorno.shape[0]


# In[32]:


range(risco_retorno.shape[0])


# In[33]:


risco_retorno.index


# In[34]:



plt.subplots(figsize = (10, 10))

sns.scatterplot(data=risco_retorno, x = 'Vol', y='Retornos')


for i in range(risco_retorno.shape[0]):
    plt.text(x = risco_retorno.Vol[i], y = risco_retorno.Retornos[i], s = risco_retorno.index[i],
            fontdict = dict(color = 'red', size = 15),
            bbox = dict(facecolor = 'yellow'))


# In[ ]:





# In[ ]:




