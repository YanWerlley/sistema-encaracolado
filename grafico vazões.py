#!/usr/bin/env python
# coding: utf-8

# In[5]:


# importando bibliotecas!!
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import datetime

# pegando os dados e colocando data!
ti = '1998-01-01'
tf = '2009-12-31'
df = pd.read_csv('C:/Users/Desktop/APC TRAB/data/MGB-IPH_DischargeData_AmazonBasin.txt', delimiter="\s+",engine='python',header=None)
date = pd.date_range(start=ti, end=tf, freq='D')
df['date'] = date;
df.set_index('date', inplace=True)
# df.tail()


# In[31]:


# colocando na var intervalo o range para não escrever todos ex y[1,2,3,4,5,6,7,8]
intervalo = [x+1 for x in range(0,2)]

# plootando o grafico
fig = px.line(df, x=date, y=intervalo)

# titulo e essa linha que mostrar os dados so de passar na região
fig.update_layout(hovermode='x unified', title_text='Vazões do(s) rio(s)', title_x=0.5)
fig.show()
# !!!!!!!!!!!falta arrumar legenda e deixar bonito e no futoro adicionar o valor do rio que o usuario clicar!!!!!!!!!!!!


# In[ ]:




