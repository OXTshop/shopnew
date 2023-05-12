import pyautogui as paut
import time


paut.hotkey('win','r')
paut.write('cmd', interval=0.1)
paut.press('enter')
time.sleep(0.9)

paut.write("git init", interval=0.05)
paut.press('enter')

time.sleep(0.5)

paut.write("cd C:/OXT", interval=0.05)
paut.press('enter')
paut.write("git init", interval=0.05)
paut.press('enter')
paut.write('git pull https://github.com/OXTshop/shopnew.git')
paut.press('ENTER')
time.sleep(5)
paut.write("exit", interval=0.05)
paut.press('enter')