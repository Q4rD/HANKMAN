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
    ## Темы ##
    print(ots1,"выберите тему.",ots2)
    print("1. рандом")

    spisk = input('тема: ')
    
    if spisk == '1':
        spisk = open ('words1.txt', 'r')
    clear()
    ##########
    ## сложность ##
    print(ots1,"Чтобы выйти напишите: exit.")

    print(ots1,"выберите сложность",ots2)
    dific = input("dificults: \n1. easy \n2. normal \n3. hard \n4. HAHAHAHAHAHAHAHA...\nсложность: ")
    if dific == "1":
        attempt = 20
        print(ots1,"dific: easy",ots2)
    elif dific == "2":
        attempt = 10
        print(ots1,"dific: normal",ots2)
    elif dific == "3":
        attempt = 5
        print(ots1,"dific: hard",ots2)
    elif dific == "4":
        attempt = 1
        print(ots1,"dific: HAHAHAHAHAHAHAHA...",ots2)
    elif dific == "exit":
            clear()
            print(ots1,"Вы успешно ВЫШЛИ из игры.",ots2)
            sleep(1)
            clear()
            quit()
    sleep(1)
    clear()
    print(ots1,"Чтобы выйти напишите: exit.\nНапишите bonus чтобы добавить +3 попытки.",ots2)
    ###############
    test=False
    usedln=""
    win=[]

    #spisk = open('words1.txt', 'r')
    # Список #####################
    with spisk as w:
        for i in w:
            # Рандомное слово ############
            w1 = random.choice(list(w))

    d1 ="".join(c for c in w1 if c.isalpha())
    w1= w1.rstrip('\n')
    w1= w1.rstrip(' ')
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
            win1 = ' '.join(win)
            print("Использованные БуКвЫ:", ','.join(usedln))
            print('( >-_-)> воть [',win1,']')          
            let = input("\nВвод:  ")
            print("---------------------")
            if let == "exit":
                clear()
                print(ots1,"Вы успешно ВЫШЛИ из игры.",ots2)
                sleep(1)
                clear()
                quit()

    ##### Бонус ####################
            if let == "bonus":   
                clear()
                if iAttempts == True:           
                    print(ots1,"Вы использовали бонус!!!",ots2)
                    attempt +=3
                    iAttempts = False 
                elif iAttempts == False:
                    print(ots1,"Вы УЖЕ использовали бонус!!!",ots2)
    ###################################            
            if let != "bonus":
                if let in usedln or len(let)>1:
                    clear()
                    sim =','.join(usedln)
                    print(ots1,"Не больше одного символа, попробуйте снова!",ots2)
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
            print(ots1,"Неверно (-___-)",ots2)
            win1 = ' '.join(win)
            #print('[',win1,']')
        else:
            win1 = ' '.join(win)
            print(ots1,"Верно (UwU)!",ots2)
            #print('[',win1,']')
    
        print("Ваше здоровье = ", attempt)
    
    if(d2 == 0):
        clear = lambda: os.system('clear')

        frame1 = '( /UwU)/бедили'
        frame2 = '  по\n\(UwU)/'
        frame3 = 'вы\(UwU\)'


        a = 1
        while a < 3:
            a=a+1
            sleep(0.4)
            clear()
            print(frame3)
            sleep(0.4)
            clear()
            print(frame2)
            sleep(0.4)
            clear()
            print(frame1)
        else:
            clear()
            print(ots1,"ВЫ ПОБЕДИЛИ!!! \n Слово было", d1.upper(),ots2)
            sleep(3)
            clear()
            quit()
    else:
        clear = lambda: os.system('clear')

        frame1 = '( /-_-)/играли'
        frame2 = '  про\n\(-_-)/'
        frame3 = 'вы\(-_-\)'
        frame4 ='(-_-)'

        a = 1
        while a < 3:
            a=a+1
            sleep(0.4)
            clear()
            print(frame3)
            sleep(0.4)
            clear()
            print(frame2)
            sleep(0.4)
            clear()
            print(frame1)
            sleep(0.4)
            clear()
            print(frame2)
        else:
            clear()
            print(ots1,"вы проиграли \n Слово было", d1.upper(),ots2)
            sleep(3)
            clear()
            quit()