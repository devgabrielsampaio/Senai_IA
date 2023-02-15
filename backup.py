import os
from tkinter import Button, Entry, Frame, Label, PhotoImage, Tk, font, messagebox, ttk,filedialog
from tkinter import *
import tkinter
from turtle import width
import mysql.connector
from io import *
import io
from tkcalendar import DateEntry
import datetime as dt
from  datetime import date, datetime


pastaApp=os.path.dirname(__file__)

app = Tk()
app.title("Menu Principal")
largura = 680
altura = 640
largura_screen = app.winfo_screenwidth()
altura_screen = app.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
app.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
app.resizable(False, False)
app.iconbitmap("img\\robo.ico")
btn_criarbackup=PhotoImage(file="img\\otimizacao.png")
btn_enviar=PhotoImage(file="img\\enviar.png")

def tb6_criarbackup():
    global file
    file=tkinter.filedialog.asksaveasfilename(defaultextension='.sql',filetypes=[("DB File",".sql")])
    if(file !=""):
        os.chdir("C:\\Program Files\\MariaDB 10.6\\bin")
        os.system("mysqldump -uroot -P1200 -palunolab tcc > "+file)
        messagebox.showinfo("Sucesso","Backup Criado com Sucesso!")
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Backup Criado com Sucesso")
        arquivo.close()
    if(file==""):
        messagebox.showerror("Erro","Erro ao Criar Backup")
def tb6_restaurarbackup():
    global file_restaurar
    file_restaurar=tkinter.filedialog.askopenfilename(defaultextension='.sql',filetypes=[("DB File",".sql")])
    if(file_restaurar!=""):
        conexao=mysql.connector.connect(
            host='localhost',
            port='1200',
            user='root',
            password='alunolab'
        )
        cursor=conexao.cursor()
        comando=f'create database tcc'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
        os.chdir("C:\\Program Files\\MariaDB 10.6\\bin")
        os.system("mysql -uroot -P1200 -palunolab tcc< "+file_restaurar)
        messagebox.showinfo("Sucesso","Backup Restaurado com Sucesso!")
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Backup Restaurado com Sucesso")
        arquivo.close()
    if(file_restaurar==""):
        messagebox.showerror("Erro","Erro ao Restaurar Backup")

tb6_botao1=Button(app,image=btn_criarbackup,text="Criar Backup",compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb6_criarbackup)
tb6_botao1.place(x=200,y=40,width=200,height=40)

tb6_botao2=Button(app,image=btn_enviar,text="Restaurar Backup",compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb6_restaurarbackup)
tb6_botao2.place(x=200,y=100,width=200,height=40)

app.mainloop()