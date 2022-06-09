#binario para decimal
dec = 0
strBinario = input('Digite um valor em binários:\n')
for i in range(len(strBinario)):
    numero = int(strBinario[i]) * 2**i
    dec += numero
print(dec)