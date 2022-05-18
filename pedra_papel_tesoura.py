import random

def jogar():
    imprime_abertura()
    jogada_computador = random.randint(0, 2)
    jogada = int(input('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Sua jogada é...: '''))

    print('-' * 20)
    print('Sua jogada')

    if jogada == 0:
        print('PEDRA')
    elif jogada == 1:
        print('PAPEL')
    elif jogada == 2:
        print('TESOURA')

    print('-' * 20)
    print('Jogada do computador')

    if jogada_computador == 0:
        print('PEDRA')
    elif jogada_computador == 1:
        print('PAPEL')
    elif jogada_computador == 2:
        print('TESOURA')

    print('-' * 20)
    jogada_pedra(jogada, jogada_computador)
    jogada_papel(jogada, jogada_computador)
    jogada_tesoura(jogada, jogada_computador)

def imprime_abertura():
    print("*********************************")
    print("*****PEDRA, PAPEL E TESOURA!*****")
    print("*********************************")

def jogada_pedra(jogada, jogada_computador):
    if jogada_computador == 0:
        if jogada == 0: #pedra
            print('EMPATE')
        elif jogada == 1: #papel
            print('Você ganhou!')
        elif jogada == 2: #tesoura
            print('Você perdeu.')

def jogada_papel(jogada, jogada_computador):
    if jogada_computador == 1:
        if jogada == 1: #papel
            print('EMPATE')
        elif jogada == 2: #tesoura
            print('Você ganhou!')
        elif jogada == 0: #pedra
            print('Você perdeu.')

def jogada_tesoura(jogada, jogada_computador):
    if jogada_computador == 2:
        if jogada == 2: #tesoura
            print('EMPATE')
        elif jogada == 0: #pedra
            print('Você ganhou!')
        elif jogada == 1: #papel
            print('Você perdeu.')

if __name__=='__main__':
    jogar()