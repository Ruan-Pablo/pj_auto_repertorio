import pyperclip
import pyautogui as pg
from time import sleep as s

# abrir o youtube
# from mouseinfo import mouseInfo
# (707,160) pesquiar do youtube
# (723,626) primeiro vídeo
# (1258,950) 3pontin
# (1268,836) salvar
# (900,465) repertorio aline ou tab tab tab
# (1202,167) X do pesquisar

    

s(1)
def abrirYoutube():
    s(1)
    pg.hotkey('win')
    s(0.5)
    pg.write('youtube',interval=0.25)
    pg.press('enter')
    s(3)
    pg.press('tab')
    s(0.5)
    pg.press('enter')


def altTab():
    pg.keyDown('alt')
    pg.keyDown('tab')
    pg.keyUp('alt')

def salvar_tab():
    # pg.click(1260,986, interval=0.5) #clicar nos 3 pontin do youtube
    # cont = 0
    for i in range(0,18):
        s(0.25)
        pg.press('tab')
        # cont+=1
        print("tab")
    pg.press('space')
    pg.press(['tab','tab'], interval=1)
    s(1)
    pg.press('space')
    s(1)
    pg.click(900,465,interval=0.5)# repertorio
    s(2)
    pg.press('esc')
    s(1)
    pg.press('esc')



arq = open('repertorio.txt', 'r')
lines = arq.readlines()
print(lines)

s(4)
for music in lines: #aqui ja está com a page da yt aberta
    s(2)
    pg.click(54,489) #click fora
    pyperclip.copy(music)
    pg.click(707,160, interval=1) #pesquisar
    s(1)
    pg.hotkey('ctrl','v')
    pg.press('enter')
    s(5) 
    pg.click(646,599, interval=0.5) # seleciona o primeiro
    # pg.press('enter')
    s(3)
    salvar_tab()
    pg.click(1202,167, interval=1) # apagar a pesquisa

