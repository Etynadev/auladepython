
import time
import random #seleciona de forma aleatotia elementos de alguma lista
contatos = [
        "jose", "ana", "pedro",
        "julia", "maria", "fabiana"
    ]
escolher = random.choice(contatos)
print(f" contato escolhido: {escolher}") 
def mensagem(intervalo_minutos=10):
    contador = 1
    while True: #laço de repetição, é executado enquanto a açaõ for verdaeira
        print(F"\n voçê é especial amigo!(mensagem{contador})")
        contador += 1
        time.sleep(intervalo_minutos*60)

        mensagem()
        
