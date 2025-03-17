"""produto = {
    'Nome': 'feijão',
    'Quantidade': 10
}


nome = produto['Nome']
quantidade = produto['Quantidade']
print ("Nome : ", nome)
print ('Quantidade : ',  quantidade)

#Elida de Souza e Silva .Estruturas mais complexas, elementos separados por vírgula.

#alterando on valor
produto = {
    'Nome': 'feijão',
    'Quantidade': 10
}

produto['Quantidade'] = 10

nome = produto['Nome']
quantidade = produto['Quantidade']

print("Nome :", nome)
print('Quantidade:', quantidade)

#percorrendo nosso dicionario
produto = {
    'Nome': 'feijão',
    'Quantidade': 10
}
for chave, valor in produto.items() :
    print(chave, valor) 

    #avançando no dicionario
    produto = {
    'Nome': ['feijão', 'Arroz', 'Farinha'],
    'Quantidade': [10, 10, 100]
}
    
for chave, valor in produto.items():
    print(chave, valor)

    #Função zip(CHAMAR OS ELEMENTOS DO DICIONARIO)
    produto = {
    'Nome': ['feijão', 'Arroz', 'Farinha'],
    'Quantidade': [10, 10, 100]
    }

    for nome, quantidade in zip (produto['Nome'], produto['Quantidade']) :
        print("Produto:", nome, "Quantidade:", quantidade)
"""""
produto = {
    'Nome': ['feijão', 'Arroz', 'Farinha'],
    'quantidade': [10, 10, 100], 'preço': [15, 6, 10]}

for nome, quantidade, preço, in zip (produto['Nome'], produto['quantidade'], produto['preço']):
        print("produto:", nome, "Quantidade", quantidade, "preço", preço)

    #CONJUNTO
numeros = [1, 2, 3, 3]
conjunto = set(numeros)

print(conjunto)

#Elida de Souza e Silva