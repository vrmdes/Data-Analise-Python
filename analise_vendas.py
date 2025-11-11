import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../data/vendas.csv')
print(df.head())
df.groupby('Produto')['Valor'].sum().plot(kind='bar')
plt.title('Vendas por Produto (Exemplo)')
plt.show()
