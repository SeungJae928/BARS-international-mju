'''
this program writing Bakay Egor, Moscow, Russia, 2020
BARS_brain version: 1.0
download: https://yadi.sk/d/QsL3RJtT-QnlLA
tutorial: https://www.youtube.com/playlist?list=PL24VxeCr7LD1Z3Cm_VS4bLKthcGdkNWSD
rate app: https://docs.google.com/forms/d/e/1FAIpQLSfOLysTI8F9iPvoiu5R__bpcbtZvHo4up4pca1XKYu9sgEkxA/viewform

This script is part of the project "PROMETHEUS"
https://www.youtube.com/playlist?list=PL24VxeCr7LD3qzQenzNS4zYKe5VYeBOxw

# 9  - нельзя занимать - белая
# 0  - свободная черная клетка
# 1  - белая шашка
# 11 - белая дамка
# 2  - черная шашка
# 12 - черная дамка

area_monitor = [[9, 2, 9, 2, 9, 2, 9, 2], # стартовая позиция
                [2, 9, 2, 9, 2, 9, 2, 9],
                [9, 2, 9, 2, 9, 2, 9, 2],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [1, 9, 1, 9, 1, 9, 1, 9],
                [9, 1, 9, 1, 9, 1, 9, 1],
                [1, 9, 1, 9, 1, 9, 1, 9]]

abcxy - BARS
'''

from random import * # x0 = randint(0, 100)
from copy import deepcopy 
import time
from time import sleep
from time import time
    
