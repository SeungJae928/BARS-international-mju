import tkinter.messagebox as msgbox
from tkinter import *
from random import * # x0 = randint(0, 100)
from copy import deepcopy 
#import time
from time import sleep
from time import time
Time = int(time()*1000)
ras = 50
#import os.path # для определения наличия файла
#import datetime
import webbrowser
from checkers_BARS_brain import *
BARS_brain_version("2.0 beta")
from checkers_BARS_file_manager import *
BARS_file_manager_version("1.0")


NAME = "BARS 6.1" # 
file = my_file(NAME)
# 0  - свободная черная клетка
# 1  - белая шашка
# 11 - белая дамка
# 2  - черная шашка
# 12 - черная дамка

area_zero = [[9, 2, 9, 2, 9, 2, 9, 2],
             [2, 9, 2, 9, 2, 9, 2, 9],
             [9, 2, 9, 2, 9, 2, 9, 2],
             [0, 9, 0, 9, 0, 9, 0, 9],
             [9, 0, 9, 0, 9, 0, 9, 0],
             [1, 9, 1, 9, 1, 9, 1, 9],
             [9, 1, 9, 1, 9, 1, 9, 1],
             [1, 9, 1, 9, 1, 9, 1, 9]]

area_zero2 = [[9, 0, 9, 0, 9, 0, 9, 0],
              [0, 9, 0, 9, 0, 9, 0, 9],
              [9, 0, 9, 0, 9, 0, 9, 0],
              [0, 9, 0, 9, 0, 9, 0, 9],
              [9, 0, 9, 0, 9, 0, 9, 0],
              [0, 9, 0, 9, 0, 9, 0, 9],
              [9, 0, 9, 0, 9, 0, 9, 0],
              [0, 9, 0, 9, 0, 9, 0, 9]]

#area_operation = []

area_monitor = [[9, 2, 9, 2, 9, 2, 9, 2],
                [2, 9, 2, 9, 2, 9, 2, 9],
                [9, 2, 9, 2, 9, 2, 9, 2],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [1, 9, 1, 9, 1, 9, 1, 9],
                [9, 1, 9, 1, 9, 1, 9, 1],
                [1, 9, 1, 9, 1, 9, 1, 9]]

area_monitor1 = [[9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 2, 9, 0, 9],
                [9, 2, 9, 0, 9, 0, 9, 0],
                [0, 9, 2, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 1],
                [0, 9, 1, 9, 0, 9, 1, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9]]

area_monitor2 = [[9, 0, 9, 0, 9, 2, 9, 0],
                [0, 9, 0, 9, 2, 9, 0, 9],
                [9, 2, 9, 2, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 1, 9, 0, 9, 0],
                [1, 9, 1, 9, 0, 9, 0, 9],
                [9, 1, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9]]

area_monitor3 = [[9, 0, 9, 0, 9, 0, 9, 11],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 2, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 12],
                [0, 9, 0, 9, 2, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9]]

area_monitorz = [[9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9]]

debuts = []
zadania = []

flag_file = 0

history = []
go = [] # все варианты будующих ходов
go_operation = []

klik = [[-1,-1],
        [-1,-1]]
klik_flag = 1
control_edit_checkers = [-1,-1,0]

moved_checkers = -1

go_color = 1

count1 = 0  # for generator_move

control_memory_mode = 0 # задания на память: 1,2 - просто тренажер, 3,4 - дебюты, 5,6 - задания
control_memory_mode_i = 1 # уровень сложности
control_memory_mode_over = -1 # результат
control_move = go_color # кто первый ходит
control_add = 1 # какой цвет\шашку\дамку добавить
control_edit = 0 # я в меню или нет
control_vs = 2 # за кого играет робот #######################################################################################################
go_error = 0 # для вывода на контроллере сообщения об ошибке
control_back = 0 # есть\нет возможности назать "назад"
control_forward = 0 # есть\нет возможности назать "вперед" - но пока не использую
control_revers_monitor = 0 # 1 - нормальное отображение поля; 2 - поле перевернуто (черные ближе к игроку)
control_revers_monitor_always = 0; # отже самое, что и предыдущее, только в любой момент 9а прошлое автоматом)
# для виджетов
control_protocol = []
#control_protocol_ras = 10
control_protocol_flag = 0
control_actions = []
control_actions_flag = 0
area_monitor = deepcopy(area_zero2) # 초기 필드를 빈필드로 설정

level_hard = 1

def read_file():
    global debuts
    global zadania
    global flag_file
    global file
    if (os.path.exists("BARS_protocol.txt")):
        flag_file = 1
    debuts,zadania=file.read()
    
