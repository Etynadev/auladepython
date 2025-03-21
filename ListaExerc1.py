import pandas as pd
from plyer import notification

dados_produtos = pd.read_csv("Lista Exerc..csv")
dados_produtos.columns = dados_produtos.columns.str.strip()
print(dados_produtos.head())



# 3. Calculando o total vendido por produto
dados_produtos["Total"] = dados_produtos["Quantidade"] *dados_produtos["Preço"]
total_vendas = dados_produtos.groupby("Produto")["Total"].sum()
print(total_vendas)

# 4. Identificando o produto mais vendido
produto_mais_vendido = total_vendas.idxmax()
valor_mais_vendido = total_vendas.max()
print("\nProduto_mais_vendido")
print(produto_mais_vendido)

# 5. Exibindo o relatório
print("\n Relatório de Vendas:")
print(total_vendas)
print(f"\n Produto mais vendido: {produto_mais_vendido} (Total: R$ {valor_mais_vendido:.2f})")

# 4. Calculando o total geral das vendas
total_geral_vendas = total_vendas.sum()
print(f"\n total geral de vendas:")
print(total_geral_vendas)

# 5. Criando a notificação
mensagem = (
    f"Produto mais vendido: {produto_mais_vendido} (R$ {valor_mais_vendido:.2f})\n"
    f"Total geral de vendas: R$ {total_geral_vendas:.2f}"
)

notification.notify(
    title="Resumo das Vendas",
    message=mensagem,
    app_name="Sistema de Vendas",
    timeout=10  
)
print("Notificação enviada com sucesso!")

 
