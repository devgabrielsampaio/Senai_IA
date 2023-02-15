import os
from tkinter import END, Button, Entry, Frame, Label, PhotoImage, Tk, font, messagebox, simpledialog
from tkinter import *
from tkinter import ttk
import mysql.connector
import datetime as dt

pastaApp=os.path.dirname(__file__)

app = Tk()
app.title("Esqueci a Senha")
label1=Label(app,background="#00008B",width=600,height=500)
label1.place(x=0,y=0)

global senha,novaSenha,login,mail,resposta_chave,new_pass,pesquisa,envio,abrir_login

def enviaremail():
    if(str(senha.get())==str(novaSenha.get())):
        conexao=mysql.connector.connect(
            host='localhost',
            port='1200',
            user='root',
            password='alunolab',
            database='tcc'
        )
        cursor=conexao.cursor()
        comando=f'select email from entrada where login="{login.get()}"'
        cursor.execute(comando)
        resultado=cursor.fetchall()
        for pesquisa in resultado:
            print (type(pesquisa[0]))
        try:
            if str(pesquisa[0]) is not None:
                import win32com.client as win32
                import random
                char_list='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
                new_pass=''.join(random.sample(char_list,6))
                outlook=win32.Dispatch('outlook.application')
                mail=outlook.CreateItem(0)
                mail.To=pesquisa[0]
                mail.Subject='Redefinição de Senha'
                mail.Body='Olá, Digite este código: '+new_pass+', para redefinir sua senha'
                mail.Send()
                resposta_chave=simpledialog.askstring("Chave","Informe a chave que está em seu email:")
                if(resposta_chave==new_pass):
                    usuario=str(login.get())
                    conexao2=mysql.connector.connect(
                        host='localhost',
                        port='1200',
                        user='root',
                        password='alunolab',
                        database='tcc'
                    )
                    cursor2=conexao2.cursor()
                    comando2=f'update entrada set senha="{senha.get()}" where login="{login.get()}"'
                    cursor2.execute(comando2)
                    conexao2.commit()
                    try:
                        messagebox.showinfo("Senha Redefinida","Senha Redefinida com Sucesso")
                        login.delete(0,END)
                        senha.delete(0,END)
                        novaSenha.delete(0,END)
                        data=dt.datetime.now()
                        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
                        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
                        arquivo.writelines("\n"+data_texto+" || O Usuário "+usuario+" Redefiniu a Senha")
                        arquivo.close()
                    except UnboundLocalError:
                        messagebox.showerror("Erro","Erro ao redefinir senha!")
                        data=dt.datetime.now()
                        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
                        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
                        arquivo.writelines("\n"+data_texto+" || Erro ao Redefinir Senha")
                        arquivo.close()
                    finally:
                        cursor2.close()
                        conexao2.close()
                if(resposta_chave!=new_pass):
                    messagebox.showerror("Erro","Chave Informada é Inválida")   
                    data=dt.datetime.now()
                    data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
                    arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
                    arquivo.writelines("\n"+data_texto+" || Chave Inválida")
                    arquivo.close()    
        except UnboundLocalError:
            messagebox.showerror('Erro','Login Inexistente')
            data=dt.datetime.now()
            data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
            arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
            arquivo.writelines("\n"+data_texto+" || Login Inexistente")
            arquivo.close()   
        finally:
            cursor.close()
            conexao.close()
    else:
        messagebox.showerror('Erro','As senhas informadas não são iguais!')
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open("logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Senhas Não Conferem")
        arquivo.close()   


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

label4=Label(app,text="Nova Senha:",background="white",foreground="black",font=("Century Gothic", 16, font.BOLD))
label4.place(x=240,y=170,width=200,height=30)

login=Entry(app,background="#00008B",foreground="white",font=("Century Gothic", 12, font.BOLD))
login.place(x=210,y=120,width=250,height=40)

senha=Entry(app,background="#00008B",foreground="white",font=("Century Gothic", 12, font.BOLD),show="*")
senha.place(x=210,y=200,width=250,height=40)

label4=Label(app,text="Confirme:",background="white",foreground="black",font=("Century Gothic", 16, font.BOLD))
label4.place(x=240,y=240,width=200,height=30)

novaSenha=Entry(app,background="#00008B",foreground="white",font=("Century Gothic", 12, font.BOLD),show="*")
novaSenha.place(x=210,y=270,width=250,height=40)

botao1=Button(app,foreground="white",background="#E50557",text="Enviar Chave",font=("Century Gothic", 12, font.BOLD),command=enviaremail)
botao1.place(x=265,y=320,width=150,height=50)
