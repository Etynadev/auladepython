import pandas as pd
import matplotlib.pyplot as plt

dados_produtos = pd.read_csv('analise.csv', delimiter=',')

plt.figure(figsize=(10,6))

for prododuto in dados_produtos['produto'].unique():
    dados_produtos= dados_produtos[dados_produtos['produto'] == produto]
    plt.plot(dados_produtos['ano'], label=produto, marker='o')

plt.title('Preço dos produtos ao longo dos anos')
plt.xlabel('ano')
plt.ylabel('preço')
plt.legend(title="produto")

plt.grid(True)
plt.show  