def generator_move(area_operation, go_color):
    area = deepcopy(area_operation)
    klik = [[-1,-1],
            [-1,-1]]
    go_operation = []
    count1 = 0
    
    def bumerang(go_operation, count1, y2, x2):
        
        def znak2(r):
            if (r>0):
                return 1
            else:
                return 0
            
        if (len(go_operation[len(go_operation)-1])<2):
            return 1
        else:
            into = go_operation[len(go_operation)-1][len(go_operation[len(go_operation)-1])-1]  # самый последний элемент
            into = into%100
            y1 = int(into/10)
            x1 = into%10
            into = go_operation[len(go_operation)-1][len(go_operation[len(go_operation)-1])-2] # самый предпоследний элемент
            into = into%100
            y0 = int(into/10)
            x0 = into%10
            a = znak2(x1-x0)
            b = znak2(y1-y0)
            c = znak2(x2-x1)
            d = znak2(y2-y1)
            if ((a==0 and c==1 or a==1 and c==0) and (d==0 and b==1 or d==1 and b==0)): # просто алгебра логики
                return 0 # <=====
                #return 1
            else:
                return 1

    def eating2(go_operation, count1, area1, y0, x0, y1, x1):
        klik = [[x0,y0],
                [x1,y1]]
        area2 = deepcopy(area1)
        q = area2[ klik[0][1] ][ klik[0][0] ]
        area2[ klik[0][1] ][ klik[0][0] ] = 0
        area2[ klik[1][1] ][ klik[1][0] ] = q
        x0c = klik[0][0]
        y0c = klik[0][1]
        x1c = klik[1][0]
        y1c = klik[1][1]
        c = 0
        if ((abs(x0c-x1c)==abs(y0c-y1c) and abs(y0c-y1c)>=2)): # eat
            while (x1c!=x0c):
                if (area2[y0c][x0c] != 0):
                    if(1): # записать в go_operation какие шашки были съедены
                        count1 = count1 + 1
                        into = go_operation[len(go_operation)-1][len(go_operation[len(go_operation)-1])-1]
                        go_operation[len(go_operation)-1][len(go_operation[len(go_operation)-1])-1] = 10000+area2[y0c][x0c]*100+y0c*10+x0c
                        go_operation[len(go_operation)-1].append(into)
                        #go_operation[len(go_operation)-1].append(10000+area2[y0c][x0c]*100+y0c*10+x0c)
                    area2[y0c][x0c] = area2[y0c][x0c] + 100 # правило одной руки
                    #area2[y0c][x0c] = 0
                x0c = x0c + znak(x1c-x0c)
                y0c = y0c + znak(y1c-y0c)
        area2[ klik[0][1] ][ klik[0][0] ] = 0
        eating(go_operation, count1, area2, go_color, y1, x1)
    
    def eating(go_operation, count1, area_operation, go_color, y, x):
        #global count1
        #global go_operation
        count1 = count1 + 1
        area = deepcopy(area_operation)
        x0 = klik[0][0]
        y0 = klik[0][1]
        x1 = klik[1][0]
        y1 = klik[1][1]
        eat = 0
        xa = 0 # shaska => damka
        while (xa <= 7):
            if (area[0][xa] == 1):
                area[0][xa] = area[0][xa] + 10
            if (area[7][xa] == 2):
                area[7][xa] = area[7][xa] + 10
            xa = xa + 1
        if(1):
            if (area[y][x]==go_color): # proverka na vozmognost siest shaskami
                if (y-2>=0 and x-2>=0):
                    if (area[y][x]%10!=area[y-1][x-1]%10 and area[y-1][x-1]<100 and area[y][x]!=0 and area[y-1][x-1]!=0 and area[y-2][x-2]==0 and bumerang(go_operation, count1, y-2, x-2)):
                        eat = 1
                        a = 0
                        if (y==2 and go_color==1):
                            a = 1000 
                        go_operation[len(go_operation)-1].append(a+go_color*100+(y-2)*10+(x-2))
                        eating2(go_operation, count1, area, y, x, y-2, x-2)
                if (y+2<=7 and x-2>=0):
                    if (area[y][x]%10!=area[y+1][x-1]%10 and area[y+1][x-1]<100 and area[y][x]!=0 and area[y+1][x-1]!=0 and area[y+2][x-2]==0 and bumerang(go_operation, count1, y+2, x-2)):
                        eat = 1
                        a = 0
                        if (y==5 and go_color==2):
                            a = 1000 
                        go_operation[len(go_operation)-1].append(a+go_color*100+(y+2)*10+(x-2))
                        eating2(go_operation, count1, area, y, x, y+2, x-2)
                if (y-2>=0 and x+2<=7):
                    if (area[y][x]%10!=area[y-1][x+1]%10 and area[y-1][x+1]<100 and area[y][x]!=0 and area[y-1][x+1]!=0 and area[y-2][x+2]==0 and bumerang(go_operation, count1, y-2, x+2)):
                        eat = 1
                        a = 0
                        if (y==2 and go_color==1):
                            a = 1000 
                        go_operation[len(go_operation)-1].append(a+go_color*100+(y-2)*10+(x+2))
                        eating2(go_operation, count1, area, y, x, y-2, x+2)
                if (y+2<=7 and x+2<=7):
                    if (area[y][x]%10!=area[y+1][x+1]%10 and area[y+1][x+1]<100 and area[y][x]!=0 and area[y+1][x+1]!=0 and area[y+2][x+2]==0 and bumerang(go_operation, count1, y+2, x+2)): 
                        eat = 1
                        a = 0
                        if (y==5 and go_color==2):
                            a = 1000 
                        go_operation[len(go_operation)-1].append(a+go_color*100+(y+2)*10+(x+2))
                        eating2(go_operation, count1, area, y, x, y+2, x+2)
            if (area[y][x]==go_color+10 and 1): # proverka na vozmognost siest damkami 
                xd1 = x
                xd2 = x
                xd3 = x
                xd4 = x
                yd1 = y
                yd2 = y
                yd3 = y
                yd4 = y
                i = 0
                while (i < 10):
                    if (yd1>0 and xd1>0 and area[yd1-1][xd1-1]==0 and area[yd1-1][xd1-1]<100):
                        yd1 = yd1 - 1
                        xd1 = xd1 - 1
                    if (yd2<7 and xd2>0 and area[yd2+1][xd2-1]==0 and area[yd2+1][xd2-1]<100):
                        yd2 = yd2 + 1
                        xd2 = xd2 - 1
                    if (yd3>0 and xd3<7 and area[yd3-1][xd3+1]==0 and area[yd3-1][xd3+1]<100):
                        yd3 = yd3 - 1
                        xd3 = xd3 + 1
                    if (yd4<7 and xd4<7 and area[yd4+1][xd4+1]==0 and area[yd4+1][xd4+1]<100):
                        yd4 = yd4 + 1
                        xd4 = xd4 + 1
                    i = i + 1
                if (yd1-2>=0 and xd1-2>=0):
                    if (go_color!=area[yd1-1][xd1-1]%10 and area[yd1-1][xd1-1]<100 and area[yd1-1][xd1-1]!=0 and area[yd1-2][xd1-2]==0 and bumerang(go_operation, count1, yd1-1, xd1-1)):
                        eat = 1
                        yd1 = yd1 - 2
                        xd1 = xd1 - 2
                        if (1):
                            i = 1
                            while (yd1>=0 and xd1>=0 and i==1):
                                go_operation[len(go_operation)-1].append(1000+go_color*100+(yd1)*10+(xd1))
                                eating2(go_operation, count1, area, y, x, yd1, xd1)
                                #if (area[yd1][xd1]==0 and yd1==y1 and xd1==x1):
                                yd1 = yd1 - 1
                                xd1 = xd1 - 1
                                if (yd1>=0 and xd1>=0 and area[yd1][xd1]!=0):
                                    i = 0
                if (yd2+2<=7 and xd2-2>=0):
                    if (go_color!=area[yd2+1][xd2-1]%10 and area[yd2+1][xd2-1]<100 and area[yd2+1][xd2-1]!=0 and area[yd2+2][xd2-2]==0 and bumerang(go_operation, count1, yd2+1, xd2-1)):
                        eat = 1
                        yd2 = yd2 + 2
                        xd2 = xd2 - 2
                        if (1):
                            i = 1
                            while (yd2<=7 and xd2>=0 and i==1):
                                go_operation[len(go_operation)-1].append(1000+go_color*100+(yd2)*10+(xd2))
                                eating2(go_operation, count1, area, y, x, yd2, xd2)
                                #if (area[yd2][xd2]==0 and yd2==y1 and xd2==x1):
                                yd2 = yd2 + 1
                                xd2 = xd2 - 1
                                if (yd2<=7 and xd2>=0 and area[yd2][xd2]!=0):
                                    i = 0
                if (yd3-2>=0 and xd3+2<=7):
                    if (go_color!=area[yd3-1][xd3+1]%10 and area[yd3-1][xd3+1]<100 and area[yd3-1][xd3+1]!=0 and area[yd3-2][xd3+2]==0 and bumerang(go_operation, count1, yd3-1, xd3+1)):
                        eat = 1
                        yd3 = yd3 - 2
                        xd3 = xd3 + 2
                        if (1):
                            i = 1
                            while (yd3>=0 and xd3<=7 and i==1):
                                go_operation[len(go_operation)-1].append(1000+go_color*100+(yd3)*10+(xd3))
                                eating2(go_operation, count1, area, y, x, yd3, xd3)
                                #if (area[yd3][xd3]==0 and yd3==y1 and xd3==x1):
                                yd3 = yd3 - 1
                                xd3 = xd3 + 1
                                if (yd3>=0 and xd3<=7 and area[yd3][xd3]!=0):
                                    i = 0
                if (yd4+2<=7 and xd4+2<=7):
                    if (go_color!=area[yd4+1][xd4+1]%10 and area[yd4+1][xd4+1]<100 and area[yd4+1][xd4+1]!=0 and area[yd4+2][xd4+2]==0 and bumerang(go_operation, count1, yd4+1, xd4+1)):
                        eat = 1
                        yd4 = yd4 + 2
                        xd4 = xd4 + 2
                        if (1):
                            i = 1
                            while (yd4<=7 and xd4<=7 and i==1):
                                go_operation[len(go_operation)-1].append(1000+go_color*100+(yd4)*10+(xd4))
                                eating2(go_operation, count1, area, y, x, yd4, xd4)
                                #if (area[yd4][xd4]==0 and yd4==y1 and xd4==x1):
                                yd4 = yd4 + 1
                                xd4 = xd4 + 1
                                if (yd4<=7 and xd4<=7 and area[yd4][xd4]!=0):
                                    i = 0
                #==================================================================
        count1 = count1 - 1
        if (eat==0 and len(go_operation[len(go_operation) - 1])>1):
            #print(count1)
            go_operation.append([])
            i = 0
            c = len(go_operation) - 1
            while (i < count1):
                go_operation[c].append(go_operation[c-1][i])
                i = i + 1
        else:
            del go_operation[len(go_operation) - 1][count1]
        if (len(go_operation[len(go_operation)-1])>0):
            if (go_operation[len(go_operation)-1][len(go_operation[len(go_operation)-1])-1]>2000):
                del go_operation[len(go_operation)-1][len(go_operation[len(go_operation)-1])-1]
                count1 = count1 - 1
        return eat
    ##############################################################################
    x = 0
    y = 0
    eat = 0
    while (y<=7):
        go_operation.append([area[y][x]*100+y*10+x])
        if (eating(go_operation, count1, area, go_color, y ,x)==1):
            eat = 1
        else:
            del go_operation[len(go_operation)-1]
        x = x + 1
        if (x > 7):
            x = 0
            y = y + 1
    if (eat==1):
        wer = 0
        while (len(go_operation) > wer):
            if (len(go_operation[wer])==0):
                del go_operation[wer]
            else:
                wer = wer + 1
    #eat = 0
    ###########################
    if (eat==0): # not eat
        go_operation.clear()
        x = 0
        y = 0
        while (y<=7):
            if (area[y][x]%10==go_color):
                if (area[y][x]/10<1): # not queen
                    if (go_color==1 and y>=1 and x>=1):
                        if (area[y-1][x-1]==0):
                            if (y==1):
                                go_operation.append([100+y*10+x,1100+(y-1)*10+x-1])
                            else:
                                go_operation.append([100+y*10+x, 100+(y-1)*10+x-1])
                    if (go_color==1 and y>=1 and x<=6):
                        if (area[y-1][x+1]==0):
                            if (y==1):
                                go_operation.append([100+y*10+x,1100+(y-1)*10+x+1])
                            else:
                                go_operation.append([100+y*10+x, 100+(y-1)*10+x+1])
                    if (go_color==2 and y<=6 and x>=1):
                        if (area[y+1][x-1]==0):
                            if (y==6):
                                go_operation.append([200+y*10+x,1200+(y+1)*10+x-1])
                            else:
                                go_operation.append([200+y*10+x, 200+(y+1)*10+x-1])
                    if (go_color==2 and y<=6 and x<=6):
                        if (area[y+1][x+1]==0):
                            if (y==6):
                                go_operation.append([200+y*10+x,1200+(y+1)*10+x+1])
                            else:
                                go_operation.append([200+y*10+x, 200+(y+1)*10+x+1])
                else: # queen
                    xd1 = x
                    xd2 = x
                    xd3 = x
                    xd4 = x
                    yd1 = y
                    yd2 = y
                    yd3 = y
                    yd4 = y
                    i = 0
                    while (i < 10):
                        if (yd1>0 and xd1>0 and area[yd1-1][xd1-1]==0):
                            yd1 = yd1 - 1
                            xd1 = xd1 - 1
                            go_operation.append([1000+go_color*100+y*10+x,1000+go_color*100+yd1*10+xd1])
                        if (yd2<7 and xd2>0 and area[yd2+1][xd2-1]==0):
                            yd2 = yd2 + 1
                            xd2 = xd2 - 1
                            go_operation.append([1000+go_color*100+y*10+x,1000+go_color*100+yd2*10+xd2])
                        if (yd3>0 and xd3<7 and area[yd3-1][xd3+1]==0):
                            yd3 = yd3 - 1
                            xd3 = xd3 + 1
                            go_operation.append([1000+go_color*100+y*10+x,1000+go_color*100+yd3*10+xd3])
                        if (yd4<7 and xd4<7 and area[yd4+1][xd4+1]==0):
                            yd4 = yd4 + 1
                            xd4 = xd4 + 1
                            go_operation.append([1000+go_color*100+y*10+x,1000+go_color*100+yd4*10+xd4])
                        i = i + 1
            x = x + 1
            if (x > 7):
                x = 0
                y = y + 1
    klik = [[-1,-1],
            [-1,-1]]
    if (1):
        #print('Text text', end='')
        go_operation2 = deepcopy(go_operation)
        i = 0
        if (eat==1 and 0):
            go_operation.clear()
            while (i < len(go_operation2)): # and 0
                if (len(go_operation2[i]) > 1):
                    go_operation.append(go_operation2[i])
                i = i + 1
            i = 0
    #=======================================================
    # съесть 0 или 1, 2 или 3?
    if (len(go_operation)>1): # если есть варианты, из чего выбирать
        if (len(go_operation[0])>2): # полюбас надо есть
            i = 0
            while (len(go_operation)>i+1):
                u = 1
                if (go_operation[i][0]==go_operation[i+1][0]):
                    flag = 1
                    while (len(go_operation[i])>u+1 and len(go_operation[i+1])>u+1 and flag==1):
                        if (go_operation[i][u]==go_operation[i+1][u] and go_operation[i][u+1]!=go_operation[i+1][u+1]):
                            flag = 0
                        else:
                            u = u + 2
                    if (flag==1):
                        u = u - 2
                    if (go_operation[i][u]==go_operation[i+1][u] and go_operation[i][u+1]!=go_operation[i+1][u+1]):
                        d1 = len(go_operation[i])
                        d2 = len(go_operation[i+1])
                        if (d1==d2):
                            i = i + 1
                        elif (u+2>=d1 and u+2<d2):
                            del go_operation[i]
                        elif (u+2<d1 and u+2>=d2):
                            del go_operation[i+1]
                        else:
                            #print("selection error")
                            #print(i)
                            #print_mas(area)
                            #print_mas(go_operation)
                            i = i + 1
                    else:
                        i = i + 1
                else:
                    i = i + 1
    #print_go_operation()
    return go_operation

if __name__ == "__main__":
    area_monitor = [[9, 2, 9, 2, 9, 2, 9, 2], # стартовая позиция
                    [2, 9, 2, 9, 2, 9, 2, 9],
                    [9, 2, 9, 2, 9, 2, 9, 2],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [1, 9, 1, 9, 1, 9, 1, 9],
                    [9, 1, 9, 1, 9, 1, 9, 1],    
                    [1, 9, 1, 9, 1, 9, 1, 9]]
    go_color = 1 # кто должен пойти: 1 - белые, 2 - черные
    go_operation = generator_move(area_monitor, go_color) # получаем массив возможных ходов,
    # типа: go_operation = [a1,a2,a3...], где a_N - возможный ход из данной похиции вида [abcxy, abcxy]
    print(go_operation)
