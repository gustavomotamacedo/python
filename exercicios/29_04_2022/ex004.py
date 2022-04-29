frase = input('Digite uma frase qualquer:\n')
fraseMaiuscula = frase.upper()
contadorA = fraseMaiuscula.count('A')
print(f'A letra "a" aparece {contadorA} vezes')
primeiroA = int(fraseMaiuscula.find('A')) + 1
print(f'A primeira letra "a" aparece na posição {primeiroA}')
ultimoA = int(fraseMaiuscula.rfind('A')) + 1
print(f'A ultima letra "a" aparece na posição {ultimoA}')
