palavra= str(input("digite uma palavra:"))

if palavra == palavra[::-1]:#verificar se a palavra escrita é igual a palavra investida( usa-se o menos 1 para)
    print (f"palavra é palidroma:", '{palavra}')
else:
    print(f"palavra não é palidroma:", '{palavra}')

