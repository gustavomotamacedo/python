import time
import pygame
import pyautogui as pa

res = pa.confirm(text='Is a jojo reference?', title='is?', buttons=['YES YES YES YES', 'NO NO NO NO'])

if res == 'YES YES YES YES':
    pygame.init()
    pygame.mixer.music.load('pqp.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    pa.alert('OH NO! IS A REQUIEM')
    i = 1
    while i < 3:
        if i == 1:
            alerta = pa.alert('⠀⣄⡀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠁⠂⠀⠀⠀⠀⠀⠈⠉⠐⢥⣁⠢⡀⠀⠀⠀⠀\n⠀⢿⡈⠐⠒⠉⠉⠈⠁⠀⠈⠀⠂⠄⡀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠁⠜⣀⠀⠀⠀\n⠀⢸⠹⡄⠀⠀⠀⠀⠀⠤⠤⠄⣀⠤⠊⠑⠆⠈⠢⣀⠀⢠⢻⠟⠲⠅⡀⠥⠄⠀\n⠀⢞⡄⠐⡌⠀⠀⠀⠀⠀⠀⡔⠁⠠⠂⠈⠉⠁⠒⢜⡶⡡⠃⢀⢤⡀⠐⡀⡐⠀\n⠀⠘⡎⢄⠈⠢⡀⠀⡠⣀⢰⢠⢁⠀⠠⣲⣶⣶⡀⠈⠷⠁⠀⣿⢈⡘⠀⡇⡟⠀\n⠀⠀⡟⢄⠑⠀⠡⡀⠀⢈⠉⣇⠀⠀⠀⠻⣿⣿⡇⠀⡗⡄⠀⢟⣼⡿⠠⠀⠃⠀\n⢤⡒⢟⣄⠀⠈⠐⠵⣄⡠⢍⢊⢳⣄⠀⠀⠀⠂⢀⣰⣐⣐⣄⠀⢉⣠⣷⠖⠒⠁\n⠀⢹⢢⢀⡐⠄⡀⢄⠈⠋⢘⣛⣾⠟⢿⣶⣶⠶⠟⠛⢻⢿⣿⣿⡍⣼⣾⠄⠀⠀\n⠀⠀⣆⡄⠀⢀⢜⠻⡦⡀⣈⠦⢈⣶⢟⠊⣥⣠⣤⣂⣼⡆⠀⣸⣟⢯⡟⠀⠀⠀\n⠀⠀⡿⡈⣅⡇⢸⣷⡽⠬⠟⠀⠈⠹⣍⣿⣯⣏⢭⣼⠟⠁⠀⣻⡛⠋⡇⠀⠀⠀\n⠀⠀⠀⡿⠉⣣⡈⢿⣿⡀⠀⠀⠀⠜⠀⠉⠉⠁⠈⠀⠀⢀⡶⠟⠇⠀⠃⠀⠀⠀\n⢀⠴⢋⠀⢸⡁⣱⢄⠉⠙⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⣰⡸⠀⠀⠀⠀\n⡆⠀⡜⠀⠃⢵⠁⣸⣷⣶⡇⠀⠀⢃⠀⠀⠀⠀⠀⠀⠀⠀⣲⣟⡇⠇⠀⠀⠀⠀\n⠀⡰⠁⣀⠜⠀⢰⣿⡁⠘⣷⣄⡀⡈⠀⠀⠀⠀⠀⠀⠴⠬⠒⢺⠼⠀⠀⠀⠀⠀\n⠶⣥⣴⣁⣀⣴⠛⠻⡿⢷⣾⣿⣟⠶⣄⠀⠀⠀⠀⠀⠐⣦⡴⠃⠇⠀⠀⠀⠀⠀\n⡐⡙⢸⣾⣿⣿⠀⠘⣯⠀⠨⠋⠻⢷⣿⣿⣶⣤⣀⣀⠀⢉⡁⠌⠀⠀⠀⠀⠀⠀\n⠜⠀⣸⡿⠟⠁⠀⢸⣇⠉⡘⠄⡀⠀⠉⠻⣿⣿⡿⠉⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀\n⣀⣴⣿⣷⣦⣄⣀⣿⡈⠐⠧⡀⠈⢂⠄⢤⠹⣯⣯⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠟⠩⠒⠉⣹⠀⠀⠀⠈⠘⠄⡈⠑⡌⠠⠸⠀⣿⣿⡎⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⡠⠊⠉⠁⠀⠉⠀⠂⠄⡈⠐⢧⣀⠀⠀⣿⣿⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠖⠉⠀⢀⣠⣴⣶⣦⣤⣀⠀⠈⠐⠀⠉⠻⣿⣿⢸⡇⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⡈⠢⣀⣼⠟⢟⣷⠟⢧⡢⠀⠀⠀⠀⠀⠀⠀\n')
            i += 1
            print(alerta)
        elif i > 1:
            alerta = pa.alert('⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⣲⣒⢐⣲⣶⡦⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠠⠒⠀⠩⢭⣄⣠⡔⢀⡒⡝⢁⣤⠑⠁⣤⢡⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⣀⢷⠀⡭⡂⢄⡇⠈⡜⣧⢀⠸⡙⠇⠟⡿⢸⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⢜⠂⡱⢄⠑⠂⠱⣆⠹⠈⡸⢤⣠⠞⠑⠒⠇⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⢹⡅⡫⣲⢟⣐⡏⠉⠷⠊⠄⣀⠀⠀⡔⠈⡺⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠈⡮⢈⢤⡌⡲⡀⠀⣠⣤⠤⣄⠧⠰⣶⡿⡇⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠘⡢⣿⡩⡯⠇⠐⡟⠛⠂⠉⠁⠀⠥⡀⡅⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢲⣌⢟⢍⡄⠀⠀⠀⠀⠀⠀⠠⠞⢡⠁⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⡘⠯⣯⣽⠹⢆⡀⠀⠀⠀⠠⣄⡳⡇⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⣻⣍⣼⣿⣇⢡⡈⠑⢦⣤⣀⣀⡠⣁⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⡴⢋⣿⣟⡇⠉⡏⠟⠲⢤⣌⣿⣿⠃⠀⡇⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⡴⢶⣷⣯⡵⣻⠗⡀⢱⢲⠄⡔⢢⣯⢇⠀⢰⡦⣀⢀⡀⠀⠀⠀\n⠀⠀⠸⣷⣿⣾⡟⣋⠀⠁⠚⠾⣌⡐⡀⠈⢹⠀⣧⣾⣲⣽⠻⡌⢂⠀⠀\n⢀⣤⣔⣿⣧⣤⣽⢿⣷⣤⣌⣀⣀⠉⣳⣦⣼⡆⢯⡟⠓⠲⣔⠈⢢⡱⡀\n⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣻⣍⣀⣴⣫⠗⠂⠉⠙⡄⠀⠀⠈⠖⣼⣷⡇\n')
            i -= 1
            print(alerta)
