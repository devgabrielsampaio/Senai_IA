
from cgitb import text
from doctest import master
from fileinput import filename
from logging import PlaceHolder, config
from tkinter import *
from tkinter import ttk
import os
from tkinter import font
import time
import datetime as dt
import tkinter
from tkinter import messagebox
from webbrowser import BackgroundBrowser
import webbrowser 
import mysql.connector
from tkinter import simpledialog

pastaApp=os.path.dirname(__file__)

app = Tk()
app.title("Tela de Entrada")
label1=Label(app,background="#00008B",width=600, height=500)
label1.place(x=0,y=0)
def entrar():
    def tela_menu():
        app.destroy()
        exec(open("Tela_Menu.py",encoding="utf-8").read())
    def assistente_virtual():
        app.destroy()
        exec(open("Assistente_Virtual.py",encoding="utf-8").read())
    login1=login.get()
    senha1=senha.get()
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f'select nivel from entrada where login="{login1}" and senha="{senha1}"'
    cursor.execute(comando)
    resultado=cursor.fetchall()
    for linha in resultado:
        print(linha[0])
    try:
        if linha[0]=="Administrador":
            data=dt.datetime.now()
            data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
            arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
            arquivo.write("\n"+data_texto+" || o Usuário "+login.get()+" entrou no sistema com privilégios de usuário "+linha[0])
            arquivo.close()
            tela_menu()
        if linha[0]=="Padrão":
            data=dt.datetime.now()
            data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
            arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
            arquivo.writelines("\n"+data_texto+" || o Usuário "+login.get()+" entrou no sistema com privilégios de usuário "+linha[0])
            arquivo.close()
            assistente_virtual()
    except UnboundLocalError:
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || o Usuário "+login.get()+" tentou acessar o sistema")
        arquivo.close()
        messagebox.showerror('Erro','Login ou Senha Incorretos')
    finally:
        cursor.close()
        conexao.close()
def esqueciasenha():
    def abrirtela():
        app.destroy()
        exec(open("Esqueci_senha.py",encoding="utf-8").read())
    resposta_login=simpledialog.askstring("Esqueci a Senha","Digite seu Login:",parent=app)
    if(resposta_login is None) :
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || o Usuário deixou o campo em branco na redefinição de senha")
        arquivo.close()
        messagebox.showerror("Erro","Preencha o Campo Login Corretamente!")
    else:
      conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f'select email from entrada where login="{resposta_login}"'
    cursor.execute(comando)
    resultado=cursor.fetchall()
    for pesquisa in resultado:
        print (type(pesquisa[0]))
    try:
        if pesquisa[0] is not None:
            data=dt.datetime.now()
            data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
            arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
            arquivo.writelines("\n"+data_texto+" || o Usuário "+resposta_login+" Acessou a Redefinição de Senha")
            arquivo.close()
            abrirtela()
    except UnboundLocalError:
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || o Usuário "+resposta_login+" tentou acessar a Redefinição de Senha")
        arquivo.close()
        messagebox.showerror('Erro','Login Inexistente')
    finally:
        cursor.close()
        conexao.close()   



btn_facebook=PhotoImage(file="img\\facebook.png")
btn_ativo=PhotoImage(file="img\\entrar_normal.png")
btn_instagram=PhotoImage(file="img\\instagram.png")
btn_linkedin=PhotoImage(file="img\\linkedin.png")
btn_esqueciasenha=PhotoImage(file="img\\esqueci_senha.png")

largura = 630
altura = 550
largura_screen = app.winfo_screenwidth()
altura_screen = app.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
app.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
app.resizable(False, False)
app.iconbitmap("img\\robo.ico")

label2=Label(app,background="white",foreground="white",width=50,height=30)
label2.place(x=150,y=50)

label3=Label(app,text="Login:",background="white",foreground="black",font=("Century Gothic", 16, font.BOLD))
label3.place(x=280,y=90,width=90,height=30)

label4=Label(app,text="Senha:",background="white",foreground="black",font=("Century Gothic", 16, font.BOLD))
label4.place(x=280,y=170,width=90,height=30)

login=Entry(app,background="#00008B",foreground="white",font=("Century Gothic", 12, font.BOLD))
login.place(x=210,y=120,width=250,height=40)

senha=Entry(app,background="#00008B",foreground="white",font=("Century Gothic", 12, font.BOLD),show="*")
senha.place(x=210,y=200,width=250,height=40)

botao1=Button(app,image=btn_ativo,borderwidth=0,foreground="white",activebackground="white",command=entrar)
botao1.place(x=230,y=252,width=200,height=50)
botao1["bg"]="white"

botao5=Button(app,image=btn_esqueciasenha,borderwidth=0,foreground="white",activebackground="white",command=esqueciasenha)
botao5.place(x=230,y=311,width=200,height=50)
botao5["bg"]="white"

label5=Label(app,text="_________________________________",background="white",foreground="black",font=("Century Gothic", 14, font.BOLD))
label5.place(x=190,y=360,width=280,height=20)

label6=Label(app,text="Confira:",background="white",foreground="black",font=("Century Gothic", 16, font.BOLD))
label6.place(x=190,y=390,width=280,height=20)

label7=Label(app,text="_________________________________",background="white",foreground="black",font=("Century Gothic", 14, font.BOLD))
label7.place(x=190,y=408,width=280,height=20)

botao2=Button(app,image=btn_facebook,borderwidth=0,foreground="white",activebackground="white",command=lambda:webbrowser.open('https://www.facebook.com/firjansenai/'))
botao2.place(x=190,y=435,width=50,height=30)
botao2["bg"]="white"

botao3=Button(app,image=btn_instagram,borderwidth=0,foreground="white",activebackground="white",command=lambda:webbrowser.open('https://www.instagram.com/firjansenai/'))
botao3.place(x=300,y=435,width=50,height=30)
botao3["bg"]="white"

botao4=Button(app,image=btn_linkedin,borderwidth=0,foreground="white",activebackground="white",command=lambda:webbrowser.open('https://www.linkedin.com/company/firjan/'))
botao4.place(x=420,y=435,width=50,height=30)
botao4["bg"]="white"

app.mainloop()