def mensagem(msg):
    print('---------------')
    print(msg)
    print('---------------')

mensagem('Seu nome tem Silva?')
nome = input('Digite seu nome: ')
buscador = int(nome.find('Silva'))
if buscador != -1:
    print('Sim! Tem Silva!')
else:
    print('Me parece que não tem Silva')
mensagem('Fim do programa')