nomeCidade = input('Digite o nome da cidade: ')
procurador = int(nomeCidade.find('Santo'))
if procurador != 0 and procurador != -1:
    print('Me parece que o nome da cidade tem Santo, mas não começa com Santo')
elif procurador == 0:
    print('O nome desta cidade começa com Santo')
else:
    print('Essa cidade nem ao menos tem Santo no nome')