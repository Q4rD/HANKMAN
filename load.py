
from time import sleep
import os

def loading():
    clear = lambda: os.system('clear')
    a = 0
    while a < 100:
        a=a+5
        fr1 ='( >-_->)'
        fr2 ='    ( >-_->)'
        fr3 ='        ( >-_->)'
        fr4 ='            ( >-_->)'
        fr5 ='                ( >-_->)'
        fr6 ='                <(-_-< )'
        fr7 ='            <(-_-< )'
        fr8 ='          <(-_-< )'
        fr9 ='      <(-_-< )'
        fr10 ='<(-_-< )'
        sleep(0.05)
        clear()
        print(fr1,a)
        sleep(0.05)
        clear()
        print(fr2,a)
        sleep(0.05)
        clear()
        print(fr3,a)
        sleep(0.05)
        clear()
        print(fr4,a)
        sleep(0.05)
        clear()
        print(fr5,a)
        sleep(0.05)
        clear()
        print(fr6,a)
        sleep(0.05)
        clear()
        print(a,fr7)
        sleep(0.05)
        clear()
        print(a,fr8)
        sleep(0.05)
        clear()
        print(a,fr9)
        sleep(0.05)
        clear()
        print(a,fr10)
    else:
        a = 100
        sleep(2)

    
    