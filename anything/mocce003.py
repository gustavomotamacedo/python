from asyncio.windows_events import NULL
from socket import htonl
import time
import pyautogui as pa


def getIp():
    pa.hotkey('win', 'r')
    pa.write('cmd')
    pa.press('enter')
    time.sleep(0.5)
    pa.write('ipconfig')
    pa.press('enter')
    time.sleep(0.5)
    pa.click(1366/2, 768/2)
    pa.hotkey('ctrl', 'a')
    pa.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pa.hotkey('alt', 'f4')
    time.sleep(0.5)

def saveOnNotepad(cont):
    pa.hotkey('win', 'r')
    pa.write('notepad')
    pa.press('enter')
    time.sleep(0.5)
    pa.hotkey('ctrl', 'v')
    pa.hotkey('ctrl', 's')
    pa.write('ip-do-boboca{}.txt' .format(cont))
    pa.press('enter')
    time.sleep(0.5)
    pa.hotkey('alt', 'f4')
    time.sleep(0.5)

def saveAScreenshot(cont):
    pa.press('prntscrn')
    pa.hotkey('win', 'r')
    pa.write('mspaint')
    pa.press('enter')
    time.sleep(0.5)
    pa.hotkey('ctrl', 'v')
    time.sleep(1)
    pa.hotkey('ctrl', 's')
    time.sleep(0.5)
    pa.write('print_do_boboca{}.jpeg' .format(cont))
    pa.press('enter')
    time.sleep(0.5)
    pa.hotkey('alt', 'f4')
    time.sleep(0.5)

def openVSCode():
    pa.hotkey('win', 'r')
    pa.write('Code')
    pa.press('enter')
    time.sleep(0.5)    

cont1 = 0
cont2 = 0
while True:
    escolha = pa.confirm(text='Escolha o que deseja fazer', title='App legal!', buttons=['Salvar ip no bloco de notas', 'Tirar um print', 'Abrir VS Code','Parar'])
    print(escolha)
    if escolha == 'Salvar ip no bloco de notas':
        getIp()
        saveOnNotepad(cont1)
        cont1 += 1
    elif escolha == 'Tirar um print':
        saveAScreenshot(cont2)
        cont2 += 1
    elif escolha == 'Abrir VS Code':
        openVSCode()
    elif escolha == 'Parar' or escolha == None:
        break
