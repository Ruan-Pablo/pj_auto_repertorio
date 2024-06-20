import pyperclip
import pyautogui as pg
from time import sleep as s

# abrir o youtube
# from mouseinfo import mouseInfo

# (707,160) pesquiar do youtube
# (723,626) primeiro vídeo
# (1258,950) 3pontin
#   (333,941) 3ponto tela em 75%
# (1268,836) salvar
# (900,465) repertorio aline ou tab tab tab
# (1202,167) apagar, X do pesquisar

    # TESTANDO COM A TELA EM 75% - pra ver se o botao para de sair do lugar

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

def clicar_repertorio():
    pos75 = (844,490) #75%
    pg.click(pos75,interval=0.5)


def salvar_tab():
    for i in range(4):
        pg.press('tab', interval=1)
        print('tab')
        s(1)
    s(1)
    pg.press('space')
    s(1)
    pg.press('esc')
    s(1)
    pg.press('esc')

def pontin_tab():
    # pg.click(1260,986, interval=0.5) #clicar nos 3 pontin do youtube
    # cont = 0
    for i in range(0,18):
        s(0.25)
        pg.press('tab')
        # cont+=1
        print("tab")
    pg.press('space')
    # salvar_tab()
    s(1)
    clicar_repertorio() # repertorio
    s(2)
    pg.press('esc')
    s(1)
    pg.press('esc')

def pontin_click():
    pos75 = (1336,951)
    pg.click(pos75, interval=1)





arq = open('repertorio.txt', 'r')
lines = arq.readlines()
print(lines)

pos_pesquisar75 = (737,156)
pos_segundo_vid75 = (646,599)
pos_segundo_vid75 = (646,599)
apagar_pesq75 = (1140,158)
s(4)
encontrado = True
for music in lines: #aqui ja está com a page da yt aberta

    pyperclip.copy(music)
    pg.click(pos_pesquisar75, duration=1) #pesquisar
    s(1)
    pg.hotkey('ctrl','v')
    pg.press('enter')
    s(5) 
    pg.click(pos_segundo_vid75, duration=1) # seleciona o primeiro
    # pg.press('enter')
    s(3)


    # pontin_tab()
    pontin_click()
    while encontrado:
        try:
            pg.click('salvar.png', duration=1)
            encontrado = False
        except pg.ImageNotFoundException:
            print("Imagem SALVAR nao encontrada.")
    encontrado = True
    s(1)
    while encontrado:
        try:
            pg.click('repertorio.png', duration=1)
            encontrado = False
        except pg.ImageNotFoundException:
            print("Imagem ALINE nao encontrada.")
    encontrado = True
    pg.click(apagar_pesq75, duration=1) # apagar a pesquisa
    s(2)
    pg.click(54,489) #click fora
