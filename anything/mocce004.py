from timeit import repeat
import pyautogui as pa
import pygame

senha = pa.password('Digite a senha', 'Login')
if senha == 'me_mama':
    pa.alert('SUUS')
    pygame.init()
    pygame.mixer.music.load('pqp.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    while True:
        for i in range(10):
            pa.alert('AMONGUS!')
        parar = pa.confirm('SuS?', 'is sus?', ['YaaaY', 'noooN', 'niexT'])
        if parar == 'noooN':
            break
        elif parar == 'niexT':
            pygame.mixer.music.stop()
            pygame.mixer.music.load('prince_ali_copy.mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
        else:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('pqp.mp3')
            pygame.mixer.music.play()
            pygame.event.wait()