import time
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog, dialog
import easygui as g
import pygame.mixer
import os
import random as r
import time as t

#初始化
pygame.mixer.init()
window = tk.Tk()
window.geometry('590x200')
window.minsize(300,200)
window.title('Guide IDE(beta v0.74.2)')
window.configure(bg='skyblue')
bgm_n = 2

#导入
bgm1 = pygame.mixer.Sound('audio/bgm/1.flac')
bgm2 = pygame.mixer.Sound('audio/bgm/2.flac')
bgm3 = pygame.mixer.Sound('audio/bgm/3.flac')

#方法/类定义
def play_audio(number):
    bgms[number].play(-1)

def test():
    pass
    #file_login = open('config/config.txt',mode='r')
    #read = file_login.readlines()
    #for i in read:
    #g.msgbox(i)

def guide_moudle():
    os.system('python Guide-init.py')

def newFile():
    def save():
        global file_path
        global file_text
        file_path = filedialog.asksaveasfilename(title=u'保存文件(记得后缀名带上)')
        print('保存文件：', file_path)
        file_text = code.get('1.0', tk.END)
        if file_path is not None:
            with open(file=file_path, mode='a+', encoding='utf-8') as file:
                file.write(file_text)
            code.delete('1.0', tk.END)
            dialog.Dialog(None, {'title': '保存好了！', 'text': '保存完成,如需运行请直接双击文件!', 'bitmap': 'warning', 'default': 0,
                                 'strings': ('OK', 'Cancle')})
            print('保存完成')
            toplevel1.destroy()


    toplevel1 = Toplevel()
    toplevel1.title('新的文件')
    toplevel1.geometry("1200x600")

    labelframe1 = LabelFrame(toplevel1, text='代码填写', width=300, height=200)
    labelframe1.place(x=0, y=0,width=1200,height=600)

    code = Text(labelframe1, fg='black')
    code.place(x=5,y=5, width=1150,height=550)

    button_toplevel = Button(labelframe1,text='保存',command=save)
    button_toplevel.pack()


def openFile():
    def open():
        global file_path
        global file_text
        file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
        print('打开文件：', file_path)
        file_text = os.open(file_path,1)
        code.insert('insert',file_text)

    def error():
        messagebox.showerror('ERROR','暂未开启此模式，请等待更新版本！')

    file_path = None
    file_text = None
    toplevel1 = Toplevel()
    toplevel1.title('打开文件')
    toplevel1.geometry("1200x600")

    labelframe1 = LabelFrame(toplevel1, text='代码填写', width=300, height=200)
    labelframe1.place(x=0, y=0, width=1200, height=600)

    code = Text(labelframe1, fg='black')
    code.place(x=5, y=5, width=1150, height=550)

    button_toplevel = Button(labelframe1, text='打开', command=error)
    button_toplevel.pack()

def settings():
    global bgm_n
    def set_music():
        global bgm_n
        value = lb.get(lb.curselection())  # 获取当前选中的文本
        bgm_n = value

    toplevel1 = Toplevel()
    toplevel1.title('设置')
    toplevel1.geometry("400x600")

    labelframe1 = LabelFrame(toplevel1, text='BGM设置', width=300, height=200)
    labelframe1.place(x=0, y=0, width=120, height=200)

    var2 = tk.StringVar()
    var2 = tk.StringVar()

    lb = tk.Listbox(toplevel1, listvariable=var2)

    list_insert = ['暂无设置','Developer_v0.19.5']
    for item in list_insert:
        lb.insert('end', item)  # 从最后一个位置开始加入值
    lb.place(x=0,y=0,width=120)

def login():
    file_login = open('config/config.txt', mode='r')

    def auth():
        un_pwd = file_login.readlines()
        if un_pwd[0] != '':
            if str(entry_un.get()) == str(un_pwd[0]):
                if str(entry_pwd.get()) == str(un_pwd[1]):
                    messagebox.showinfo('成功','登录成功！')
                    file_login.close()
                else:
                    messagebox.showinfo('error', '您的密码错误')
            else:
                messagebox.showinfo('error', '您的用户名错误')
        else:
            messagebox.showinfo('error','您尚未注册！')

    #参数
    toplevel1 = Toplevel()
    toplevel1.title('登录')
    toplevel1.geometry("400x120")

    labelframe1 = LabelFrame(toplevel1, text='登录', width=300, height=200)
    labelframe1.place(x=0, y=0, width=400, height=115)

    entry_un = Entry(labelframe1,textvariable='请输入用户名')
    entry_un.pack()

    entry_pwd = Entry(labelframe1,textvariable='请输入密码',show='*')
    entry_pwd.pack()

    button_login = Button(labelframe1,text='登录',command=auth)
    button_login.pack()

def register():
    userR = 'none'
    pwdR = '1234'
    file_reg = open('config/config.txt', mode='w')
    file_reg.write(userR+'\n'+pwdR)


#组件写入
label = Label(window,text='欢迎来到Guide IDE!',bg='skyblue',font=('华文彩云', 12)) # text:标签的文本内容,bg:标签背景颜色,font:（字体，字号，粗细...） 字体
label.place(x=0,y=0,width=150,height=50)

button1 = Button(window,text='新建文件',bg='skyblue',font=('华文彩云', 12),command=newFile)
button1.place(x=30,y=50,width=100,height=50)

button2 = Button(window,text='打开文件',bg='skyblue',font=('华文彩云', 12),command=openFile)
button2.place(x=30,y=105,width=100,height=50)

button_settings = Button(window,text='设置',bg='skyblue',command=settings)
button_settings.place(width=50,height=25,x=500,y=0)

button_guide = Button(window,text='Guide代码',command=guide_moudle)
button_guide.place(width=80,height=25,x=500,y=60)

button_test = Button(window,text='test',command=test)
button_test.place(width=50,height=25,x=500,y=30)

#参数定义
bgms = [bgm1,bgm2,bgm3]

#窗口显示/循环
play_audio(2)
window.mainloop()