def borda(s1):
    tam = len(s1)
    if tam:
        print('+', '-' *tam, '+')
        print('!', 'Elida de Souza e Silva', '!')
        print('+','-' *tam, '+')
    print('Olá seja bem vindo(a) a lojinha de makes da')
    borda('Elida de Souza e Silva')
    print('Pomoção de Bases Mari Maria!!! \n')
    #criaçãodevariavéis
    valor = float(input('insira o valor da Base:'))
    quantidade = int(input('insira a quantidade de Bases:'))
    #condição para ops descontos
    if quantidade < 10:
        desconto = 0
    elif quantidade < 20:
        desconto = 0.1
    else:
        desconto = 0.2
    #parametros para os valores
    valor_sem_desconto = quantidade * valor
    valor_com_desconto = quantidade * (1 - desconto)
    valor_total = quantidade * valor_com_desconto
    valor_desconto = quantidade * valor * desconto
    porcentagem_desconto = desconto * 80
    #saída dos dados
    print(f'valor total sem desconto: ', valor_sem_desconto)
    print(f'valor unitário:R$ {valor:.2f}')
    print(f'valor com desconto: R$ {valor_total:.2f} ({porcentagem_desconto:.0f}% de desconto)')
    print(f'valor total: R${valor_total:.2f}(desconto total: R$ {valor_desconto:.2f})')