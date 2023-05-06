import pyautogui as paut
import time
import os
from datetime import date


data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto)

paut.hotkey('win','r')
paut.write('cmd', interval=0.1)
paut.press('enter')
time.sleep(0.9)

paut.write("git init", interval=0.05)
paut.press('enter')

time.sleep(0.5)

paut.write("cd C:/server_index_github", interval=0.05)
paut.press('enter')
paut.write("git init", interval=0.05)
paut.press('enter')
paut.write('git add .', interval=0.05)
paut.press('enter')
paut.write('git status', interval=0.05)
paut.press('enter')
time.sleep(1)

paut.write(f'git commit -m "{data_em_texto}"')
paut.press('enter')

time.sleep(0.8)
paut.write('git push https://github.com/GuilhermeTeo/NEWPAGE.git master -f')
paut.press('enter')
time.sleep(5)

paut.write('exit')
paut.press('enter')
