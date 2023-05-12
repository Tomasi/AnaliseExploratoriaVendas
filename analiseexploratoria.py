# -*- coding: utf-8 -*-
"""AnaliseExploratoria.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AZZVksyv8aj2gO-aI4oTTWHUewUxJJHx
"""

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Gerando dados sintéticos
np.random.seed(0)

sul_vendas = np.random.uniform(1000.0, 5000.0, size=100).round(2)
nordeste_vendas = np.random.uniform(500.0, 3000.0, size=100).round(2)
norte_vendas = np.random.uniform(200.0, 2000.0, size=100).round(2)
sudeste_vendas = np.random.uniform(1500.0, 6000.0, size=100).round(2)
centro_oeste_vendas = np.random.uniform(800.0, 4000.0, size=100).round(2)

df = pd.DataFrame({
    'Região': ['Sul'] * 100 + ['Nordeste'] * 100 + ['Norte'] * 100 + ['Sudeste'] * 100 + ['Centro-Oeste'] * 100,
    'Vendas': np.concatenate([sul_vendas, nordeste_vendas, norte_vendas, sudeste_vendas, centro_oeste_vendas])
})

df['Produto'] = ['Produto A', 'Produto B', 'Produto C', 'Produto D'] * 125
df['Custo'] = np.random.uniform(50.0, 200.0, size=500).round(2)
df['Vlr.Venda'] = np.random.uniform(220.0, 400.0, size=500).round(2)
df['Total'] = df.groupby('Região')['Vendas'].transform('sum')
df['Data'] = [f"{random.randint(1, 28):02d}/{random.randint(1, 12):02d}/{random.randint(2019, 2022)}" for _ in range(df.shape[0])]
outras_empresas = ['Empresa X', 'Empresa Y', 'Empresa Z']
df['Empresa'] = np.where(df['Região'] == 'Sul', 'FabProdresponsável', np.random.choice(outras_empresas, size=df.shape[0]))

# Reorganizando a ordem das colunas
df = df[['Data', 'Região', 'Empresa', 'Produto', 'Custo', 'Vendas', 'Vlr.Venda', 'Total']]
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y') 
df = df.sort_values('Data')

# Exportar o DataFrame para um arquivo Excel
df.to_excel('dados_vendas.xlsx', index=False)

"""# Análise Estatística Descritiva"""

df = pd.read_excel('dados_vendas.xlsx')
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

# Estatísticas descritivas das vendas por região (Quantidade de Vendas)
stats_vendas_por_regiao = df.groupby('Região')['Vendas'].describe()
print(stats_vendas_por_regiao)

# Estatísticas descritivas das vendas por região (Valor de Venda)
stats_valor_por_regiao = df.groupby('Região')['Vlr.Venda'].describe()
print(stats_valor_por_regiao)

# Estatísticas descritivas das vendas ao longo do tempo (Quantidade de Vendas)
stats_vendas_por_data = df.groupby(df['Data'].dt.to_period('M'))['Vendas'].describe()
print(stats_vendas_por_data)

# Estatísticas descritivas das vendas ao longo do tempo (Valor de Venda)
stats_valor_por_data = df.groupby(df['Data'].dt.to_period('M'))['Vlr.Venda'].describe()
print(stats_valor_por_data)

# Gráfico de barras das vendas por região (Quantidade de Vendas)
plt.figure(figsize=(10, 6))
df.groupby('Região')['Vendas'].mean().plot(kind='bar')
plt.xlabel('Região')
plt.ylabel('Média de Vendas')
plt.title('Média de Vendas por Região (Quantidade de Vendas)')
plt.show()

# Gráfico de linhas das vendas ao longo do tempo (Valor de Venda)
plt.figure(figsize=(10, 6))
df.groupby(df['Data'].dt.to_period('M'))['Vlr.Venda'].mean().plot()
plt.xlabel('Data')
plt.ylabel('Média de Vendas')
plt.title('Média de Vendas ao Longo do Tempo (Valor de Venda)')
plt.xticks(rotation=45)
plt.show()

# Histograma dos valores de venda
plt.figure(figsize=(10, 6))
plt.hist(df['Vlr.Venda'], bins=10, edgecolor='black')
plt.xlabel('Valor de Venda')
plt.ylabel('Frequência')
plt.title('Distribuição dos Valores de Venda')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Região', y='Vlr.Venda', data=df)
plt.xlabel('Região')
plt.ylabel('Valor de Venda')
plt.title('Distribuição dos Valores de Venda por Região')
plt.show()

plt.figure(figsize=(8, 8))
df.groupby('Produto')['Vendas'].sum().plot(kind='pie', autopct='%1.1f%%', shadow=True)
plt.ylabel('')
plt.title('Participação de cada Produto nas Vendas Totais')
plt.legend(loc='best')
plt.show()

"""# Modelo Preditivo"""

X = df[['Região', 'Vlr.Venda']]
y = df['Vendas']

X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Avaliar o desempenho do modelo
mse = mean_squared_error(y_test, y_pred)
print('Erro quadrático médio (MSE):', mse)

import matplotlib.pyplot as plt

# Plotar o gráfico de dispersão
plt.scatter(X_test['Vlr.Venda'], y_test, color='blue', label='Dados Reais')

# Plotar a linha da regressão linear
plt.plot(X_test['Vlr.Venda'], y_pred, color='red', linewidth=2, label='Regressão Linear')

# Configurar o gráfico
plt.xlabel('Valor de Venda')
plt.ylabel('Vendas')
plt.title('Regressão Linear - Valor de Venda vs. Vendas')
plt.legend()

# Mostrar o gráfico
plt.show()
