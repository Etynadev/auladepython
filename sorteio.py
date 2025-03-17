import random

def sorteio_aluno():
    alunos = [
        "jose", "ana", "pedro",
        "julia", "maria", "fabiana"
    ]
    escolher = random.choice(alunos)
    print(f" o aluno escolhido foi: {escolher}")

sorteio_aluno()

#sorteio com numeros

import random

def sorteio_numeros():
    numeros = [
        "2", "3", "6",
        "8", "7", "11"
    ]
    escolher = random.choice(numeros)
    print(f" o numero escolhido foi: {escolher}")

sorteio_numeros()

