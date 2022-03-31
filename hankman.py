import random
import os
from time import sleep

def game():
    #################################
    clear = lambda: os.system('clear')
    ots1 = '---------------------\n'
    ots2 = '\n---------------------'
    #################################
    ## ИГРА ##
    ## сложность ##
    print(ots1,"выберите сложность",ots2)
    dific = input("dificults: \n1. easy \n2. normal \n3. hard \n4. HAHAHAHAHAHAHAHA...\nсложность: ")
    if dific == "1":
        attempt = 20
        print("dific: easy")
    elif dific == "2":
        attempt = 10
        print("dific: normal")
    elif dific == "3":
        attempt = 5
        print("dific: hard")
    elif dific == "4":
        attempt = 1
        print("dific: HAHAHAHAHAHAHAHA...")
        print(ots)
    sleep(1)
    clear()
    print(ots1,"чтобы выйти напишите: exit\nнапишите health чтобы добавить +3 попытки",ots2)
    ###############
    test=False
    usedln=""
    win=[]

    # Список #####################
    with open('words2.txt', 'r') as w:
        for i in w:
            # Рандомное слово ############
            w1 = random.choice(list(w))

    d1 ="".join(c for c in w1 if c.isalpha())
    w1= w1.rstrip('\n')
    d1 = w1
    d2=len(d1)
    #print("слово: ",d1)
    ###############################   
    iAttempts = True

    # диапозон ##########
    for i in range(len(w1)):
        win+="_"
    
    while d2 != 0 and attempt != 0:
        test = False
    # Введите слово ##############
        while True:
            let = input("ввод:  ")
            if let == "exit":
                clear()
                print(ots1,"Вы успешно ВЫШЛИ из игры.",ots2)
                sleep(1)
                clear()
                quit()

    ##### аптечка ####################
            if let == "health":   
                clear()
                if iAttempts == True:           
                    print(ots1,"Вы использовали аптечку!!!",ots2)
                    attempt +=3
                    iAttempts = False 
                elif iAttempts == False:
                    print(ots1,"Вы УЖЕ использовали аптечку!!!",ots2)
    ###################################            
            if let != "health":
                if let in usedln or len(let)>1:
                    clear()
                    print(ots1,"Не больше одного символа, попробуйте снова!\nиспользованные БуКвЫ:",','.join(usedln),ots2)
                else:
                    usedln+=let
                    break

        count=0
        for i in w1:
            if let in i:
                d2 -= 1
                test=True
                win[count]=let
            count+=1

        clear()  

        if not test:
            attempt -= 1
            print(ots1,"Неверно\nиспользованные БуКвЫ:", ','.join(usedln),ots2)
            win1 = ' '.join(win)
            print('[',win1,']')
        else:
            win1 = ' '.join(win)
            print(ots1,"Верно\nиспользованные БуКвЫ:", ','.join(usedln),ots2)
            print('[',win1,']')
    
        print("Ваше здоровье = ", attempt)
    
    if(d2 == 0):
        sleep(1)
        clear()
        print(ots1,"ВЫ ПОБЕДИЛИ!!! \n Слово было", d1.upper(),ots2)
        sleep(3)
        clear()
        quit()
    else:
        sleep(1)
        clear()
        print(ots1,"ВЫ ПРОИГРАЛИ! ПОПРОБУЙТЕ СНОВА!", "\n слово было: ", d1.upper(),ots2)
        sleep(3)
        clear()
        quit()