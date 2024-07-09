import pyautogui
import time 
pyautogui.PAUSE= 1
# Passo a passo do projeto

 # Passo 1: Entrar no sistema da empresa -#https://desktop.worldtracer.aero/desktop/index.html#!/index/login   
    # abrir o navegador (chrome)
pyautogui.hotkey ("win")
pyautogui.write ("edge")
pyautogui.press ("enter")

 # entrar no link 
 
pyautogui.write("https://desktop.worldtracer.aero/desktop/index.html#!/index/login")

pyautogui.press ("enter")
time.sleep(5)  
#pyautogui.write("33697@AD")

#pyautogui.press("tab")
#pyautogui.write("33697Azul@")
# Passo 2: Fazer login
pyautogui.click(x=1208, y=862)
time.sleep(10)
pyautogui.click(x=1379, y=838)
time.sleep(10)
pyautogui.click(x=314, y=343)

pyautogui.click(x=179, y=438)
    
  

    
 # Passo 3: Importar a base de produtos pra cadastrar

# clicar no campo de código