import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 0.5

#Passo 1: ENTRAR NO SISTEMA (NESSE CASO NO LINK)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")


#carregar site
time.sleep(5)
