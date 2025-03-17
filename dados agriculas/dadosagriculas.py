import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_produtos =  pd.read_csv("analise.csv")
dados_produtos.columns = dados_produtos.columns.str.strip()
print(dados_produtos.head())


produtividade_media = dados_produtos.groupby("tipo_de_cultivo")["produtividade"].mean().reset_index()
print("\nProdutividade por Tipo de Cultivo:")
print(produtividade_media)

produto_max_produtividade = produtividade_media.loc[produtividade_media["produtividade"].idxmax()]
print("\nProdutividade com maior produtividade")
print(produto_max_produtividade)

uso_agua_medio = dados_produtos.groupby("tipo_de_cultivo")["uso_de_agua"].min()
produto_min_uso_agua = uso_agua_medio.idxmax()
print("\nProduto com menor uso médio de Agua:", produto_min_uso_agua)


plt.figure(figsize=(10, 6))

for prododuto in dados_produtos['tipos_de_cultivo'].unique():
    dados= dados[dados['tipos_de_cultivos'] == dados]
    plt.plot(dados['produtividade'], label=dados, marker='o')


plt.title('Produtividade ao longo dos anos por Tipo de Cultivo')
plt.xlabel('ano')
plt.ylabel('produtividade')
plt.legend(title="tipo de cultivo")

plt.grid(True)
plt.show
