usuario = input('input username: ')
objeto_arquivo = open('usuario.txt', 'a')
objeto_arquivo.write('\n')
objeto_arquivo.write(usuario)