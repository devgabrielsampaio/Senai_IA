from cgitb import text
from doctest import master
import os
from tkinter import END, Button, Entry, Image, Label, PhotoImage, Tk, font
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import PIL
import mysql.connector
import time
import pyttsx3
import pyaudio
import speech_recognition as sr

pastaApp=os.path.dirname(__file__)

global aviso,texto,busca_turma,busca,abrirmicrofone,img,label1

app = Tk()
app.title("Assistente Virtual")
label1=Label(app,background="white",width=600, height=500)
label1.place(x=0,y=0)

largura = 680
altura = 640
largura_screen = app.winfo_screenwidth()
altura_screen = app.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
app.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
app.iconbitmap("img\\robo.ico")


label=Label(app,text="UTILIZE O MICROFONE PARA FAZER SUA BUSCA!",background="white",foreground="#005caa",font=("Century Gothic", 16, font.BOLD))
label.place(x=300,y=40,width=800,height=30)

label2=Label(app,text="APÓS CLICAR, AGUARDE 3 SEGUNDOS E DIGA O NOME DO LOCAL!",background="white",foreground="#005caa",font=("Century Gothic", 16, font.BOLD))
label2.place(x=300,y=100,width=800,height=30)

img= ImageTk.PhotoImage(Image.open("img\\mic.png"),master=app)
img2= ImageTk.PhotoImage(Image.open("img\\senai.png"),master=app)

label3=Label(app,image=img2)
label3.place(x=-50,y=450,width=409,height=334)

def busca_turma():
    from PIL import Image, ImageTk
    import PIL  
    global img_consulta
    import io
    app.update()
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f"select nome,sala,andar,bloco from turma where nome like '"+frase+"%'"
    cursor.execute(comando)
    resultado=cursor.fetchall()
    for pesquisa in resultado:
        print('')
    try:
        if pesquisa[0]!="":
            engine=pyttsx3.init()
            engine.say("A "+pesquisa[0]+"Estará na "+pesquisa[1]+" que fica no andar "+pesquisa[2]+"E no Bloco "+pesquisa[3])
            engine.runAndWait()
            conexao1=mysql.connector.connect(
                host='localhost',
                port='1200',
                user='root',
                password='alunolab',
                database='tcc'
            )
            cursor1=conexao1.cursor()
            comando1=f"select imagem from ambiente where nome like '"+pesquisa[1]+"%'"
            cursor1.execute(comando1)
            resultado1=cursor1.fetchall()
            consulta=resultado1[0][0]
            janela2 = Tk()
            janela2_largura = 490
            janela2_altura = 400
            janela2_largura_screen = janela2.winfo_screenwidth()
            janela2_altura_screen = janela2.winfo_screenheight()
            janela2_posx = janela2_largura_screen/2 - janela2_largura/2
            janela2_posy = janela2_altura_screen/2 - janela2_altura/2
            janela2.geometry("%dx%d+%d+%d" % (janela2_largura, janela2_altura, janela2_posx, janela2_posy))
            janela2.resizable(False, False)
            janela2.iconbitmap("img\\robo.ico")
            img_consulta=PIL.Image.open(io.BytesIO(consulta))
            img_consulta.thumbnail((1500,1000))
            img_consulta=PIL.ImageTk.PhotoImage(img_consulta,master=janela2)
            janela2.title(frase)
            label2=Label(janela2,width=500,height=400)
            label2.place(x=-10,y=0)
            label2.configure(image=img_consulta)
            label2.image=img_consulta 
            janela2.after(15000,janela2.destroy) 
    except UnboundLocalError:
        app.update()
        engine=pyttsx3.init()
        engine.say("hum... não entendi o que você disse")
        engine.runAndWait()
    finally:
        app.update()
        cursor.close()
        conexao.close()

def busca():
    from PIL import Image, ImageTk
    import PIL  
    global img_consulta
    import io
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f"select nome,andar,bloco from ambiente where nome like '"+frase+"%'"
    cursor.execute(comando)
    resultado=cursor.fetchall()
    for pesquisa in resultado:
        print('')
    try:
        if pesquisa[0]!="":
            engine=pyttsx3.init()
            engine.say(pesquisa[0]+"Se localiza no andar "+pesquisa[1]+"E no Bloco "+pesquisa[2])
            engine.runAndWait()
            conexao1=mysql.connector.connect(
                host='localhost',
                port='1200',
                user='root',
                password='alunolab',
                database='tcc'
            )
            cursor1=conexao1.cursor()
            comando1=f"select imagem from ambiente where nome like '"+frase+"%'"
            cursor1.execute(comando1)
            resultado1=cursor1.fetchall()
            consulta=resultado1[0][0]
            janela2 = Tk()
            janela2_largura = 490
            janela2_altura = 400
            janela2_largura_screen = janela2.winfo_screenwidth()
            janela2_altura_screen = janela2.winfo_screenheight()
            janela2_posx = janela2_largura_screen/2 - janela2_largura/2
            janela2_posy = janela2_altura_screen/2 - janela2_altura/2
            janela2.geometry("%dx%d+%d+%d" % (janela2_largura, janela2_altura, janela2_posx, janela2_posy))
            janela2.resizable(False, False)
            janela2.iconbitmap("img\\robo.ico")
            img_consulta=PIL.Image.open(io.BytesIO(consulta))
            img_consulta.thumbnail((1500,1000))
            img_consulta=PIL.ImageTk.PhotoImage(img_consulta,master=janela2)
            janela2.title(frase)
            label2=Label(janela2,width=500,height=400)
            label2.place(x=-10,y=0)
            label2.configure(image=img_consulta)
            label2.image=img_consulta 
            janela2.after(15000,janela2.destroy)
    except UnboundLocalError:
        app.update()
        engine=pyttsx3.init()
        engine.say("hum... não entendi o que você disse")
        engine.runAndWait()
    finally:
        app.update()
        cursor.close()
        conexao.close()

def abrirmicrofone():
    global frase,sr,pyttsx3
    microfone=sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source,duration=1)
        print('Diga alguma coisa')
        audio=microfone.listen(source)    
    try:
        frase=microfone.recognize_google(audio,language='pt-BR')
        print('você disse '+frase)
        if("turma" in frase):
            busca_turma()
        else:
            busca()
    except sr.UnknownValueError:
        app.update()
        engine=pyttsx3.init()
        engine.say("hum... não entendi o que você disse")
        engine.runAndWait()
    except sr.RequestError:
        app.update()
        engine=pyttsx3.init()
        engine.say("Por favor conecte-se a internet")
        engine.runAndWait()
    

botao1=tkinter.Button(app,image=img,background="white",foreground="white",bd=0,activebackground="gold",command=abrirmicrofone)
botao1.place(x=500,y=220,width=350,height=330)
botao1["bg"]="white"

app.mainloop()