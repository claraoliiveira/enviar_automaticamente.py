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
# Passo 2: NAVEGAR NO SISTEMA E ENCONTRAR A BASE DE DADOS (ENTRAR NA PASTA EXPLORAR)
pyautogui.click(x=516, y=361, clicks = 2)
time.sleep(2)
pyautogui.click(x=437, y=443)
pyautogui.click(x=1668, y=233)
pyautogui.click(x=1441, y=783)
time.sleep(7)
#Passo 3 CALCULAR OS INDICADORES(FATURAMENTO E QUANTIDADE DE PRODUTOS VENDIDOS)
import pandas
tabela = pandas.read_excel(r"C:\Users\clara\Downloads\Vendas - Dez.xlsx")
display(tabela)
#Passo 3 CALCULAR OS INDICADORES(FATURAMENTO E QUANTIDADE DE PRODUTOS VENDIDOS)
quantidade = tabela['Quantidade'].sum()
faturamento = tabela['Valor Final'].sum()
display(quantidade)
display(faturamento)
#Entrar no e-mail
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/1/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(7)
#ESCREVER E ENVIAR EMAIL
pyautogui.click(x=130, y=261)
pyautogui.write('claraloliveirap@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyperclip.copy('Relátorio de Vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
texto = f"""
Prezados, bom dia.
O faturamento do dia de ontem foi R${faturamento:.2f}
e a quantidade de produtos vendidos foi de {quantidade:}
Abs
EU"""
time.sleep(3)
pyperclip.copy(texto)
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('ctrl', 'enter')
time.sleep(3)


time.sleep(8)
pyautogui.position()
