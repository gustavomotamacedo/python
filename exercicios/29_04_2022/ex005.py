numero = input('Digite um número entre 0 e 9999: ')
while int(numero) <= 0 or int(numero) > 9999:
    numero = input('Por favor digite outro valor: ')
tamanho = len(numero)
numero = numero[::-1]
for i in range(tamanho):
    match i:
        case 0:
            print('Unidades:', numero[i])
        case 1:
            print('Dezenas:', numero[i])
        case 2:
            print('Centenas:', numero[i])
        case 3:
            print('Milhares:', numero[i])
