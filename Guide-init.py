import easygui
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog, dialog

Auttric = 'GuideMoudle:'

#codeLab
class Object():
    def printf(self,str):
        return Auttric+' '+str
    def var(self,name,str):
        return Auttric+' '+'定义:'+name+'变量,内容为:'+str
    def window(self,name,type,bg):
        window = tk.Tk()
        window.geometry(type)
        window.title(name)
        window.configure(bg=bg)

        labal = Label(window,text='RUNNING:正在运行窗口:'+name)
        labal.pack()
        window.mainloop()
    def messages(self,title,string):
        messagebox.showinfo(title,string)

#Running As Its.
def running():
    tj1 = None
    tj2 = None
    tj3 = None
    p = None

    if command == 'printf':
        tj1 = easygui.enterbox('请输入打印内容:')
        easygui.msgbox(title='running',msg=object.printf(tj1))
    elif command == 'var':
        tj1 = easygui.enterbox('请输入变量名')
        tj2 = easygui.enterbox('请输入变量定义内容')
        p = object.var(tj1,tj2)
        easygui.msgbox(title='running',msg=p)
    elif command == 'window':
        tj1 = easygui.enterbox('请输入窗口名称')
        tj2 = easygui.enterbox('请输入窗口宽高(宽x高)')
        tj3 = easygui.enterbox('请输入背景颜色(英语！)')
        object.window(tj1,tj2,tj3)
    elif command == 'messages':
        tj1 = easygui.enterbox('请输入标题')
        tj2 = easygui.enterbox('请输入文本')
        object.messages(tj1,tj2)
        easygui.msgbox(title='running',msg='进程结束')
    else:
        easygui.msgbox(title='running_Guide IDE',msg='请输入正确的指令')

object = Object()
command = easygui.enterbox('请输入指令:')
running()
