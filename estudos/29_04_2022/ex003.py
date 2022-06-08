from posixpath import split


nomeCompleto = input('Digite seu nome completo: ')
nomeCortado = nomeCompleto.split()
nomePrimeiro = nomeCortado[0]
ultimoIndice = int(len(nomeCortado)) - 1
nomeUltimo = nomeCortado[ultimoIndice]
print('Primeiro nome: ', nomePrimeiro)
print('Ultimo nome:', nomeUltimo)