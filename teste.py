import pyperclip
import pyautogui as pg
from time import sleep as s
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://www.youtube.com/watch?v=a4ARV1sxOn8&t=628s")
s(10)
element = driver.find_element(By.XPATH, "//tp-yt-paper-dialog")
# /html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog
print(element)