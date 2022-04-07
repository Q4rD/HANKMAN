## menu ##
from tqdm import tqdm
import time
import os

from load import loading
from hankman import game
clear = lambda: os.system('clear')

menu = "——————————————————————————\n ( >-_-)>[HANKMAN]<(-_-< )\n\n          <play>\n          <exit>\n\nнапишите play чтобы начать\nнапишите exit чтобы выйти\n——————————————————————————" 
print(menu)
menuPUT = input()
if menuPUT == 'play':
    clear()
    # for i in tqdm(range(100),desc='loading'):   
    #     time.sleep(0.04)
    loading()
    clear()
    game()
elif menuPUT == 'exit':
    clear()
    quit()
###########