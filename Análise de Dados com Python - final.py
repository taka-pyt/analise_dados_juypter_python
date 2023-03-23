#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa do varejo e tem milhares de clientes diferentes.
# 
# Com o objetivo de aumentar o faturamento e o lucro da sua empresa, a diretoria quer conseguir identificar quem é o cliente ideal para seus produtos, baseado no histórico de compras dos clientes.
# 
# Para isso, ela fez um trabalho de classificar os clientes com uma nota de 1 a 100. Só que agora, sobrou para você conseguir, a partir dessa nota, descobrir qual o perfil de cliente ideal da empresa.
# 
# Qual a profissão? Qual a idade? Qual a faixa de renda? E todas as informações que você puder analisar para dizer qual o cliente ideal da empresa.
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=share_link

# In[ ]:


#logica do código

#1 - Importar base de dados dos clientes
#2 - Visualizar a base de dados
    ##2.1 - Entender as informações disponíveis
    ##2.2 - Procurar erros na base de dados
#3 - Tratamento da base de dados
#4 - Análise incial (nota dos clientes)
#5 - Análise completa (entender como cada caracteristica impacta na nota)


# In[5]:


#1 - Importar a base de dados
import pandas

tabela = pandas.read_csv("clientes.csv", encoding="latin", sep=";")

#2 - Visualizar a base de dados
##2.2 - Procurar erros na base de dados
###deletar coluna inutil
###axis = 0 se for linha e axis = 1 se for coluna
tabela = tabela.drop("Unnamed: 8", axis=1)
display(tabela)


# In[10]:


#3 - Tratamento da base de dados

## - acertar informações que estão sendo reconhecidas de forma errada
tabela["Salário Anual (R$)"] = pandas.to_numeric(tabela["Salário Anual (R$)"], errors ="coerce")

## - corrigir informações vazias
tabela = tabela.dropna()
print(tabela.info())
 

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    -


# In[12]:


#4 - Análise incial (nota dos clientes)
display(tabela.describe())


# In[19]:


## suposição - quanto maior o salário, maior a nota
## clientes de promoção são piores

import plotly.express as px

#cria gráfico

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)
    #exibe gráfico
    grafico.show()


# In[ ]:


#perfil ideal de cliente
##acima dos 15 anos (não ocorre muita variação entre faixas etárias depois desta faixa)
##faixa salaria não parece fazer tanta diferença
##pessoas que trabalham com entretenimento e artistas (construção é o pior)
##a faixa ideal é quem tem entre 10-15 anos de trabalho
##pessoas com famílias grandes não geram tanto resultado

