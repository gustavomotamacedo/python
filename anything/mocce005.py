import pyautogui as pa
import random as rand
import pygame as pg
menu = pa.confirm('CLIQUE EM "INICIAR" PARA COMEÇAR', 'MENU', ['INICIAR', 'FECHAR'])
if menu == 'INICIAR':
    game = True
    pg.init()
    pg.mixer.music.load('prince_ali_copy.mp3')
    pg.mixer.music.play(fade_ms=1000)
    dif = 500
    vitorias = 0
    print(vitorias)
    derotas = 0
    print(derotas)
    maior = 0
    print(maior)
    pos = int((rand.random() * 9) + 1)
    print(pos)
    pa.alert("""O jogo funciona da seguinte maneira:
             Rapidamente será mostrada a posicao da bolinha;
             Voce devera acertar onde ela está em seguida, clicando na sua posicao
             Caso acerte voce ganhara 1 ponto e depois de uma certa quantidade de pontos a velocidade ira aumentar
             Caso voce perca sua pontuacao e zerada
             Caso voce perca 3 vezes sua velocidade e reiniciada""", 'Regras', timeout=5000)
else:
    game = False
while game == True:
    pa.alert('Escolha onde está escondida a bolinha', f'Pontos = {vitorias}', 'Ok', timeout=1500)
    match pos:
        case 1:
            bolinha = pa.confirm(title=f'Pontos = {vitorias}', buttons=['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ], timeout=dif)
        case 2:
            bolinha = pa.confirm(title=f'Pontos = {vitorias}', buttons=[' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ], timeout=dif)
        case 3:
            bolinha = pa.confirm(title=f'Pontos = {vitorias}', buttons=[' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ], timeout=dif)
        case 4:
            bolinha = pa.confirm(title=f'Pontos = {vitorias}', buttons=[' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ], timeout=dif)
        case 5:
            bolinha = pa.confirm(title=f'Pontos = {vitorias}', buttons=[' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ], timeout=dif)
        case 6:
            bolinha = pa.confirm(title=f'Pontos = {vitorias}', buttons=[' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ], timeout=dif)
        case 7:
            bolinha = pa.confirm(title=f'Pontos = {vitorias}', buttons=[' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ], timeout=dif)
        case 8:
            bolinha = pa.confirm(title=f'Pontos = {vitorias}', buttons=[' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', ], timeout=dif)
        case 9:
            bolinha = pa.confirm(title=f'Pontos = {vitorias}', buttons=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ], timeout=dif)
    bolinha = pa.confirm(title=f'Pontos = {vitorias}', buttons=['1', '2', '3', '4', '5', '6', '7', '8', '9', ])
    if bolinha != str(pos):
        if vitorias >= maior:
            maior = vitorias
            print(maior)
        vitorias = 0
        print(vitorias)
        menu = pa.confirm('Você errou, consegue continuar?', 'Encontre a bolinha', buttons=['Sim', 'Nao'])
        if menu != 'Sim':
            pa.alert(f'Sua maior pontuacao foi {maior}, e voce perdeu {derotas} vezes', 'Fim', 'Ok, adeus')
            break 
        else: 
            derotas += 1
            print(derotas)
            dif = 500
    else:
        vitorias += 1
        if vitorias >= maior:
            maior = vitorias
            print(maior)
        pa.alert('Boa!', f'Pontos = {vitorias}', timeout=500)
        pa.alert('Você acertou!', f'Pontos = {vitorias}', timeout=500)
        menu = pa.confirm('Quer continuar?', f'Pontos = {vitorias}', buttons=['Sim', 'Nao'])
        if menu != 'Sim':
            pa.alert(f'Sua maior pontuacao foi {maior}, e voce perdeu {derotas} vezes', 'Fim', 'Ok, adeus')
            break
        else:  
            pos = int((rand.random() * 9) + 1)
            match vitorias:
                case 3:
                    dif = 250
                case 5:
                    dif = 200
                case 7:
                    dif = 150
                case 10:
                    dif = 100