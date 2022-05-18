import forca
import adivinhacao
import pedra_papel_tesoura

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print('(1) Forca / (2) Adivinhação / (3) Pedra, papel e tesoura')

    jogo = int(input('Qual jogo? '))

    if jogo == 1:
        print('Jogando Forca')
        forca.jogar()
    elif jogo == 2:
        print('Jogando Adivinhação')
        adivinhacao.jogar()
    elif jogo == 3:
        print('Jogando Pedra, papel e tesoura')
        pedra_papel_tesoura.jogar()

if __name__=='__main__':
    escolhe_jogo()