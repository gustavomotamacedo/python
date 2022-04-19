c = 0
fim = int(input('Digite a quantidade de alunos:\t'))
soma = 0
c = 1
while c <= fim:
    nota = float(input('Digite a nota do aluno {}: ' .format(c)))
    soma += nota
    c += 1
alunos = c -1
media = soma / alunos
print('A media da nota {} dos {} alunos é de {} pontos.' .format(soma, alunos, media))
    