import pandas as pd
import plotly.express as px

tabela = pd.read_csv(r'telecom_users.csv')

tabela = tabela.drop('Unnamed: 0', axis=1)

tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

tabela = tabela.dropna(how='all', axis=1)
tabela = tabela.dropna(how='any', axis=0)

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn', text_auto=True)
    grafico.show()
