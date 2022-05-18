from random import randint
print('Bem vindo ao jogo de adivinhação!')
computador = randint(0, 10)
tentativas = 0
cont_tentativas = 0

nivel_dif = int(input('Escolha o nível de dificuldade:\n'
                      '[1] Fácil\n'
                      '[2] Médio\n'
                      '[3] Dificil\n'))

if nivel_dif == 1:
    print('Nível Fácil!')
    print('Você precisa adivinhar um número de 0 a 10! Acha que consegue?')
    print('VAMOS COMEÇAR!!!')
    while True:
        jogada = int(input('Digite seu palpite: '))
        tentativas += 1
        print(f'Tentativa {tentativas} de 3')
        if jogada < 0 or jogada > 10:
            print('Jogada inválida! Apenas números de 0 a 10!')
        else:
            if jogada > computador:
                print('ERRRRROU!!! Seu número é maior, tente novamente')
                if tentativas == 3:
                    break
            elif jogada < computador:
                print('ERRRRROU!!! Seu número é menor, tente novamente')
                if tentativas == 3:
                    break
            elif jogada == computador:
                if tentativas == 3:
                    break
                print(f'PARABÉNS!!!! você adivinhou o número! seu número foi {jogada} e o computador jogou {computador}')

if nivel_dif == 2:
    print('Nível Médio')
    print('Você precisa adivinhar um número de 0 a 50! Acha que consegue?')
    print('VAMOS COMEÇAR!!!')
    while True:
        jogada = int(input('Digite seu palpite: '))
        tentativas += 1
        print(f'Tentativa {tentativas} de 3')
        if jogada < 0 or jogada > 50:
            print('Jogada inválida! Apenas números de 0 a 50!')
        else:
            if jogada > computador:
                print('ERRRRROU!!! Seu número é maior, tente novamente')
                if tentativas == 3:
                    break
            elif jogada < computador:
                print('ERRRRROU!!! Seu número é menor, tente novamente')
                if tentativas == 3:
                    break
            elif jogada == computador:
                print(f'PARABÉNS!!!! você adivinhou o número! seu número foi {jogada} e o computador jogou {computador} ')
                if tentativas == 3:
                    break

if nivel_dif == 3:
    print('Nível Dificil')
    print('Você precisa adivinhar um número de 0 a 100! Acha que consegue?')
    print('VAMOS COMEÇAR!!!')
    while True:
        jogada = int(input('Digite seu palpite: '))
        tentativas += 1
        print(f'Tentativa {tentativas} de 3')
        if jogada < 0 or jogada > 100:
            print('Jogada inválida! Apenas números de 0 a 100!')
        else:
            if jogada > computador:
                print('ERRRRROU!!! Seu número é maior, tente novamente')
                if tentativas == 3:
                    break
            elif jogada < computador:
                print('ERRRRROU!!! Seu número é menor, tente novamente')
                if tentativas == 3:
                    break
            elif jogada == computador:
                print(f'PARABÉNS!!!! você adivinhou o número! seu número foi {jogada} e o computador jogou {computador}\n')
                if tentativas == 3:
                    break

print('Fim de jogo!')