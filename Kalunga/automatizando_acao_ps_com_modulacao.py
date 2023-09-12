import pyautogui
import time

cont = 0
conclusao = 30

def alt_tab():
    pyautogui.hotkey('alt', 'tab')

def aperta_botoes():
    pyautogui.hotkey('shift', 'F4')


alt_tab()
while (cont < conclusao):
    aperta_botoes()
    cont += 1
    print(f'o contador está na posição {cont}')
print('automação concluída!')