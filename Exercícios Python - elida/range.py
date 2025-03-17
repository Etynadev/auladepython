for i in range (5):
    print("melhot cursinho...")


for i in range (5):
    print("TOP TREE")

contador = 1

while contador <= 6:
    print("Executando", contador, "vez")
    contador += 1


quantidadeImpares = 0

quantidadePares = 0

for i in range (5):
    numero = int(input("informe um numero: \n"))
    if numero % 2 == 0: # Numero é par
        quantidadePares +=1 
    else:
        quantidadePares +=1 
print(f"Quantidade de pares: {quantidadePares}")
print(f"Quantidade de impares: {quantidadeImpares}")

#Elida de Souza de Silva
#criamos 2 variáveis(0) utilizamos o for( LAÇO DE REPETIÇÃO) PARA O USUARIO REPETIR 5 VEZERS, para cada , o programa vai verificar se é impar ou par. se o numero é par é adicionado 1 a variavel quantidadepares, se ele n é par é adicionada 1 na quantidade impares. ao final é mostrado os valores.