def qwerty():
    global area_monitor
    global area_zero
    global area_zero2
    global klik
    global klik_flag
    global go_color
    global history
    global debuts
    global zadania
    global go
    global go_operation
    global count1
    global control_memory_mode
    global control_memory_mode_i
    global control_memory_mode_over
    global control_move
    global control_add
    global control_edit
    global control_vs
    global go_error
    global control_forward
    global control_back
    global moved_checkers
    global control_edit_checkers
    global control_protocol
    global control_protocol_flag
    global control_actions
    global control_actions_flag
    global control_revers_monitor
    global control_revers_monitor_always
    global level_hard
    out_window = Tk()
    #out_window.title('BARS 4.3')#============> поменять версию и в print_file() # demonstration special
    out_window.title(NAME)
    #window.geometry('1000x1000')
    #canvas = Canvas(out_window,width=9*ras,height=9*ras)
    canvas = Canvas(out_window,width=12*ras,height=9*ras,bg="white") # ,cursor="pencil"

    def print_file():
        global control_vs
        global history
        global file
        file.write(history, control_vs)
        
            
    #===================================================================================================================================================================================================
    #===================================================================================================================================================================================================
    #===================================================================================================================================================================================================
    
    def map(x, in_min, in_max, out_min, out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min);
    
    def millis():
        return int(time()*1000);
    
    def cut(i, a):
        if (abs(i) > a):
            i = abs(i)/i*a;
            i = int(i);
        return i;
    
    def znak(a):
        if   (a > 0): return  1
        elif (a < 0): return -1
        else: return  0

    def num(a):
        if   (a=='0'): return 0
        elif (a=='1'): return 1
        elif (a=='2'): return 2
        elif (a=='3'): return 3
        elif (a=='4'): return 4
        elif (a=='5'): return 5
        elif (a=='6'): return 6
        elif (a=='7'): return 7
        elif (a=='8'): return 8
        elif (a=='9'): return 9
        else: return -1

    def hello():
        print("Hello!")
        print("это специальная программа, для создания готовых диаграмм")
        print("и историй ходов к ним, в СС для этой программы")
        #print("для вывода диаграммы нажмите <вывести диаграмму>")
        #print("для вывда всей истории игры+диаграмма нажмите <вывести протокол>")
        print()
        #canvas.create_rectangle(ras*9,0,ras*12,ras*9,fill="white")
        #canvas.create_text(ras*10.5,ras*3,text="русские",font="Verdana 20",justify=CENTER,fill="black")
        #canvas.create_text(ras*10.5,ras*3,text="шашки",font="Verdana 20",justify=CENTER,fill="black")

    def control_revers_monitor_result():
        global go_color
        global control_vs
        global control_revers_monitor
        global control_revers_monitor_always
        #print(control_revers_monitor_always)
        a1 = 0
        if ((control_vs==1 or go_color==2 and control_vs==3) and control_revers_monitor==1):
            a1 = 1
        a2 = control_revers_monitor_always
        if (a1==1 and a2==0 or a1==0 and a2==1):
            return 1
        else:
            return 0

    def  reboot_controller():
        global control_memory_mode
        global control_memory_mode_i
        global control_memory_mode_over
        global go_color     
        global control_move
        global control_add
        global control_edit
        global control_vs # за кого играет робот
        global go_error
        global control_back
        global control_protocol
        global control_actions
        global control_revers_monitor
        global control_revers_monitor_always
        global debuts
        global zadania
        
        def bykva(xx):
            if(1):
                if  (xx==0):
                    return "a"
                elif(xx==1):
                    return "b"
                elif(xx==2):
                    return "c"
                elif(xx==3):
                    return "d"
                elif(xx==4):
                    return "e"
                elif(xx==5):
                    return "f"
                elif(xx==6):
                    return "g"
                elif(xx==7):
                    return "h"

        def bykva2(b):
            if(1):
                if (b==0):
                    return "-"
                else:
                    return ":"

        def vidget1():
            global control_protocol
            i = 0
            while (i<len(control_protocol)):
                mas = deepcopy(control_protocol[i])
                n = mas[0]
                if (n/10>=1):
                    canvas.create_text(ras*9.5,ras*0.7+i*ras*0.25,text=int(n/10),font="Verdana 8",justify=CENTER,fill="black")
                n = n%10
                canvas.create_text(ras*9.65,ras*0.7+i*ras*0.25,text=n%10,font="Verdana 8",justify=CENTER,fill="black")
                canvas.create_text(ras*9.75,ras*0.7+i*ras*0.25,text=".",font="Verdana 8",justify=CENTER,fill="black")
                if (mas[1]==-1):
                    canvas.create_text(ras*10.35,ras*0.7+i*ras*0.25,text=". . . . .",font="Verdana 8",justify=CENTER,fill="black")
                else:
                    canvas.create_text(ras*10.05,ras*0.7+i*ras*0.25,text=bykva(mas[1]%10),font="Verdana 8",justify=CENTER,fill="black")
                    canvas.create_text(ras*10.2,ras*0.7+i*ras*0.25,text=8-(int(mas[1]/10)),font="Verdana 8",justify=CENTER,fill="black")
                    canvas.create_text(ras*10.35,ras*0.7+i*ras*0.25,text=bykva2(mas[2]),font="Verdana 8",justify=CENTER,fill="black")
                    canvas.create_text(ras*10.5,ras*0.7+i*ras*0.25,text=bykva(mas[3]%10),font="Verdana 8",justify=CENTER,fill="black")
                    canvas.create_text(ras*10.65,ras*0.7+i*ras*0.25,text=8-(int(mas[3]/10)),font="Verdana 8",justify=CENTER,fill="black")
                if (mas[4]==-1):
                    canvas.create_text(ras*11.25,ras*0.7+i*ras*0.25,text=". . . . .",font="Verdana 8",justify=CENTER,fill="black")
                else:
                    canvas.create_text(ras*10.95,ras*0.7+i*ras*0.25,text=bykva(mas[4]%10),font="Verdana 8",justify=CENTER,fill="black")
                    canvas.create_text(ras*11.1,ras*0.7+i*ras*0.25,text=8-(int(mas[4]/10)),font="Verdana 8",justify=CENTER,fill="black")
                    canvas.create_text(ras*11.25,ras*0.7+i*ras*0.25,text=bykva2(mas[5]),font="Verdana 8",justify=CENTER,fill="black")
                    canvas.create_text(ras*11.4,ras*0.7+i*ras*0.25,text=bykva(mas[6]%10),font="Verdana 8",justify=CENTER,fill="black")
                    canvas.create_text(ras*11.55,ras*0.7+i*ras*0.25,text=8-(int(mas[6]/10)),font="Verdana 8",justify=CENTER,fill="black")
                i = i + 1

        def vidget2():
            global control_actions
            i = 0
            while (i<len(control_actions)):
                mas = deepcopy(control_actions[i])
                n = mas[0]
                if (n/10>=1):
                    canvas.create_text(ras*9.5,ras*4.25+i*ras*0.25,text=int(n/10),font="Verdana 8",justify=CENTER,fill="black")
                n = n%10
                canvas.create_text(ras*9.65,ras*4.25+i*ras*0.25,text=n%10,font="Verdana 8",justify=CENTER,fill="black")
                canvas.create_text(ras*9.75,ras*4.25+i*ras*0.25,text=".",font="Verdana 8",justify=CENTER,fill="black")
                if (mas[1]==-1):
                    canvas.create_text(ras*10.35,ras*4.25+i*ras*0.25,text=". . . . .",font="Verdana 8",justify=CENTER,fill="black")
                else:
                    canvas.create_text(ras*10.05,ras*4.25+i*ras*0.25,text=bykva(mas[1]%10),font="Verdana 8",justify=CENTER,fill="black")
                    canvas.create_text(ras*10.2,ras*4.25+i*ras*0.25,text=8-(int(mas[1]/10)),font="Verdana 8",justify=CENTER,fill="black")
                    canvas.create_text(ras*10.35,ras*4.25+i*ras*0.25,text=bykva2(mas[2]),font="Verdana 8",justify=CENTER,fill="black")
                    canvas.create_text(ras*10.5,ras*4.25+i*ras*0.25,text=bykva(mas[3]%10),font="Verdana 8",justify=CENTER,fill="black")
                    canvas.create_text(ras*10.65,ras*4.25+i*ras*0.25,text=8-(int(mas[3]/10)),font="Verdana 8",justify=CENTER,fill="black")
                i = i + 1
        
        canvas.create_rectangle(ras*9,0,ras*12,ras*9,fill="white")
        #control_edit = 1 #
        if (control_edit==0 or control_memory_mode==6):
            canvas.create_text(ras*10.5,ras*0.25,text="파티 프로토콜",font="Verdana 8",justify=CENTER,fill="black")
            canvas.create_rectangle(ras*9.25,ras*0.5,ras*11.75,ras*3.5,fill="white")  # ras*6
            canvas.create_text(ras*10.5,ras*3.75,text="가능한 움직임",font="Verdana 8",justify=CENTER,fill="black")
            canvas.create_rectangle(ras*9.25,ras*4,ras*11.75,ras*6,fill="white")
            canvas.create_rectangle(ras*10.625,ras*8.25,ras*11.75,ras*8.75,fill="white")
            if (control_memory_mode==6):
                canvas.create_text(ras*11.1875,ras*8.5,text="go out(나가라)",font="Verdana 8",justify=CENTER,fill="black")
            else:
                canvas.create_text(ras*11.1875,ras*8.5,text="메뉴",font="Verdana 8",justify=CENTER,fill="black")
            if (control_back):
                canvas.create_rectangle(ras*9.25,ras*8.25,ras*10.375,ras*8.75,fill="white", outline="black")
                canvas.create_text(ras*9.8125,ras*8.5,text="back(뒤)",font="Verdana 8",justify=CENTER,fill="black")
            else:
                canvas.create_rectangle(ras*9.25,ras*8.25,ras*10.375,ras*8.75,fill="white", outline="grey")
                canvas.create_text(ras*9.8125,ras*8.5,text="back(뒤)",font="Verdana 8",justify=CENTER,fill="grey")
            # вывод в виджеты
            vidget1()
            vidget2()
            if (go_error==11):
                canvas.create_text(ras*10.5,ras*6.375,text="화이트 이겼다!",font="Verdana 8",justify=CENTER,fill="black")
            elif (go_error==12):
                canvas.create_text(ras*10.5,ras*6.375,text="블랙 이겼다!",font="Verdana 8",justify=CENTER,fill="black")
            elif (control_vs==1 and go_color==2 or control_vs==2 and go_color==1 or control_vs==3 or control_memory_mode==6 or go_error==9):
                if (go_error==1):
                    canvas.create_text(ras*10.5,ras*6.375,text="당신은 잡아야합니다",font="Verdana 8",justify=CENTER,fill="red")
                elif (go_error==2):
                    canvas.create_text(ras*10.5,ras*6.375,text="당신은 움직일 수 없습니다",font="Verdana 8",justify=CENTER,fill="black")
                elif (go_error==3):
                    canvas.create_text(ras*10.5,ras*6.375,text="다른 플레이어가 이동 중입니다",font="Verdana 7",justify=CENTER,fill="black")
                elif (go_error==4):
                    canvas.create_text(ras*10.5,ras*6.375,text="다시 생각해라",font="Verdana 8",justify=CENTER,fill="black")
                elif (go_error==5):
                    canvas.create_text(ras*10.5,ras*6.375,text="작업 완료!",font="Verdana 8",justify=CENTER,fill="black")
                elif (go_error==9):
                    canvas.create_text(ras*10.5,ras*6.375,text="로봇 생각...",font="Verdana 8",justify=CENTER,fill="black")
            # for special version:
            if (control_memory_mode!=6):
                canvas.create_rectangle(ras*9.25,ras*7.5,ras*11.75,ras*8.0,fill="white")
                canvas.create_text(ras*10.5,ras*7.75,text="시작하기",font="Verdana 8",justify=CENTER,fill="black") # 원래 프로토콜 저장
                if (go_error==11 or go_error==12):
                    canvas.create_rectangle(ras*9.25,ras*6.75,ras*11.75,ras*7.25,fill="white")
                    canvas.create_text(ras*10.5,ras*7,text="new game",font="Verdana 8",justify=CENTER,fill="black")
            else:
                canvas.create_text(ras*10.5,ras*7.5,text="연습",font="Verdana 8",justify=CENTER,fill="grey") # 0.35
                canvas.create_text(ras*10.5,ras*7.85,text=str(zadania[control_memory_mode_i][0]),font="Verdana 8",justify=CENTER,fill="black")
            if (go_error!=11 and go_error!=12):
                # revers_monitor
                canvas.create_rectangle(ras*10.325,ras*7.25,ras*10.825,ras*6.75,fill="white")
                col = "black"
                if (control_revers_monitor==1):
                    col = "grey"
                canvas.create_polygon(ras*10.475,ras*7.15,ras*10.375,ras*7.05,ras*10.43,ras*7.05,ras*10.43,ras*6.85,ras*10.51,ras*6.85,ras*10.51,ras*7.05,ras*10.575,ras*7.05, fill="white", outline=col)
                canvas.create_polygon(ras*10.575,ras*6.95,ras*10.675,ras*6.85,ras*10.775,ras*6.95,ras*10.71,ras*6.95,ras*10.71,ras*7.15,ras*10.63,ras*7.15,ras*10.63,ras*6.95, fill="white", outline=col)
                # revers_monitor_always
                canvas.create_rectangle(ras*9.375,ras*7.25,ras*9.875,ras*6.75,fill="white")
                canvas.create_oval(ras*9.45,ras*7.18,ras*9.8,ras*6.83,fill="white")
                canvas.create_polygon(ras*9.62,ras*7.0,ras*9.5,ras*6.83,ras*10.28,ras*6.83, fill="white", outline="white")
                canvas.create_polygon(ras*9.6,ras*6.95,ras*9.48,ras*6.83,ras*9.6,ras*6.83, fill="white", outline="black")
                
                canvas.create_rectangle(ras*11.625,ras*7.25,ras*11.125,ras*6.75,fill="white")
                canvas.create_polygon(ras*11.225, ras*6.825, ras*11.225, ras*7.175, ras*11.3, ras*7.175, ras*11.3, ras*7, ras*11.45, ras*7, ras*11.45, ras*7.175, ras*11.535, ras*7.175, ras*11.535, ras*6.825, ras*11.45, ras*6.825, ras*11.45, ras*6.95, ras*11.3, ras*6.95, ras*11.3, ras*6.825, fill="white", outline="black")
                
        else:
            # остальные кнопки
            if (control_memory_mode!=5):
                canvas.create_text(ras*10.5,ras*0.35,text="포지셔닝",font="Verdana 8",justify=CENTER,fill="grey")
                canvas.create_text(ras*10.6,ras*0.75,text="흰색 말",font="Verdana 8",justify=CENTER,fill="black") # ras*10.8,ras*0.75,
                canvas.create_text(ras*10.5,ras*1.0,text="흰색 킹",font="Verdana 8",justify=CENTER,fill="black")
                canvas.create_text(ras*10.7,ras*1.25,text="검은색 말",font="Verdana 8",justify=CENTER,fill="black")
                canvas.create_text(ras*10.6,ras*1.5,text="검은색 킹",font="Verdana 8",justify=CENTER,fill="black")
                canvas.create_text(ras*10.5,ras*1.75,text="말 지우기",font="Verdana 8",justify=CENTER,fill="black")
                if (control_add==1):
                    canvas.create_oval(ras*9.35,ras*0.7,ras*9.45,ras*0.8,fill="black", outline="black")
                else:
                    canvas.create_oval(ras*9.35,ras*0.7,ras*9.45,ras*0.8,fill="white", outline="black")
                if (control_add==11):
                    canvas.create_oval(ras*9.35,ras*0.95,ras*9.45,ras*1.05,fill="black", outline="black")
                else:
                    canvas.create_oval(ras*9.35,ras*0.95,ras*9.45,ras*1.05,fill="white", outline="black")
                if (control_add==2):
                    canvas.create_oval(ras*9.35,ras*1.2,ras*9.45,ras*1.3,fill="black", outline="black")
                else:
                    canvas.create_oval(ras*9.35,ras*1.2,ras*9.45,ras*1.3,fill="white", outline="black")
                if (control_add==12):
                    canvas.create_oval(ras*9.35,ras*1.45,ras*9.45,ras*1.55,fill="black", outline="black")
                else:
                    canvas.create_oval(ras*9.35,ras*1.45,ras*9.45,ras*1.55,fill="white", outline="black")
                if (control_add==0):
                    canvas.create_oval(ras*9.35,ras*1.7,ras*9.45,ras*1.8,fill="black", outline="black")
                else:
                    canvas.create_oval(ras*9.35,ras*1.7,ras*9.45,ras*1.8,fill="white", outline="black")
                canvas.create_rectangle(ras*9.25,ras*2.25,ras*11.75,ras*2.75,fill="white")  
                canvas.create_text(ras*10.5,ras*2.5,text="필드를 지우다",font="Verdana 8",justify=CENTER,fill="black")
                #canvas.create_rectangle(ras*9.25,ras*2.05,ras*11.75,ras*2.55,fill="white")  
                #canvas.create_text(ras*10.5,ras*2.3,text="очистить поле",font="Verdana 8",justify=CENTER,fill="black")
            #control_memory_mode = 1 
            if (control_memory_mode==0):
                canvas.create_rectangle(ras*9.25,ras*8.25,ras*11.75,ras*8.75,fill="white")
                canvas.create_text(ras*10.5,ras*8.5,text="플레이",font="Verdana 8",justify=CENTER,fill="black")
                canvas.create_rectangle(ras*9.25,ras*7.75,ras*11.75,ras*8.125,fill="white")
                canvas.create_text(ras*10.5,ras*7.9375,text="기억 작업",font="Verdana 7",justify=CENTER,fill="black")
                if (len(debuts)>1):
                    canvas.create_rectangle(ras*9.25,ras*7.25,ras*11.75,ras*7.625,fill="white")
                    canvas.create_text(ras*10.5,ras*7.4375,text="데뷔",font="Verdana 7",justify=CENTER,fill="black")
                else:
                    canvas.create_rectangle(ras*9.25,ras*7.25,ras*11.75,ras*7.625,fill="white", outline="grey")
                    canvas.create_text(ras*10.5,ras*7.4375,text="데뷔",font="Verdana 7",justify=CENTER,fill="grey")
                if (len(zadania)>1):
                    canvas.create_rectangle(ras*9.25,ras*7.125,ras*11.75,ras*6.75,fill="white")
                    canvas.create_text(ras*10.5,ras*6.9375,text="문제집",font="Verdana 7",justify=CENTER,fill="black")
                else:
                    canvas.create_rectangle(ras*9.25,ras*7.125,ras*11.75,ras*6.75,fill="white", outline="grey")
                    canvas.create_text(ras*10.5,ras*6.9375,text="문제집",font="Verdana 7",justify=CENTER,fill="grey")
                # кнопки - ссылки на браузер
                # 0.375 0.125
                canvas.create_rectangle(ras*11.375,ras*6.25,ras*11.75,ras*6.625,fill="white")
                canvas.create_text(ras*11.5625,ras*6.4375,text="?",font="Verdana 9",justify=CENTER,fill="black")
                #
                canvas.create_rectangle(ras*10.875,ras*6.25,ras*11.25,ras*6.625,fill="white")
                canvas.create_polygon(ras*10.975,ras*6.425,ras*11.15,ras*6.425,ras*11.0625,ras*6.525,fill="black")
                canvas.create_rectangle(ras*10.975,ras*6.525,ras*11.15,ras*6.525,fill="black")
                canvas.create_rectangle(ras*11.05,ras*6.425,ras*11.05,ras*6.325,fill="black")
                #
                canvas.create_rectangle(ras*10.75,ras*6.25,ras*10.375,ras*6.625,fill="white")
                canvas.create_polygon(ras*10.43,ras*6.4,ras*10.52,ras*6.4,ras*10.57,ras*6.3,ras*10.61,ras*6.4,ras*10.7,ras*6.4, ras*10.62,ras*6.45,ras*10.63,ras*6.55, ras*10.57,ras*6.5, ras*10.5,ras*6.55,ras*10.52,ras*6.45,fill="white",outline="black")
                #
                #canvas.create_rectangle(ras*9.875,ras*6.25,ras*10.25,ras*6.625,fill="white") # play recorder history
                #canvas.create_rectangle(ras*9.63,ras*6.25,ras*9.25,ras*6.625,fill="white") # setting
                #
                #canvas.create_text(ras*10.0,ras*2.75,text="уровень сложности",font="Verdana 8",justify=CENTER,fill="black")
                # др. кнопки
                canvas.create_rectangle(ras*9.25,ras*3.0,ras*11.75,ras*3.5,fill="white") 
                canvas.create_text(ras*10.5,ras*3.25,text="새 게임",font="Verdana 8",justify=CENTER,fill="black")
                canvas.create_text(ras*10.5,ras*3.8,text="선공",font="Verdana 8",justify=CENTER,fill="grey")
                canvas.create_text(ras*10.12,ras*4.2,text="화이트",font="Verdana 8",justify=CENTER,fill="black") 
                canvas.create_text(ras*10.2,ras*4.45,text="블랙",font="Verdana 8",justify=CENTER,fill="black")
                if (control_move==1):
                    canvas.create_oval(ras*9.35,ras*4.15,ras*9.45,ras*4.25,fill="black", outline="black")
                else:
                    canvas.create_oval(ras*9.35,ras*4.15,ras*9.45,ras*4.25,fill="white", outline="black")
                if (control_move==2):
                    canvas.create_oval(ras*9.35,ras*4.4,ras*9.45,ras*4.5,fill="black", outline="black")
                else:
                    canvas.create_oval(ras*9.35,ras*4.4,ras*9.45,ras*4.5,fill="white", outline="black")
                canvas.create_text(ras*10.5,ras*4.85,text="게임 모드",font="Verdana 8",justify=CENTER,fill="grey")
                canvas.create_text(ras*10.75,ras*5.25,text="인간-인간",font="Verdana 8",justify=CENTER,fill="black")
                canvas.create_text(ras*10.6,ras*5.5,text="인간-로봇",font="Verdana 8",justify=CENTER,fill="black")
                canvas.create_text(ras*10.62,ras*5.75,text="로봇-인간",font="Verdana 8",justify=CENTER,fill="black")
                # canvas.create_text(ras*10.45,ras*6,text="робот-робот",font="Verdana 8",justify=CENTER,fill="black")
                if (control_vs==3):
                    canvas.create_oval(ras*9.35,ras*5.2,ras*9.45,ras*5.3,fill="black", outline="black")
                else:
                    canvas.create_oval(ras*9.35,ras*5.2,ras*9.45,ras*5.3,fill="white", outline="black")
                if (control_vs==2):
                    canvas.create_oval(ras*9.35,ras*5.45,ras*9.45,ras*5.55,fill="black", outline="black")
                else:
                    canvas.create_oval(ras*9.35,ras*5.45,ras*9.45,ras*5.55,fill="white", outline="black")
                if (control_vs==1):
                    canvas.create_oval(ras*9.35,ras*5.7,ras*9.45,ras*5.8,fill="black", outline="black")
                else:
                    canvas.create_oval(ras*9.35,ras*5.7,ras*9.45,ras*5.8,fill="white", outline="black")
                # if (control_vs==4):
                #     canvas.create_oval(ras*9.35,ras*5.95,ras*9.45,ras*6.05,fill="black", outline="black")
                # else:
                #     canvas.create_oval(ras*9.35,ras*5.95,ras*9.45,ras*6.05,fill="white", outline="black")
            else: # if (control_memory_mode==1 or control_memory_mode==2):
                col = "black"
                if (control_memory_mode==1 or control_memory_mode==3 or control_memory_mode==5):
                    col = "black"
                    canvas.create_rectangle(ras*9.25,ras*8.25,ras*11.75,ras*8.75,fill="white")
                    canvas.create_text(ras*10.5,ras*8.5,text="작업 시작",font="Verdana 7",justify=CENTER,fill="black")
                else:
                    col = "grey"
                    canvas.create_rectangle(ras*9.25,ras*8.25,ras*11.75,ras*8.75,fill="white")
                    canvas.create_text(ras*10.5,ras*8.5,text="작업 제출",font="Verdana 8",justify=CENTER,fill="black")
                if (control_memory_mode<3):   
                    canvas.create_text(ras*10.5,ras*6.35,text="난이도",font="Verdana 8",justify=CENTER,fill="grey")
                elif (control_memory_mode<5):
                    canvas.create_text(ras*10.5,ras*6,text="데뷔",font="Verdana 8",justify=CENTER,fill="grey")
                else:
                    canvas.create_text(ras*10.5,ras*6,text="연습",font="Verdana 8",justify=CENTER,fill="grey")
                if (control_memory_mode==4 or control_memory_mode==3):
                    canvas.create_text(ras*10.5,ras*6.35,text=str(debuts[control_memory_mode_i][0]),font="Verdana 8",justify=CENTER,fill="black") 
                if (control_memory_mode==6 or control_memory_mode==5):
                    canvas.create_text(ras*10.5,ras*6.35,text=str(zadania[control_memory_mode_i][0]),font="Verdana 8",justify=CENTER,fill="black") 
                #canvas.create_rectangle(ras*9.25,ras*6.75,ras*11.75,ras*7.25,fill="white")
                canvas.create_rectangle(ras*10.25,ras*6.75,ras*10.75,ras*7.25,fill="white", outline=col)
                canvas.create_text(ras*10.5,ras*7,text=control_memory_mode_i,font="Verdana 8",justify=CENTER,fill=col)
                #
                canvas.create_polygon(ras*10.9,ras*6.75,ras*10.9,ras*7.25,ras*11.2,ras*7.0, fill="white", outline=col)
                #
                canvas.create_polygon(ras*11.35,ras*6.75,ras*11.35,ras*7.25,ras*11.55,ras*7.0, fill="white", outline=col)
                canvas.create_polygon(ras*11.55,ras*6.75,ras*11.55,ras*7.25,ras*11.75,ras*7.0, fill="white", outline=col)
                #
                canvas.create_polygon(ras*10.1,ras*6.75,ras*10.1,ras*7.25,ras*9.8,ras*7.0, fill="white", outline=col)
                #
                canvas.create_polygon(ras*9.65,ras*6.75,ras*9.65,ras*7.25,ras*9.45,ras*7.0, fill="white", outline=col)
                canvas.create_polygon(ras*9.45,ras*6.75,ras*9.45,ras*7.25,ras*9.25,ras*7.0, fill="white", outline=col)
                #
                canvas.create_rectangle(ras*9.25,ras*7.5,ras*11.75,ras*8.0,fill="white")
                canvas.create_text(ras*10.5,ras*7.75,text="저장",font="Verdana 8",justify=CENTER,fill="black")
                if (control_memory_mode_over>=0):
                    canvas.create_text(ras*10.5,ras*4.6,text="당신의 결과",font="Verdana 8",justify=CENTER,fill="grey")
                    canvas.create_text(ras*10.5,ras*5.0,text=str(int(control_memory_mode_over/control_memory_mode_i*10))+"%",font="Verdana 10",justify=CENTER,fill="black")
                    control_memory_mode_over = -1
                
    
    def reboot_checkers():
        global area_monitor
        area = deepcopy(area_monitor)
        global klik
        global go_color
        global control_vs
        global moved_checkers
        global control_revers_monitor
        global control_revers_monitor_always
        global control_memory_mode
        x = 0 # shaska => damka
        while (x <= 7):
            if (area[0][x] == 1):
                area[0][x] = area[0][x] + 10
            x = x + 1
        x = 0
        while (x <= 7):
            if (area[7][x] == 2):
                area[7][x] = area[7][x] + 10
            x = x + 1
        x = 0
        y = 0
        # make area
        #canvas.create_line(0,0,600,600,width=5,fill="yellow")
        canvas.create_rectangle(0,0,ras*9,ras*9,fill="#feb")
        canvas.create_rectangle(ras*0.5,ras*0.5,ras*8.5,ras*8.5,fill="#feb")
        if ((control_edit==0 or control_memory_mode==6) and control_revers_monitor_result()):
            canvas.create_text(ras*8,ras*0.25,text="a",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*7,ras*0.25,text="b",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*6,ras*0.25,text="c",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*5,ras*0.25,text="d",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*4,ras*0.25,text="e",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*3,ras*0.25,text="f",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*2,ras*0.25,text="g",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*1,ras*0.25,text="h",font="Verdana 10",justify=CENTER,fill="black")
            
            canvas.create_text(ras*8,ras*8.75,text="a",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*7,ras*8.75,text="b",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*6,ras*8.75,text="c",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*5,ras*8.75,text="d",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*4,ras*8.75,text="e",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*3,ras*8.75,text="f",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*2,ras*8.75,text="g",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*1,ras*8.75,text="h",font="Verdana 10",justify=CENTER,fill="black")

            canvas.create_text(ras*0.25,ras*8,text="8",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*0.25,ras*7,text="7",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*0.25,ras*6,text="6",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*0.25,ras*5,text="5",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*0.25,ras*4,text="4",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*0.25,ras*3,text="3",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*0.25,ras*2,text="2",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*0.25,ras*1,text="1",font="Verdana 10",justify=CENTER,fill="black")
            
            canvas.create_text(ras*8.75,ras*8,text="8",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8.75,ras*7,text="7",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8.75,ras*6,text="6",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8.75,ras*5,text="5",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8.75,ras*4,text="4",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8.75,ras*3,text="3",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8.75,ras*2,text="2",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8.75,ras*1,text="1",font="Verdana 10",justify=CENTER,fill="black")

            ii = 0
            while (ii<32): 
                #print(int(ii/8),ii%8,int((63-ii)/8),(63-ii)%8)
                rez = deepcopy(area[int(ii/8)][ii%8])
                area[int(ii/8)][ii%8] = deepcopy(area[int((63-ii)/8)][(63-ii)%8])
                area[int((63-ii)/8)][(63-ii)%8] = deepcopy(rez)
                ii += 1
            moved_checkers = (7-int(moved_checkers/10))*10+(7-moved_checkers%10)
        else:
            #canvas.create_text(ras/4+0*ras,ras/4+1*ras,text="A",font="Verdana 12",justify=CENTER,fill="black")
            canvas.create_text(ras*1,ras*0.25,text="a",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*2,ras*0.25,text="b",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*3,ras*0.25,text="c",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*4,ras*0.25,text="d",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*5,ras*0.25,text="e",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*6,ras*0.25,text="f",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*7,ras*0.25,text="g",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8,ras*0.25,text="h",font="Verdana 10",justify=CENTER,fill="black")
            
            canvas.create_text(ras*1,ras*8.75,text="a",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*2,ras*8.75,text="b",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*3,ras*8.75,text="c",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*4,ras*8.75,text="d",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*5,ras*8.75,text="e",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*6,ras*8.75,text="f",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*7,ras*8.75,text="g",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8,ras*8.75,text="h",font="Verdana 10",justify=CENTER,fill="black")

            canvas.create_text(ras*0.25,ras*1,text="8",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*0.25,ras*2,text="7",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*0.25,ras*3,text="6",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*0.25,ras*4,text="5",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*0.25,ras*5,text="4",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*0.25,ras*6,text="3",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*0.25,ras*7,text="2",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*0.25,ras*8,text="1",font="Verdana 10",justify=CENTER,fill="black")
            
            canvas.create_text(ras*8.75,ras*1,text="8",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8.75,ras*2,text="7",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8.75,ras*3,text="6",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8.75,ras*4,text="5",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8.75,ras*5,text="4",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8.75,ras*6,text="3",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8.75,ras*7,text="2",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_text(ras*8.75,ras*8,text="1",font="Verdana 10",justify=CENTER,fill="black")
        while (y < 8):
            x = 0
            while (x < 8):
                if (area[y][x]!=9):
                    canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2,x*ras+ras/2*3,y*ras+ras/2*3,fill="#c96",outline="#c96")
                    if (area[y][x]!=0 and area[y][x]<100 and 1):
                        wer = 0.05
                        canvas.create_oval([x*ras+ras/2+ras*wer+ras/10,(y-1)*ras+ras/2*3+ras/10+ras*wer],[x*ras+ras/2*3-ras/10+ras*wer,(y-1)*ras+ras/2*5-ras/10+ras*wer],fill="#643", outline="#643")
                        
                x = x + 1
            y = y + 1
        # make checkers
        x = 0
        y = 0
        while (y < 8):
            x = 0
            while (x < 8): 
                if ((area[y][x] != 9) and (area[y][x] != 0)):
                    if (area[y][x]%10==1):
                        if (moved_checkers==y*10+x):
                            canvas.create_oval([x*ras+ras/2+ras/10,(y-1)*ras+ras/2*3+ras/10],[x*ras+ras/2*3-ras/10,(y-1)*ras+ras/2*5-ras/10],fill="white", outline="red")
                        elif (go_color==1):
                            canvas.create_oval([x*ras+ras/2+ras/10,(y-1)*ras+ras/2*3+ras/10],[x*ras+ras/2*3-ras/10,(y-1)*ras+ras/2*5-ras/10],fill="white", outline="white")
                        else:
                            canvas.create_oval([x*ras+ras/2+ras/10,(y-1)*ras+ras/2*3+ras/10],[x*ras+ras/2*3-ras/10,(y-1)*ras+ras/2*5-ras/10],fill="white", outline="white")
                    else:
                        qwe = 10
                        if (moved_checkers==y*10+x):
                            canvas.create_oval([x*ras+ras/2+ras/qwe,(y-1)*ras+ras/2*3+ras/qwe],[x*ras+ras/2*3-ras/qwe,(y-1)*ras+ras/2*5-ras/qwe],fill="black", outline="red")
                        elif (go_color==2):
                            canvas.create_oval([x*ras+ras/2+ras/qwe,(y-1)*ras+ras/2*3+ras/qwe],[x*ras+ras/2*3-ras/qwe,(y-1)*ras+ras/2*5-ras/qwe],fill="black", outline="black")
                        else:
                            canvas.create_oval([x*ras+ras/2+ras/qwe,(y-1)*ras+ras/2*3+ras/qwe],[x*ras+ras/2*3-ras/qwe,(y-1)*ras+ras/2*5-ras/qwe],fill="black", outline="black")
                    if (int(area[y][x]/10)%10 >= 1):
                        if (area[y][x]%10==1):
                            canvas.create_oval([x*ras+ras/2+ras/5,(y-1)*ras+ras/2*3+ras/5],[x*ras+ras/2*3-ras/5,(y-1)*ras+ras/2*5-ras/5],fill="#bb9", outline="#bb9") 
                        else:
                            canvas.create_oval([x*ras+ras/2+ras/5,(y-1)*ras+ras/2*3+ras/5],[x*ras+ras/2*3-ras/5,(y-1)*ras+ras/2*5-ras/5],fill="#555", outline="#555") 
                    else:
                        if (area[y][x]%10==1):
                            canvas.create_oval([x*ras+ras/2+ras/5,(y-1)*ras+ras/2*3+ras/5],[x*ras+ras/2*3-ras/5,(y-1)*ras+ras/2*5-ras/5],fill="white", outline="grey")
                            canvas.create_oval([x*ras+ras/2+ras/3.3,(y-1)*ras+ras/2*3+ras/3.3],[x*ras+ras/2*3-ras/3.3,(y-1)*ras+ras/2*5-ras/3.3],fill="white", outline="grey")
                        else:
                            canvas.create_oval([x*ras+ras/2+ras/5,(y-1)*ras+ras/2*3+ras/5],[x*ras+ras/2*3-ras/5,(y-1)*ras+ras/2*5-ras/5],fill="black", outline="grey")
                            canvas.create_oval([x*ras+ras/2+ras/3.3,(y-1)*ras+ras/2*3+ras/3.3],[x*ras+ras/2*3-ras/3.3,(y-1)*ras+ras/2*5-ras/3.3],fill="black", outline="grey")
                    if (area[y][x]>100):
                        canvas.create_line(x*ras+ras*0.8,y*ras+ras*0.55,x*ras+ras*1.45,y*ras+ras*1.0,width=3,fill="#c96")
                        canvas.create_line(x*ras+ras*0.55,y*ras+ras*1.4,x*ras+ras*1.2,y*ras+ras*0.6,width=5,fill="#c96")
                        canvas.create_line(x*ras+ras*1.5,y*ras+ras*1.2,x*ras+ras*0.5,y*ras+ras*1.4,width=4,fill="#c96")
                x = x + 1
            y = y + 1
            canvas.create_rectangle(ras*0.5,ras*0.5,ras*8.5,ras*8.5,width=2, outline="#c96")
        if ((control_edit==0 or control_memory_mode==6) and control_revers_monitor_result()):
            moved_checkers = (7-int(moved_checkers/10))*10+(7-moved_checkers%10)
        #out_window.update()
    
    def reboot_monitor():
        canvas.delete("all")
        reboot_checkers()
        reboot_controller()
        
    #===================================================================================================================================================================================================
    #===================================================================================================================================================================================================
    #===================================================================================================================================================================================================
    
    def print_go_operation():
        global go_operation

        def print_coo(yy,xx):
            if(1):
                if(1):
                    if  (xx==0):
                        print("a", end='')
                    elif(xx==1):
                        print("b", end='')
                    elif(xx==2):
                        print("c", end='')
                    elif(xx==3):
                        print("d", end='')
                    elif(xx==4):
                        print("e", end='')
                    elif(xx==5):
                        print("f", end='')
                    elif(xx==6):
                        print("g", end='')
                    elif(xx==7):
                        print("h", end='')
                    else:
                        print("error")
                    print(-yy+8, end='')
                    
        if (0): # 1 - выводить (0 - нет)
            i = 0
            while (i < len(go_operation)):
                print(i+1, " ", end='')
                if (0): # непрофессиональный вывод (1 - да, 0 - профессиональный вывод)
                    if (1): # как выводить (1 - с человеческими координатами, 0 - как реально выглядит массив)
                        u = 0
                        while(u < len(go_operation[i])):
                            if (go_operation[i][u]>2000):
                                print("<", end='')
                            if (1): # 1 - выводить (0 - нет) какая шашка
                                asd = int(go_operation[i][u]/100)%100
                                if (asd==1):
                                    print("(wc) ", end='')
                                if (asd==2):
                                    print("(bc) ", end='')
                                if (asd==11):
                                    print("(wl) ", end='')
                                if (asd==12):
                                    print("(bl) ", end='')
                            yy = int(go_operation[i][u]/10)%10
                            xx = go_operation[i][u]%10
                            if  (xx==0):
                                print("a",-yy+8, end='')
                            elif(xx==1):
                                print("b",-yy+8, end='')
                            elif(xx==2):
                                print("c",-yy+8, end='')
                            elif(xx==3):
                                print("d",-yy+8, end='')
                            elif(xx==4):
                                print("e",-yy+8, end='')
                            elif(xx==5):
                                print("f",-yy+8, end='')
                            elif(xx==6):
                                print("g",-yy+8, end='')
                            elif(xx==7):
                                print("h",-yy+8, end='')
                            else:
                                print("error")
                            if (go_operation[i][u]>2000):
                                print(">", end='')
                            if (u+1 < len(go_operation[i])):
                                print(" - ", end='')
                            u = u + 1
                        if (len(go_operation[i])>0):
                            print()
                    else:
                        print(go_operation[i])
                else:
                    y = int(go_operation[i][0]/10)%10
                    x = go_operation[i][0]%10
                    print_coo(y,x)
                    u = len(go_operation[i])
                    if (u>2):
                        print(":", end='')
                    else:
                        print("-", end='')
                    y = int(go_operation[i][u-1]/10)%10
                    x = go_operation[i][u-1]%10
                    print_coo(y,x)
                    print()
                i = i + 1
            print("====================")
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def print_mas(mas):
        i = 0
        while (i<len(mas)):
            print(mas[i])
            i = i + 1

    def print_history():
        global history
        #print_mas(history)
        #print()
        #global area_monitor
        #print_mas(area_monitor)
        #print()
        def print_coo(yy,xx):
            if(1):
                if(1):
                    if  (xx==0):
                        print("a", end='')
                    elif(xx==1):
                        print("b", end='')
                    elif(xx==2):
                        print("c", end='')
                    elif(xx==3):
                        print("d", end='')
                    elif(xx==4):
                        print("e", end='')
                    elif(xx==5):
                        print("f", end='')
                    elif(xx==6):
                        print("g", end='')
                    elif(xx==7):
                        print("h", end='')
                    else:
                        print("error")
                    print(-yy+8, end='')

        def print_field(ch, area):
            i = 0
            x = 0
            y = 0
            while (y<=7):
                if (area[y][x]==ch):
                    if (i==0):
                        if (ch==1):
                            print("white checker:")
                        if (ch==2):
                            print("black checker:")
                        if (ch==11):
                            print("white lady:")
                        if (ch==12):
                            print("black lady:")
                    if (i==6):
                        print()
                    print_coo(y,x)
                    print(" ", end='')
                    i = i + 1
                if (x<7):
                    x = x + 1
                else:
                    y = y + 1
                    x = 0
            if(i>0):
                print()
        
        if (0): # 1 - выводить (0 - нет)
            print("===> history game:")
            print("===> start field:")
            x = 0
            y = 0
            area = deepcopy(history[0])
            print_field(1,  area)
            print_field(11, area)
            print_field(2,  area)
            print_field(12, area)
            while (y<=7 and 0):
                if (area[y][x]==0):
                    print("-- ", end='')
                elif (area[y][x]==9):
                    print("** ", end='')
                elif (area[y][x]==1):
                    print("wc ", end='')
                elif (area[y][x]==2):
                    print("bc ", end='')
                elif (area[y][x]==11):
                    print("wl ", end='')
                elif (area[y][x]==12):
                    print("bl ", end='')
                x = x + 1
                if (x>7):
                    print()
                    x = 0
                    y = y + 1
            print("===> moves:")
            i = 1
            if (0): # непрофессиональный вывод (1 - да, 0 - профессиональный вывод)
                while (i < len(history)):
                    print(i, " ", end='')
                    if (1): # как выводить (1 - с человеческими координатами, 0 - как реально выглядит массив)
                        u = 0
                        while(u < len(history[i])):
                            if (history[i][u]>2000):
                                print("<", end='')
                            if (1): # 1 - выводить (0 - нет) какая шашка
                                asd = int(history[i][u]/100)%100
                                if (asd==1):
                                    print("(wc) ", end='')
                                if (asd==2):
                                    print("(bc) ", end='')
                                if (asd==11):
                                    print("(wl) ", end='')
                                if (asd==12):
                                    print("(bl) ", end='')
                            yy = int(history[i][u]/10)%10
                            xx = history[i][u]%10
                            print_coo(yy,xx)
                            if (history[i][u]>2000):
                                print(">", end='')
                            if (u+1 < len(history[i])):
                                print(" - ", end='')
                            u = u + 1
                        if (len(history[i])>0):
                            print()
                    else:
                        print(go_operation[i])
                    i = i + 1
            else:
                while (i < len(history)):
                    print(int(i/2)+1, " ", end='')
                    if (int(history[i][0]/100)%10==1):
                        y = int(history[i][0]/10)%10
                        x = history[i][0]%10
                        print_coo(y,x)
                        u = len(history[i])
                        if (u>2):
                            print(":", end='')
                        else:
                            print("-", end='')
                        y = int(history[i][u-1]/10)%10
                        x = history[i][u-1]%10
                        print_coo(y,x)
                        i = i + 1
                    else:
                        print(".....", end='')
                    print(" ", end='')
                    if (i<len(history)):
                        if (int(history[i][0]/100)%10==2):
                            y = int(history[i][0]/10)%10
                            x = history[i][0]%10
                            print_coo(y,x)
                            u = len(history[i])
                            if (u>2):
                                print(":", end='')
                            else:
                                print("-", end='')
                            y = int(history[i][u-1]/10)%10
                            x = history[i][u-1]%10
                            print_coo(y,x)
                        else:
                           print(".....", end='') 
                    else:
                        print(".....", end='')
                    print()
                    i = i + 1
            print("====================")
    
    def move(y0, x0, y1, x1, c):
        global area_monitor
        area_monitor[y0][x0] = 0
        x0 = x0 + znak(x1-x0)
        y0 = y0 + znak(y1-y0)
        while (x1!=x0):
            if (area_monitor[y0][x0]!=0):
                area_monitor[y0][x0] = area_monitor[y0][x0] + 500 # corpse
            x0 = x0 + znak(x1-x0)
            y0 = y0 + znak(y1-y0)
        area_monitor[y1][x1] = c
        reboot_monitor()
        out_window.update()

    def clear_corpse():
        reboot_checkers()
        reboot_controller()
        global area_monitor
        x = 0
        y = 0
        eat = 0
        while (y<=7):
            if(area_monitor[y][x]>100):
                area_monitor[y][x] = 0
                eat = 1
            x = x + 1
            if (x>7):
                y = y + 1
                x = 0
        if (eat==1):
            sleep(0.5)
            reboot_checkers()
            reboot_controller()

    def no_wins(go_color):
        global go_operation
        flag = 1
        if (len(go_operation)==0):
            flag = 0
        return flag

    def wins(go_color):
        global go_operation
        if (len(go_operation)==0):
            if (go_color==1):
                canvas.create_text(4.5*ras,4.5*ras,text="black wins!",font="Verdana 52",justify=CENTER,fill="blue")
            else:
                canvas.create_text(4.5*ras,4.5*ras,text="white wins!",font="Verdana 52",justify=CENTER,fill="blue")
            out_window.update()
        
    #===================================================================================================================================================================================================
    #===================================================================================================================================================================================================
    #===================================================================================================================================================================================================

    def more_color(go_color):
        if (go_color==1):
            return 2
        elif (go_color==2):
            return 1
        else:
            return 0
    
    def mozg_random():
        global area_monitor
        global go_color
        global go_operation
        global go_error
        global history
        global level_hard
        #print("11", go_operation)
        go_operation = deepcopy(generator_move(area_monitor, go_color))
        #print(history)
        if (no_wins(go_color)):
            #print(evklid(area_monitor, go_color))
            if (1): #######################################################################################
                #nostardamus(go_color)
                #level_hard = 1
                go_operation = deepcopy(BARS_mind(area_monitor, go_color, level_hard))
            else: # my random brain (мозг)
                go_operation = deepcopy(generator_move(area_monitor, go_color))
                l = randint(0, len(go_operation)-1)
                go_operation = deepcopy(go_operation[l])
            i = 1
            go_error = 0
            #l = randint(0, len(go_operation)-1)
            history.append(go_operation)
            #print("=", go_operation[l])
            while (len(go_operation)-1>=i):
                into = go_operation[i-1]
                y0 = int(into/10)%10
                x0 = into%10
                if (go_operation[i]>2000):
                    i = i + 1
                into = go_operation[i]
                y1 = int(into/10)%10
                x1 = into%10
                ch = int(into/100)%100
                sleep(0.5)
                move(y0, x0, y1, x1, ch)
                i = i + 1
            
            clear_corpse()
        else:
            if (go_color==1):
                go_error = 12
            else:
                go_error = 11
            go_color = -1
            reboot_checkers()
            reboot_controller()
            out_window.update()
            print_history()
        #go_operation = deepcopy(generator_move(area_monitor, go_color))
        #print("12", go_operation)
            
    
    def mozg():
        global go_color
        global go_error
        global go_operation
        go_error = 9
        reboot_controller()
        out_window.update()
        reboot_checkers()
        reboot_controller()
        out_window.update()
        #print("1", evklid(area_monitor, go_color))
        if (go_color!=-1):
            mozg_random()
            if (go_color!=-1): # no_wins(go_color)
                if (go_color==1):
                    go_color = 2
                else:
                    go_color = 1
                go_operation = deepcopy(generator_move(area_monitor, go_color))
                if (no_wins(go_color)==0):
                    if (go_color==1):
                        go_error = 12
                    else:
                        go_error = 11
                    go_color = -1
                    reboot_checkers()
                    reboot_controller()
                    out_window.update()
                    print_history()
                else:
                    print_go_operation()
            if (go_error==9):
                go_error = 0
            reboot_checkers()
            reboot_controller()
        #print("2", evklid(area_monitor, go_color))

    #===================================================================================================================================================================================================
    #===================================================================================================================================================================================================
    #===================================================================================================================================================================================================

    def people_move(y,x):
        global history
        global go_operation
        global area_monitor
        global go_color
        global klik
        global go_error
        global moved_checkers
        global control_memory_mode
        global control_revers_monitor
        global control_revers_monitor_always
        kostil = 0
        print("my")
        if (klik[0][0]==-1 and area_monitor[y][x]!=9 and area_monitor[y][x]!=0): # взять шашку
            if (area_monitor[y][x]%10==go_color):
                klik[0][0] = x
                klik[0][1] = y
                #if ((control_vs==1 or go_color==2 and control_vs==3) and control_edit==0 and control_revers_monitor==1):
                #    x = 7 - x
                #    y = 7 - y
                moved_checkers = y*10+x
                #if ((control_vs==1 or go_color==2 and control_vs==3) and control_edit==0 and control_revers_monitor==1):
                #    x = 7 - x
                #    y = 7 - y
                go_error = 0
            else:
                go_error = 3
        elif (klik[0][0]!=-1 and klik[1][0]==-1 and klik[0][0]==x and klik[0][1]==y): # если никуда не ходили при необходимости отпустить
            klik[0][0] = -1
            klik[0][1] = -1
            moved_checkers = -1
            go_error = 0
        elif (klik[0][0]!=-1 and klik[1][0]==-1 and area_monitor[y][x]%10==go_color): # если никуда не ходили при необходимости смешить шашку
            klik[0][0] = x
            klik[0][1] = y
            #if ((control_vs==1 or go_color==2 and control_vs==3) and control_edit==0 and control_revers_monitor==1):
            #    x = 7 - x
            #    y = 7 - y
            moved_checkers = y*10+x
            #if ((control_vs==1 or go_color==2 and control_vs==3) and control_edit==0 and control_revers_monitor==1):
            #    x = 7 - x
            #    y = 7 - y
            go_error = 0
        elif ((klik[0][0] != -1) and (area_monitor[y][x] != 9) and (area_monitor[y][x] == 0)): # если все-таки ходим
            flag = 0
            i = 0
            l = 0
            g = 0
            gg = 0
            while (klik[gg][0]!=-1 and gg<len(klik)):
                gg = gg + 1
            klik[gg][0] = x
            klik[gg][1] = y
            gg = gg + 1
            ch = 0
            eat = 0
            while (l<len(go_operation) and flag==0):
                i = 0
                g = 0
                flag = 1
                while (i<len(go_operation[l]) and g<gg): #  and flag==0
                    if (go_operation[l][i]>2000):
                        i = i + 1
                        eat = 1
                    if (go_operation[l][i]%100!=klik[g][1]*10+klik[g][0]):
                        flag = 0
                    else:
                        ch = int(go_operation[l][i]/100)%100
                    g = g + 1
                    i = i + 1
                l = l + 1
            l = l - 1
            if (flag==1):
                #print("yes")
                move(klik[gg-2][1],klik[gg-2][0],klik[gg-1][1],klik[gg-1][0],ch)
                #klik.append([-1,-1])
                if (i<len(go_operation[l])): # продолжаем ходить
                    #if ((control_vs==1 or go_color==2 and control_vs==3) and control_edit==0):
                    #    moved_checkers = (7-klik[gg-1][1])*10+7-klik[gg-1][0]
                    #else:
                    #    moved_checkers = klik[gg-1][1]*10+klik[gg-1][0]
                    moved_checkers = klik[gg-1][1]*10+klik[gg-1][0]
                    klik.append([-1,-1])
                else: # конец хода, смена цвета
                    #print("--",go_operation[l])
                    #if (control_revers_monitor_result()):
                    #    sleep(0.5)
                    control_revers_monitor_always = 0
                    if (control_memory_mode==6): # and control_revers_monitor==1
                        sleep(0.5)
                    history.append(go_operation[l])
                    moved_checkers = -1
                    klik.clear()
                    klik = [[-1,-1],[-1,-1]]
                    if (go_color == 1):
                        if (control_vs==3):
                            kostil = 1
                        go_color = 2
                    else:
                        if (control_vs==3):
                            kostil = 1
                        go_color = 1
                    clear_corpse()
                    go_operation = deepcopy(generator_move(area_monitor, go_color))
                    print_go_operation()
                go_error = 0
            else:
                #moved_checkers = -1
                klik[gg-1][0] = -1
                klik[gg-1][1] = -1
                if (eat==1):
                    go_error = 1
                else:
                    go_error = 2
        else:
            go_error = 2
        if (no_wins(go_color)==0):
            if (go_color==1):
                go_error = 12
            else:
                go_error = 11
            go_color = -1
            reboot_checkers()
            reboot_controller()
            out_window.update()
            print_history()
        reboot_checkers()
        reboot_controller()
        if (kostil==1 and control_memory_mode==0):
            sleep(0.5)
        #wins(go_color)

    def craft_task_memory():
        global control_memory_mode 
        global control_memory_mode_i
        global control_memory_mode_over
        global area_monitor
        global area_zero2
        global history
        #print("craft_task_memory")
        area_monitor = deepcopy(area_zero2)
        i = 0
        while (i<control_memory_mode_i):
            x = randint(0, 7)
            y = randint(0, 7)
            if (area_monitor[y][x]==0):
                i = i + 1
                c = randint(1, 4)
                if (c==3):
                    c = 11
                if (c==4):
                    c = 12
                area_monitor[y][x] = c
        x = 0 # shaska => damka
        while (x <= 7):
            if (area_monitor[0][x] == 1):
                area_monitor[0][x] = area_monitor[0][x] + 10
            x = x + 1
        x = 0
        while (x <= 7):
            if (area_monitor[7][x] == 2):
                area_monitor[7][x] = area_monitor[7][x] + 10
            x = x + 1
        history.clear()
        history = deepcopy(area_monitor)
        reboot_monitor()
        out_window.update()
        t = millis()
        while (t+control_memory_mode_i*1000>millis()):
            canvas.create_rectangle(ras*10.2,ras*4.4,ras*10.8,ras*4.8,fill="white", outline="white")
            ttt = int((t+control_memory_mode_i*1000-millis())/1000)+1
            if (ttt>control_memory_mode_i):
                ttt = control_memory_mode_i
            canvas.create_text(ras*10.5,ras*4.6,text=ttt,font="Verdana 8",justify=CENTER,fill="grey")
            sleep(0.1)
            out_window.update()
        #sleep(control_memory_mode_i) # 
        area_monitor = deepcopy(area_zero2)

    def craft_task_memory2():
        global control_memory_mode 
        global control_memory_mode_i
        global control_memory_mode_over
        global area_monitor
        global area_zero2
        global history
        global debuts
        #print("craft_task_memory")
        area_monitor = deepcopy(debuts[control_memory_mode_i][1])
        #print(area_monitor)
        x = 0 # shaska => damka
        while (x <= 7):
            if (area_monitor[0][x] == 1):
                area_monitor[0][x] = area_monitor[0][x] + 10
            x = x + 1
        x = 0
        while (x <= 7):
            if (area_monitor[7][x] == 2):
                area_monitor[7][x] = area_monitor[7][x] + 10
            x = x + 1
        history.clear()
        history = deepcopy(area_monitor)
        reboot_monitor()
        out_window.update()
        x = 0
        y = 0
        qwer = control_memory_mode_i
        control_memory_mode_i = 5 # 0
        #while (y<=7):
        #    if (history[y][x]>0 and history[y][x]!=9):
        #        control_memory_mode_i = control_memory_mode_i + 1
        #    if (x<7):
        #        x = x + 1
        #    else:
        #        y = y + 1
        #        x = 0
        t = millis()
        while (t+control_memory_mode_i*1000>millis() and 1):
            canvas.create_rectangle(ras*10.2,ras*4.4,ras*10.8,ras*4.8,fill="white", outline="white")
            ttt = int((t+control_memory_mode_i*1000-millis())/1000)+1
            if (ttt>control_memory_mode_i):
                ttt = control_memory_mode_i
            canvas.create_text(ras*10.5,ras*4.6,text=ttt,font="Verdana 8",justify=CENTER,fill="grey")
            sleep(0.1)
            out_window.update()
        #sleep(control_memory_mode_i) #
        control_memory_mode_i = qwer
        area_monitor = deepcopy(area_zero2)

    def craft_task_memory3():
        global control_memory_mode 
        global control_memory_mode_i
        global control_memory_mode_over
        global area_monitor
        global area_zero2
        global history
        global zadania
        global go_color
        global control_edit
        global go_operation
        area_monitor = deepcopy(zadania[control_memory_mode_i][1])
        control_edit = 1
        #print(int(zadania[control_memory_mode_i][2][0][0]/100)%10)
        go_color = int(zadania[control_memory_mode_i][2][0][0]/100)%10
        history.clear()
        history.append(deepcopy(area_monitor))
        go_operation = deepcopy(generator_move(area_monitor, go_color))

    def test_task_memory():
        global control_memory_mode 
        global control_memory_mode_i
        global control_memory_mode_over
        global area_monitor
        global history
        #print("test_task_memory")
        x = 0
        y = 0
        i = 0
        while (y<=7):
            if (area_monitor[y][x]!=0 and area_monitor[y][x]!=9):
                if (history[y][x]==0):
                    i = i - 3
                elif (area_monitor[y][x]==history[y][x]):
                    i = i + 10
                elif(area_monitor[y][x]%10==history[y][x]%10):
                    i = i + 5
                elif(int(area_monitor[y][x]/10)==int(history[y][x]/10)):
                    i = i + 2
                else:
                    i = i + 1
                
            if (x<7):
                x = x + 1
            else:
                y = y + 1
                x = 0
        if (i<0):
            i = 0
        if (i<control_memory_mode_i*10): # сделать демонстрацию по необходимости
            mas = deepcopy(area_monitor)
            ii = 0
            while(ii<3):
                area_monitor = deepcopy(history)
                reboot_monitor()
                out_window.update()
                sleep(1)
                area_monitor = deepcopy(mas)
                reboot_monitor()
                out_window.update()
                sleep(1)
                ii = ii + 1
        history.clear()
        control_memory_mode_over = i
        #print(i)

    def test_task_memory2():
        global control_memory_mode
        global control_memory_mode_over
        global area_monitor
        global control_memory_mode_i
        global history
        #print("test_task_memory")
        x = 0
        y = 0
        control_memory_mode_i2 = 0
        while (y<=7):
            if (history[y][x]>0 and history[y][x]!=9):
                control_memory_mode_i2 = control_memory_mode_i2 + 1
            if (x<7):
                x = x + 1
            else:
                y = y + 1
                x = 0
        x = 0
        y = 0
        i = 0
        while (y<=7):
            if (area_monitor[y][x]!=0 and area_monitor[y][x]!=9):
                if (history[y][x]==0):
                    i = i - 3
                elif (area_monitor[y][x]==history[y][x]):
                    i = i + 10
                elif(area_monitor[y][x]%10==history[y][x]%10):
                    i = i + 5
                elif(int(area_monitor[y][x]/10)==int(history[y][x]/10)):
                    i = i + 2
                else:
                    i = i + 1
                
            if (x<7):
                x = x + 1
            else:
                y = y + 1
                x = 0
        if (i<0):
            i = 0
        if (i<control_memory_mode_i2*10): # сделать демонстрацию по необходимости
            mas = deepcopy(area_monitor)
            ii = 0
            while(ii<3):
                area_monitor = deepcopy(history)
                reboot_monitor()
                out_window.update()
                sleep(1)
                area_monitor = deepcopy(mas)
                reboot_monitor()
                out_window.update()
                sleep(1)
                ii = ii + 1
        history.clear()
        #control_memory_mode_over = i
        #print(control_memory_mode_i, control_memory_mode_i2, i)
        control_memory_mode_over = i*control_memory_mode_i/control_memory_mode_i2 #map(i, 0, control_memory_mode_i, )
        #print(i)

    def test_task_memory3():
        global control_memory_mode_i
        global history
        global zadania
        global go_error
        mas_z = deepcopy(zadania[control_memory_mode_i][2])
        mas_h = deepcopy(history)
        del mas_h[0]
        #print(mas_h)
        #print(mas_z)
        #print()
        if (mas_h==mas_z):
            go_error = 5
        elif (len(mas_h)<=len(mas_z)):
            i = len(mas_h)-1
            ii = 0
            while (i<len(mas_z)-1):
                del mas_z[i+1]
                ii = 1
            #print(mas_z)
            if (mas_h!=mas_z):
                back()
                go_error = 4
            #elif (mas_h==mas_z and ii==0):
            #    sleep(0.5)
        

    def back():
        global klik
        global go_color
        global go_error
        global control_move
        global control_vs
        global moved_checkers
        global history
        global area_monitor
        global go_operation
        qwe = go_color
        go_color_kostil = int(history[len(history)-1][0]/100)%10
        if (control_vs!=3):
            go_color_kostil = more_color(go_color_kostil)
            
        if (len(history)>1):
            qwe = deepcopy(history[len(history)-1][0])
            qwe = int(qwe/100)
            qwe = qwe%10
            qwe1 = 0
            #print(qwe)
        if (klik[1][0]==-1):
            moved_checkers = -1
            #print("go back")
            mov1 = deepcopy(history[len(history)-1])
            del history[len(history)-1]
            i = len(mov1)-2
            while (i>=0):
                into = mov1[i+1]
                y0 = int(into/10)%10
                x0 = into%10
                ea = 0
                if (mov1[i]>2000):
                    i = i - 1
                    ea = 1
                into = mov1[i]
                y1 = int(into/10)%10
                x1 = into%10
                ch = int(into/100)%100
                sleep(0.2)
                move(y0, x0, y1, x1, ch)
                if (ea==1):
                    into = mov1[i+1]
                    ye = int(into/10)%10
                    xe = into%10
                    che = int(into/100)%100
                    area_monitor[ye][xe] = che
                i = i - 1
            if (control_vs!=3 and go_error<10 or qwe==control_vs):
                if (qwe==1):
                    qwe = 2
                else:
                    qwe = 1
                mov1 = deepcopy(history[len(history)-1])
                del history[len(history)-1]
                i = len(mov1)-2
                while (i>=0):
                    into = mov1[i+1]
                    y0 = int(into/10)%10
                    x0 = into%10
                    ea = 0
                    if (mov1[i]>2000):
                        i = i - 1
                        ea = 1
                    into = mov1[i]
                    y1 = int(into/10)%10
                    x1 = into%10
                    ch = int(into/100)%100
                    sleep(0.2)
                    move(y0, x0, y1, x1, ch)
                    if (ea==1):
                        into = mov1[i+1]
                        ye = int(into/10)%10
                        xe = into%10
                        che = int(into/100)%100
                        area_monitor[ye][xe] = che
                    i = i - 1
                if (go_color==-1):
                    if (control_vs==1):
                        go_color = 2
                    else:
                        go_color = 1
        else:
            moved_checkers = -1
            flag = 0
            i = 0
            l = 0
            g = 0
            gg = 0
            while (klik[gg][0]!=-1 and gg<len(klik)):
                gg = gg + 1
            ch = 0
            eat = 0
            while (l<len(go_operation) and flag==0):
                i = 0
                g = 0
                flag = 1
                while (i<len(go_operation[l]) and g<gg): #  and flag==0
                    if (go_operation[l][i]>2000):
                        i = i + 1
                        eat = 1
                    if (go_operation[l][i]%100!=klik[g][1]*10+klik[g][0]):
                        flag = 0
                    else:
                        ch = int(go_operation[l][i]/100)%100
                    g = g + 1
                    i = i + 1
                l = l + 1
            l = l - 1
            mov1 = []
            iii = 0
            while (iii<i):
                mov1.append(go_operation[l][iii])
                iii = iii + 1
            i = len(mov1)-2
            while (i>=0):
                into = mov1[i+1]
                y0 = int(into/10)%10
                x0 = into%10
                ea = 0
                if (mov1[i]>2000):
                    i = i - 1
                    ea = 1
                into = mov1[i]
                y1 = int(into/10)%10
                x1 = into%10
                ch = int(into/100)%100
                sleep(0.2)
                move(y0, x0, y1, x1, ch)
                if (ea==1):
                    into = mov1[i+1]
                    ye = int(into/10)%10
                    xe = into%10
                    che = int(into/100)%100
                    area_monitor[ye][xe] = che
                i = i - 1
        if   (control_vs==1):
            go_color = 2
        elif (control_vs==2):
            go_color = 1
        elif (klik[1][0]>-1):
            go_color = area_monitor[klik[0][1]][klik[0][0]]%10
        else:
            go_color = qwe
        go_error = 0
        klik = [[-1,-1],[-1,-1]]
        reboot_checkers()
        go_color = go_color_kostil # костыль
        go_operation = deepcopy(generator_move(area_monitor, go_color))
        print_go_operation()


    
    
    def click1(event):
        global area_monitor
        global klik
        global klik_flag
        global go_color
        global go_error
        global control_memory_mode 
        global control_memory_mode_i
        global control_memory_mode_over
        global control_move
        global control_add
        global control_edit
        global control_vs
        global control_back
        global area_zero
        global area_zero2
        global moved_checkers
        global control_protocol
        global control_protocol_flag
        global control_actions
        global control_actions_flag
        global control_revers_monitor
        global control_revers_monitor_always
        global go_operation
        global debuts
        global zadania
        if (klik_flag==1):
            klik_flag = 0
            x = event.x
            y = event.y
            #area = area_monitor
            #print(x, y)
            if ((x >= ras/2) and (x <= ras/2*17) and (y >= ras/2) and (y <= ras/2*17)): 
                x = map(x, ras/2, ras/2*17, 0, 8)
                y = map(y, ras/2, ras/2*17, 0, 8)
                #print(x, y)
                if (control_edit==0):
                    if (control_vs==1 and go_color==2 or control_vs==2 and go_color==1 or control_vs==3):
                        if (control_revers_monitor_result()):
                            x = 7 - x
                            y = 7 - y
                        people_move(y,x)
                        if (control_revers_monitor_result()):
                            x = 7 - x
                            y = 7 - y
                        if (control_vs==go_color or control_vs==4):
                            control_revers_monitor_always = 0
                            if (len(history)>1): # какая-то параша, чтобы виджеты обновлялись сразу
                                control_protocol.clear()
                                control_protocol_flag = len(history) - 1
                                i = 0
                                while (i<21 and control_protocol_flag>1):
                                    i = i + 1
                                    control_protocol_flag = control_protocol_flag - 1
                                #print(">",control_protocol_flag,len(history) - 1)
                                if (int(history[control_protocol_flag][0]/100)%10==2 and control_protocol_flag>1):
                                    control_protocol_flag = control_protocol_flag + 1
                                craft_protocol(control_protocol_flag,len(history) - 1)
                            else:
                                control_protocol.clear()
                                control_protocol_flag = 0
                            #control_protocol.clear()
                            control_actions.clear()
                            mozg()
                    else:
                        go_error = 3
                        reboot_controller()
                elif (control_memory_mode==6): # для "игры" в режиме задачника
                    if (control_revers_monitor_result()):
                        x = 7 - x
                        y = 7 - y
                    people_move(y,x)
                    if (control_revers_monitor_result()):
                        x = 7 - x
                        y = 7 - y
                    test_task_memory3()
                    #print(history)
                elif (area_monitor[y][x]!=9 and control_memory_mode!=5): # штука контролирующая добавление шашек на поле (нажатия на поле)
                    control_revers_monitor = 0
                    if (y==7 and control_add==2):
                        control_add = 12
                    if (y==0 and control_add==1):
                        control_add = 11
                    if (area_monitor[y][x]!=control_add):
                        area_monitor[y][x] = control_add
                    elif (area_monitor[y][x]/10<1 and area_monitor[y][x]!=0):
                        area_monitor[y][x] = area_monitor[y][x] + 10
                    elif (area_monitor[y][x]==11):
                        area_monitor[y][x] = 2
                    else:
                        area_monitor[y][x] = 1
                    control_add = area_monitor[y][x]
                    if (y==7 and control_add==2):
                        control_add = 12
                    if (y==0 and control_add==1):
                        control_add = 11
            else:
                if ((y>=ras*8.25 and y<=ras*8.75 and x>=ras*10.625 and x<=ras*11.75 and control_edit==0 or y>=ras*8.25 and y<=ras*8.75 and x>=ras*9.25 and x<=ras*11.75 and control_edit==1) and control_memory_mode==0):
                    # обработка входа выхода в меню
                    xx = 0
                    yy = 0
                    while (yy<=7):
                        if (area_monitor[yy][xx]>=500):
                            area_monitor[yy][xx] -= 500
                        if (xx<7):
                            xx += 1
                        else:
                            xx = 0
                            yy += 1
                    klik.clear()
                    klik = [[-1,-1],[-1,-1]]
                    moved_checkers = -1
                    control_edit_checkers = [-1,-1,0]
                    go_error = 0
                    if (control_edit==1):
                        print("hi")
                        control_edit = 0
                        go_color = control_move
                        history.clear()
                        history.append(deepcopy(area_monitor))
                        go_operation = deepcopy(generator_move(area_monitor, go_color))
                        print_go_operation()
                        if (go_color==control_vs or control_vs==4): # 헬퍼 클릭시 이쪽 코드 실행
                            mozg()
                    else:
                        control_edit = 1
                        control_move = go_color
                        if (control_move==-1):
                            control_move = 1
                        go_color = -1
                    control_revers_monitor = 0
                    control_revers_monitor_always = 0
                #canvas.create_rectangle(ras*9.875,ras*7.25,ras*10.375,ras*6.75,fill="white")
                elif (x>=ras*10.325 and y<=ras*7.25 and x<=ras*10.825 and y>=ras*6.75 and (control_edit==0 or control_memory_mode==6) and go_error!=11 and go_error!=12): 
                    if (control_revers_monitor==1):
                        control_revers_monitor = 0
                    else:
                        control_revers_monitor = 1
                elif (x>=ras*9.375 and y<=ras*7.25 and x<=ras*9.875 and y>=ras*6.75 and (control_edit==0 or control_memory_mode==6) and go_error!=11 and go_error!=12): 
                    if (control_revers_monitor_always==1):
                        control_revers_monitor_always = 0
                    else:
                        control_revers_monitor_always = 1
                    #print(control_revers_monitor_always)
                    #reboot_monitor()
                elif (x>=ras*11.125 and y<=ras*7.25 and x<=ras*11.625 and y>=ras*6.75):
                    control_vs = 4
                    if(control_vs == 4) :
                        mozg()
                        mozg()
                        reboot_checkers()
                        reboot_controller()
                        go_operation = deepcopy(generator_move(area_monitor, go_color))
                        print_go_operation()
                        control_vs = 2
                    

                elif (y>=ras*8.25 and y<=ras*8.75 and x>=ras*10.625 and x<=ras*11.75 and control_memory_mode==6):
                    xx = 0
                    yy = 0
                    while (yy<=7):
                        if (area_monitor[yy][xx]>=500):
                            area_monitor[yy][xx] -= 500
                        if (xx<7):
                            xx += 1
                        else:
                            xx = 0
                            yy += 1
                    control_memory_mode = 5
                    control_edit = 1
                    klik.clear()
                    klik = [[-1,-1],[-1,-1]]
                    moved_checkers = -1
                    control_edit_checkers = [-1,-1,0]
                    go_error = 0
                    history.clear()
                    history.append(deepcopy(area_monitor))
                elif (control_edit==0 or control_memory_mode==6):
                    if (y>=ras*8.25 and y<=ras*8.75 and x>=ras*9.25 and x<=ras*10.375 and control_back==1):
                        back() # отменить ход
                    # for special version
                    if (x>=ras*9.25 and x<=ras*11.75 and y>=ras*7.5 and y<=ras*8.0 and control_memory_mode!=6):
                        go_error = 0
                        area_monitor = deepcopy(area_zero)
                        control_move = 1
                        go_color = 1
                        history.clear()
                        history.append(deepcopy(area_monitor))
                        klik.clear()
                        klik = [[-1,-1],[-1,-1]]
                        moved_checkers = -1
                        go_operation = deepcopy(generator_move(area_monitor, go_color))
                        msgbox.showinfo("알림", "당신은 화이트 선입니다")
                        # canvas.create_rectangle(ras*9.25,ras*7.5,ras*11.75,ras*8.0,fill="white", outline="grey")
                        # canvas.create_text(ras*10.5,ras*7.75,text="сохранить протокол",font="Verdana 8",justify=CENTER,fill="grey")
                        # out_window.update()
                        # print_file()
                        # sleep(0.1)
                        #print("------------------------------------")

                    # новая игра не входя в меню
                    if (x>=ras*9.25 and y>=ras*6.75 and x<=ras*11.75 and y<=ras*7.25 and (go_error==11 or go_error==12)):
                        # 이 부분 새게임 세팅인것으로 파악돼서 시작하기 버튼에 이거 넣어놨습니다
                        go_error = 0
                        area_monitor = deepcopy(area_zero)
                        control_move = 1
                        go_color = 1
                        history.clear()
                        history.append(deepcopy(area_monitor))
                        klik.clear()
                        klik = [[-1,-1],[-1,-1]]
                        moved_checkers = -1
                        go_operation = deepcopy(generator_move(area_monitor, go_color))
                        if (control_vs==go_color or control_vs==4):
                            if (len(history)>1): # какая-то параша, чтобы виджеты обновлялись сразу
                                control_protocol.clear()
                                control_protocol_flag = len(history) - 1
                                i = 0
                                while (i<21 and control_protocol_flag>1):
                                    i = i + 1
                                    control_protocol_flag = control_protocol_flag - 1
                                #print(">",control_protocol_flag,len(history) - 1)
                                if (int(history[control_protocol_flag][0]/100)%10==2 and control_protocol_flag>1):
                                    control_protocol_flag = control_protocol_flag + 1
                                craft_protocol(control_protocol_flag,len(history) - 1)
                            else:
                                control_protocol.clear()
                                control_protocol_flag = 0
                            #control_protocol.clear()
                            control_actions.clear()
                            mozg()
                        
                else:
                    if (x>=ras*9.25 and x<=ras*11.75):
                        if (control_memory_mode!=5):
                            # еще кнопочки
                            # большие
                            if (y>=ras*2.25 and y<=ras*2.75):  # 필드 지우기
                                area_monitor = deepcopy(area_zero2)
                            # add
                            if (y>=ras*0.625 and y<=ras*0.875):
                                control_add = 1
                            if (y>=ras*0.875 and y<=ras*1.125):
                                control_add = 11
                            if (y>=ras*1.125 and y<=ras*1.375):
                                control_add = 2
                            if (y>=ras*1.375 and y<=ras*1.625):
                                control_add = 12
                            if (y>=ras*1.625 and y<=ras*1.875):
                                control_add = 0
                        if (control_memory_mode==0): # режим для развития памяти
                            # ссылка на скачивание
                            # if (x>=ras*10.875 and y>=ras*6.25 and x<=ras*11.25 and y<=ras*6.625):
                            #     canvas.create_rectangle(ras*10.875,ras*6.25,ras*11.25,ras*6.625,fill="white",outline="grey")
                            #     canvas.create_polygon(ras*10.975,ras*6.425,ras*11.15,ras*6.425,ras*11.0625,ras*6.525,fill="grey",outline="grey")
                            #     canvas.create_rectangle(ras*10.975,ras*6.525,ras*11.15,ras*6.525,fill="grey",outline="grey")
                            #     canvas.create_rectangle(ras*11.05,ras*6.425,ras*11.05,ras*6.325,fill="grey",outline="grey")
                            #     out_window.update()
                            #     sleep(0.1)
                            #     #webbrowser.open('https://yadi.sk/d/QsL3RJtT-QnlLA', new=2) # открыть ссылку
                            #     webbrowser.open('https://drive.google.com/drive/folders/13rG5KQ2AZVu8M3eQzuGKmlFusTILlbqs', new=2) # открыть ссылку
                            # ссылка на обучение
                            if (x>=ras*11.375 and y>=ras*6.25 and x<=ras*11.75 and y<=ras*6.625):
                                canvas.create_rectangle(ras*11.375,ras*6.25,ras*11.75,ras*6.625,fill="white",outline="grey") 
                                canvas.create_text(ras*11.5625,ras*6.4375,text="?",font="Verdana 9",justify=CENTER,fill="grey")
                                out_window.update()
                                sleep(0.1)
                                webbrowser.open('https://github.com/SeungJae928/BARS-international-mju', new=2) # открыть ссылку
                            # ссылка на оценивание
                            # if (x>=ras*10.375 and y>=ras*6.25 and x<=ras*10.75 and y<=ras*6.625 and 1):
                            #     canvas.create_rectangle(ras*10.75,ras*6.25,ras*10.375,ras*6.625,fill="white",outline="grey")
                            #     canvas.create_polygon(ras*10.43,ras*6.4,ras*10.52,ras*6.4,ras*10.57,ras*6.3,ras*10.61,ras*6.4,ras*10.7,ras*6.4, ras*10.62,ras*6.45,ras*10.63,ras*6.55, ras*10.57,ras*6.5, ras*10.5,ras*6.55,ras*10.52,ras*6.45,fill="white",outline="grey")
                            #     out_window.update()
                            #     sleep(0.1)
                            #     #webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLSfWepWJiSSp6inbfOmyO5AJmnSh3XO4asBRnB1FGMFRuKChOg/viewform', new=2)
                            #     webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLSfOLysTI8F9iPvoiu5R__bpcbtZvHo4up4pca1XKYu9sgEkxA/viewform', new=2)
                                #webbrowser.open('https://habr.com/ru/post/470938/', new=2) # открыть ссылку
                            # войти в режим развития памяти
                            if (y>=ras*7.75 and y<=ras*8.125): 
                                control_memory_mode = 1
                                control_memory_mode_i = 1
                            # режим дебютов
                            if (y>=ras*7.25 and y<=ras*7.625 and len(debuts)>1): 
                                control_memory_mode = 3
                                control_memory_mode_i = 1
                                area_monitor = deepcopy(debuts[control_memory_mode_i][1])
                            # задачник
                            if (y<=ras*7.125 and y>=ras*6.75 and len(zadania)>1):
                                control_memory_mode = 5
                                control_memory_mode_i = 1
                                area_monitor = deepcopy(zadania[control_memory_mode_i][1])
                            # 새게임
                            if (y>=ras*3 and y<=ras*3.5):
                                area_monitor = deepcopy(area_zero)
                                control_move = 1
                                msgbox.showinfo("알림", "당신은 화이트 선입니다")
                            # move
                            if (y>=ras*4.075 and y<=ras*4.325):
                                control_move = 1
                            if (y>=ras*4.325 and y<=ras*4.575):
                                control_move = 2
                            # vs
                            if (y>=ras*5.125 and y<=ras*5.375):
                                control_vs = 3
                            if (y>=ras*5.375 and y<=ras*5.625):
                                control_vs = 2
                            if (y>=ras*5.625 and y<=ras*5.875):
                                control_vs = 1
                            if (y>=ras*5.875 and y<=ras*6.125): # 헬퍼로 연결
                                control_vs = 4
                        else: # режим тренировки памяти
                            if ((control_memory_mode==1 or control_memory_mode==3 or control_memory_mode==5) and y>=ras*6.75 and y<=ras*7.25):
                                # смена режима по кнопкам
                                if (x>=ras*9.25 and x<=ras*9.75):
                                    control_memory_mode_i = control_memory_mode_i - 10
                                if (x>=ras*9.75 and x<=ras*10.25):
                                    control_memory_mode_i = control_memory_mode_i - 1
                                if (x>=ras*10.75 and x<=ras*11.25):
                                    control_memory_mode_i = control_memory_mode_i + 1
                                if (x>=ras*11.25 and x<=ras*11.75):
                                    control_memory_mode_i = control_memory_mode_i + 10
                                # проверка на выход за пределы массива по верхней границе
                                if (control_memory_mode_i>32 and control_memory_mode==1):
                                    control_memory_mode_i = 32
                                if (control_memory_mode_i>len(debuts)-1 and control_memory_mode==3):
                                    control_memory_mode_i = len(debuts)-1
                                if (control_memory_mode_i>len(zadania)-1 and control_memory_mode==5):
                                    control_memory_mode_i = len(zadania)-1
                                # проверка на выход за пределы массива по нижней границе
                                if (control_memory_mode_i<1):
                                    control_memory_mode_i = 1
                                # отображение картинки
                                if (control_memory_mode==3):
                                    area_monitor = deepcopy(debuts[control_memory_mode_i][1])
                                if (control_memory_mode==5):
                                    area_monitor = deepcopy(zadania[control_memory_mode_i][1])
                            if (y>=ras*8.25 and y<=ras*8.75): 
                                if (control_memory_mode==1): # "следующее задание"
                                    control_memory_mode = 2
                                    craft_task_memory() # сгенерировать новое задание
                                elif (control_memory_mode==2): 
                                    control_memory_mode = 1
                                    test_task_memory() # сдать задание
                                elif (control_memory_mode==3): # "следующее задание"
                                    control_memory_mode = 4
                                    craft_task_memory2() # сгенерировать новое задание
                                elif (control_memory_mode==4): 
                                    control_memory_mode = 3
                                    test_task_memory2() # сдать задание
                                elif (control_memory_mode==5): # "следующее задание"
                                    control_memory_mode = 6
                                    control_vs = 3
                                    craft_task_memory3() # сгенерировать новое задание
                                #elif (control_memory_mode==6): 
                                #    control_memory_mode = 5
                                #    test_task_memory2() # сдать задание
                            if (y>=ras*7.5 and y<=ras*8.0): # "выйти"
                                control_memory_mode = 0
                    
            if (control_edit==0 or control_memory_mode==6): # вызов рисовалки информации на виджетов
                
                if (len(history)>1):
                    control_protocol.clear()
                    control_protocol_flag = len(history) - 1
                    i = 0
                    while (i<21 and control_protocol_flag>1):
                        i = i + 1
                        control_protocol_flag = control_protocol_flag - 1
                    #print(">",control_protocol_flag,len(history) - 1)
                    if (int(history[control_protocol_flag][0]/100)%10==2 and control_protocol_flag>1):
                        control_protocol_flag = control_protocol_flag + 1
                    craft_protocol(control_protocol_flag,len(history) - 1)
                else:
                    control_protocol.clear()
                    control_protocol_flag = 0
                if (len(go_operation)>0):
                    control_actions.clear()
                    control_actions_flag = 0
                    craft_actions(0)
                else:
                    control_actions.clear()
                    control_actions_flag = 0
            if ((len(history)>1 and control_vs==3 or len(history)>2 and control_vs!=4 or klik[1][0]!=-1) and control_edit==0): #  and go_error<10
                control_back = 1
            else:
                control_back = 0
            klik_flag = 1
            reboot_monitor()

    def craft_protocol(a,b):  # продумать виджет 1
        global control_protocol
        global history
        #i = 0
        control_protocol.clear()
        while (a<=b and len(control_protocol)<=10): # i<200 на всякий пожарный
            mas = [int(a/2)+1,-1,-1,-1,-1,-1,-1]
            if ((int(history[a][0]/100)%10)==1):                
                if (len(history[a])>2):
                    mas[2] = 1
                else:
                    mas[2] = 0
                mas[1] = history[a][0]%100
                mas[3] = history[a][len(history[a])-1]%100
                a = a + 1
            else:
                mas[1] = -1
                mas[2] = -1
                mas[3] = -1
            if (a<=b):                
                if (len(history[a])>2):
                    mas[5] = 1
                else:
                    mas[5] = 0
                mas[4] = history[a][0]%100
                mas[6] = history[a][len(history[a])-1]%100
                a = a + 1
            else:
                mas[4] = -1
                mas[5] = -1
                mas[6] = -1
            control_protocol.append(deepcopy(mas))
            #i = i + 1
        #print(control_protocol)
        
    def craft_actions(a): # продумать виджет 2 
        global control_actions
        global go_operation
        i = 1
        b = a
        control_actions.clear()
        #print(a)
        #print(":", go_operation)
        #print_mas(go_operation)
        while (len(control_actions)<7 and len(control_actions)+b<=len(go_operation) and a<len(go_operation)):
            mas = [a+1,-1,-1,-1]             
            i = i + 1
            if (len(go_operation[a])>2):
                mas[2] = 1
            else:
                mas[2] = 0
            mas[1] = go_operation[a][0]%100
            mas[3] = go_operation[a][len(go_operation[a])-1]%100
            a = a + 1
            control_actions.append(deepcopy(mas))
        #print(control_actions)
            
    def click2(event): # только удаление шашек при редактировании
        global area_monitor
        global klik_flag
        global control_edit
        global control_add
        if (klik_flag==1 and control_edit==1 and control_memory_mode==0):
            klik_flag = 0
            x = event.x
            y = event.y
            if ((x >= ras/2) and (x <= ras/2*17) and (y >= ras/2) and (y <= ras/2*17)): 
                x = map(x, ras/2, ras/2*17, 0, 8)
                y = map(y, ras/2, ras/2*17, 0, 8)
                if (area_monitor[y][x]!=9):
                    #control_add = area_monitor[y][x]
                    area_monitor[y][x] = 0
                    reboot_monitor()
            klik_flag = 1
        

    def click3(event):
        global control_memory_mode
        global control_memory_mode_i
        global control_protocol
        global control_protocol_flag
        control_protocol_flag2 = 0
        global control_actions
        global control_actions_flag
        #control_actions_flag2 = 0
        global history
        global go_operation
        global debuts
        global zadania
        global area_monitor
        x = event.x
        y = event.y
        d = int(-1*(event.delta/120))
        if (x>=ras*9.25 and x<=ras*11.75 and y>=ras*0.5 and y<=ras*3.5): # для прокручивания виджета 1
            #print("1234567890")
            if (len(history)>1):
                control_protocol.clear()
                control_protocol_flag2 = len(history) - 1
                i = 0
                while (i<21 and control_protocol_flag2>1):
                    i = i + 1
                    control_protocol_flag2 = control_protocol_flag2 - 1
                if (int(history[control_protocol_flag2][0]/100)%10==2 and control_protocol_flag2>1):
                    control_protocol_flag2 = control_protocol_flag2 + 1
                #craft_protocol(control_protocol_flag,len(history) - 1)
                #u = control_protocol_flag2 - control_protocol_flag2
                if (control_protocol_flag+d*2<=control_protocol_flag2 and d>0 or control_protocol_flag<=control_protocol_flag2 and d<0 and control_protocol_flag+d*2>0):
                    control_protocol_flag = control_protocol_flag + d*2
                #print(control_protocol_flag,len(history)-1-control_protocol_flag2+control_protocol_flag)
                f = 0
                if (control_protocol_flag2==control_protocol_flag or int(history[control_protocol_flag][0]/100)%10==2):
                    f = 1
                craft_protocol(control_protocol_flag,len(history)-f-control_protocol_flag2+control_protocol_flag)
            else:
                control_protocol.clear()
                control_protocol_flag = 0
        if (x>=ras*9.25 and x<=ras*11.75 and y>=ras*4 and y<=ras*6): # для прокручивания виджета 2
            if (len(go_operation)>7):
                control_actions.clear()
                if (control_actions_flag>0 and d<0 or d>0 and control_actions_flag<len(go_operation)-7): #len(go_operation)-7)
                    control_actions_flag = control_actions_flag + d
                    #print(control_actions_flag)
                craft_actions(control_actions_flag)
            else:
                #control_actions.clear()
                control_actions_flag = 0
        if (x>=ras*9.25 and x<=ras*11.75 and y>=ras*6.75 and y<=ras*7.25 and control_memory_mode==1): # для прокручивания уровня сложности
            control_memory_mode_i = control_memory_mode_i - d
            if (control_memory_mode_i>32):
                control_memory_mode_i = 32
            if (control_memory_mode_i<1):
                control_memory_mode_i = 1
        if (x>=ras*9.25 and x<=ras*11.75 and y>=ras*6.75 and y<=ras*7.25 and control_memory_mode==3): # для прокручивания уровня сложности
            control_memory_mode_i = control_memory_mode_i - d
            if (control_memory_mode_i>len(debuts)-1):
                control_memory_mode_i = len(debuts)-1
            if (control_memory_mode_i<1):
                control_memory_mode_i = 1
            area_monitor = deepcopy(debuts[control_memory_mode_i][1])
        if (x>=ras*9.25 and x<=ras*11.75 and y>=ras*6.75 and y<=ras*7.25 and control_memory_mode==5): # для прокручивания уровня сложности
            control_memory_mode_i = control_memory_mode_i - d
            if (control_memory_mode_i>len(zadania)-1):
                control_memory_mode_i = len(zadania)-1
            if (control_memory_mode_i<1):
                control_memory_mode_i = 1
            area_monitor = deepcopy(zadania[control_memory_mode_i][1])
        #canvas.create_rectangle(ras*9.25,ras*6.75,ras*11.75,ras*7.25,fill="white")
        #print(y,x,d)
        reboot_monitor()
                    
    # хрень для первого запуска
    go_operation = deepcopy(generator_move(area_monitor, go_color))
    print_go_operation()
    craft_actions(0)
    history.append(deepcopy(area_monitor))
    #reboot_monitor()
    reboot_checkers()
    reboot_controller()
    #hello()
    if (control_vs==go_color or control_vs==4): # ну мало ли
        mozg()
        reboot_checkers()
        reboot_controller()
        go_operation = deepcopy(generator_move(area_monitor, go_color))
        print_go_operation()
    
    canvas.bind("<Button-1>", click1)   # ПКМ
    canvas.bind("<MouseWheel>", click3) # крутим колесико
    canvas.bind("<Button-3>", click2)   # ЛКМ

    canvas.pack()
    out_window.mainloop() # out_window.update()
    #in_window.mainloop()
    
read_file()
#print(debuts)
#print()
#print(zadania)
qwerty() # тут запуск всего
for i in history:
    print(i)