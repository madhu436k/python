from tkinter import *
screen=Tk()
screen.geometry("500x500")
screen.title('job apllication')
def delet():
    screen1.destroy()

def delet1():
    screen2.destory()
    
def error():
    screen1=Toplevel(screen)
    screen1.geometry("250x60")
    screen1.title("error msg")
    Label(screen1,text="all fields req",fg='red',bg='blue').pack()

def sucsses():
    screen1=Toplevel(screen)
    screen1.geometry("250x60")
    screen1.title("result")
    Label(screen1,text="applied sucessfully",fg='green').pack()
    


    

def register():
    uname_text=uname.get()
    psw_text=psw.get()
    if uname_text=="":
        '''screen1=Toplevel(screen)
        screen1.geometry("250x60")
        screen1.title("warning")
        Label(screen1,text="all fields req").pack()'''
        error()
    elif  psw_text=="":
        error()
    else:
        sucsses()
def clear():
    pass

heading=Label(text='job applicaton',fg='yellow',bg='blue',width="500",height='3').pack()

Label(text="uname").place(x=1,y=90)
Label(text="psw").place(x=1,y=190)

uname=StringVar()
psw=StringVar()

Entry(screen,textvariable=uname).place(x=55,y=90)
Entry(screen,textvariable=psw).place(x=55,y=190)

Button(screen,text='reg',width='7',bg='yellow',command=register).place(x=15,y=290)
Button(screen,text='clear',width='7',bg='yellow',command=clear).place(x=75,y=290)

