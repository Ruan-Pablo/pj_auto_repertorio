import pyperclip
import pyautogui as pg
from time import sleep as s
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Edge()

# driver.get("https://www.youtube.com/watch?v=a4ARV1sxOn8&t=628s")
# s(10)
# element = driver.find_element(By.XPATH, "//tp-yt-paper-dialog")
# /html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog

pos = (670,155)
pos_f = (960,155)
def verifica_selecao():
    pos75_inicial = (1367,837)
    pos75_final = (1447,840)
    pg.move()

# pg.drag(pos, 0, duration=0.5)
# pg.moveTo(pos, duration=0.5, tween=pg.easeInOutQuad)
# pg.dragTo(pos_f, button='left')
# cop = pg.hotkey('ctrl', 'c')
pg.click('salvar.png', duration=2)
exit()
pos = (737,156)
s(2)
pg.click(pos, interval=1)
# print(element)