import pyautogui as pa
import pygame
pygame.init()
instrumento = pa.confirm('Selecione o instrumento:', 'Seleção', ['Ocarina', 'Harmonica', 'Piano'])
instrumento = instrumento.lower()
fade = 1500
largura = (300,200)
janela = pygame.display.set_mode(largura)
while True:
    tecla = pygame.key.get_pressed()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if evento.type == pygame.KEYDOWN:
            if evento.key == ord('a'):
                pygame.mixer.music.load(f'{instrumento}_C.ogg')
                pygame.mixer.music.play(fade_ms=fade)
                print("tecla 'a' foi apertada")
            if evento.key == ord('s'):
                pygame.mixer.music.load(f'{instrumento}_C.ogg')
                pygame.mixer.music.play(fade_ms=fade)
                print("tecla 's' foi apertada")
            if evento.key == ord('d'):
                pygame.mixer.music.load(f'{instrumento}_E.ogg')
                pygame.mixer.music.play(fade_ms=fade)
                print("tecla 'd' foi apertada")
            if evento.key == ord('f'):
                pygame.mixer.music.load(f'{instrumento}_F.ogg')
                pygame.mixer.music.play(fade_ms=fade)
                print("tecla 'f' foi apertada")
            if evento.key == ord('g'):
                pygame.mixer.music.load(f'{instrumento}_G.ogg')
                pygame.mixer.music.play(fade_ms=fade)
                print("tecla 'g' foi apertada")
            if evento.key == ord('h'):
                pygame.mixer.music.load(f'{instrumento}_A.ogg')
                pygame.mixer.music.play(fade_ms=fade)
                print("tecla 'h' foi apertada")
            if evento.key == ord('j'):
                pygame.mixer.music.load(f'{instrumento}_B.ogg')
                pygame.mixer.music.play(fade_ms=fade)
                print("tecla 'j' foi apertada")
            if evento.key == ord('k'):
                pygame.mixer.music.load(f'{instrumento}_C2.ogg')
                pygame.mixer.music.play(fade_ms=fade)
                print("tecla 'k' foi apertada")
            if evento.key == ord('l'):
                pygame.mixer.music.load(f'{instrumento}_D2.ogg')
                pygame.mixer.music.play(fade_ms=fade)
                print("tecla 'l' foi apertada")
            if evento.key == ord('ç'):
                pygame.mixer.music.load(f'{instrumento}_E2.ogg')
                pygame.mixer.music.play(fade_ms=fade)
                print("tecla 'ç' foi apertada")        