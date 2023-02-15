
import base64
from distutils.log import error
from email.mime import image
import os
from tkinter import Button, Entry, Frame, Label, PhotoImage, Tk, font, messagebox, ttk,filedialog
from tkinter import *
import tkinter
from turtle import width
import mysql.connector
from io import *
import io
from tkcalendar import DateEntry
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,letter
from reportlab.lib.units import inch
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


global label6,nome,tipo,andar,bloco,tv,nome_consulta,tb2_tv,tb3_nome_consulta,tb3_entry_nome,tb3_cal_dataInicio,tb3_cal_dataencerramento,tb3_nome_banco,tb3_tv,tb3_datainicio,tb3_datatermino,tb3_fob,tb3_label_carregaimagem,tb3_get_image,popular,tb3_popular,tb2_Sala,buscarsala,tb4_Escolha,tb4_botao1,tb4_area,tb4_texto,cnv,tb4_cal_datainicio,tb5_tv,tb5_login,tb5_senha,tb5_nivel,tb5_email,tb5_popular,tb5_login_consulta,tb2_nome,tb2_andar,tb2_ano,tb2_bloco,tb2_popular,tb2_nome_consulta,tb3_data_inicial,tb3_data_final


def popular():
    tv.delete(*tv.get_children())
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando='select id,nome,tipo,andar,bloco from ambiente'
    cursor.execute(comando)
    resultado=cursor.fetchall()
    for linha in resultado:
        tv.insert("","end",values=linha)
def tb2_popular():
    tb2_tv.delete(*tb2_tv.get_children())
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando='select id,nome,sala,ano,andar,bloco from turma'
    cursor.execute(comando)
    resultado=cursor.fetchall()
    for linha in resultado:
        tb2_tv.insert("","end",values=linha)
def tb3_popular():
    tb3_tv.delete(*tb3_tv.get_children())
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando='select id,nome,data_inicio,data_termino from evento'
    cursor.execute(comando)
    resultado=cursor.fetchall()
    for linha in resultado:
        tb3_tv.insert("","end",values=linha)
def tb5_popular():
    tb5_tv.delete(*tb5_tv.get_children())
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando='select login,password(senha) as senha,nivel,email from entrada'
    cursor.execute(comando)
    resultado=cursor.fetchall()
    for linha in resultado:
        tb5_tv.insert("","end",values=linha)
    
def abririmagem():
    from PIL import Image, ImageTk
    import PIL
    global get_image,img
    get_image= tkinter.filedialog.askopenfilename(title="Selecione a Imagem", filetypes= (("PNG","*.png"), ("JPG","*.jpg"), ("JPEG","*.jpeg")))
    try:
        img=PIL.Image.open(get_image)
        img.thumbnail((350,350))
        img=PIL.ImageTk.PhotoImage(img)
        label6.configure(image=img)
        label6.image=img
    except AttributeError:
        messagebox.showerror("Erro","Por favor selecione uma imagem Válida!")
def tb3_abririmagem():
    from PIL import Image, ImageTk
    import PIL
    global tb3_get_image,tb3_img
    tb3_get_image= tkinter.filedialog.askopenfilename(title="Selecione a Imagem", filetypes= (("PNG","*.png"), ("JPG","*.jpg"), ("JPEG","*.jpeg")))
    try:
        tb3_img=PIL.Image.open(tb3_get_image)
        tb3_img.thumbnail((350,350))
        tb3_img=PIL.ImageTk.PhotoImage(tb3_img)
        tb3_label_carregaimagem.configure(image=tb3_img)
        tb3_label_carregaimagem.image=tb3_img
    except AttributeError:
        messagebox.showerror("Erro","Por favor selecione uma imagem Válida!")
def salvar():
    global get_image,img
    fob= open(get_image,'rb')
    fob=fob.read()
    nome_banco=nome.get()
    tipo_banco=tipo.get()
    andar_banco=andar.get()
    bloco_banco=bloco.get()
    dados=(nome_banco,tipo_banco,andar_banco,bloco_banco,fob)
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f'insert into ambiente(nome,tipo,andar,bloco,imagem) values (%s,%s,%s,%s,%s)'
    cursor.execute(comando,dados)
    conexao.commit()
    try:
        messagebox.showinfo('Sucesso','O Ambiente foi Inserido com Sucesso')
        nome.delete(0,END)
        tipo.delete(0,END)
        andar.delete(0,END)
        bloco.delete(0,END)
        label6.configure(image="")
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Ambiente Inserido com Sucesso")
        arquivo.close()
    except mysql.connector.errors.ProgrammingError:
        messagebox.showerror('Erro','Erro ao Inserir Ambiente')
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Erro ao Inserir Ambiente")
        arquivo.close()
    finally:
        popular()
        cursor.close()
        conexao.close()
def tb2_salvar():
    global tb2_nome_banco,tb2_andar_banco,tb2_bloco_banco,tb2_sala_banco,tb2_ano_banco
    tb2_nome_banco=tb2_nome.get()
    tb2_andar_banco=tb2_andar.get()
    tb2_bloco_banco=tb2_bloco.get()
    tb2_sala_banco=tb2_Sala.get()
    tb2_ano_banco=tb2_ano.get()
    dados=(tb2_nome_banco,tb2_sala_banco,tb2_ano_banco,tb2_andar_banco,tb2_bloco_banco)
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f'insert into turma(nome,sala,ano,andar,bloco) values (%s,%s,%s,%s,%s)'
    cursor.execute(comando,dados)
    conexao.commit()
    try:
        messagebox.showinfo('Sucesso','A Turma foi Inserida com Sucesso')
        tb2_nome.delete(0,END)
        tb2_andar.delete(0,END)
        tb2_bloco.delete(0,END)
        tb2_ano.delete(0,END)
        tb2_Sala.delete(0,END)
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Turma Inserida com Sucesso")
        arquivo.close()
    except mysql.connector.errors.ProgrammingError:
        messagebox.showerror('Erro','Erro ao Inserir Turma')
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Erro ao Inserir Turma")
        arquivo.close()
    finally:
        tb2_popular()
        cursor.close()
        conexao.close()
def tb3_salvar():
    global tb3_get_image,tb3_img,datetime
    tb3_data_inicial=datetime.strptime(str(tb3_cal_dataInicio.get_date()),"%Y-%m-%d")
    tb3_data_final=datetime.strptime(str(tb3_cal_dataencerramento.get_date()),"%Y-%m-%d")
    if(tb3_data_inicial>tb3_data_final):
        messagebox.showerror('Erro','Data de Início não pode ser maior que a Data Final')
    else:
        tb3_fob= open(tb3_get_image,'rb')
        tb3_fob=tb3_fob.read()
        tb3_nome_banco=tb3_entry_nome.get()
        tb3_datainicio=tb3_cal_dataInicio.get_date()
        tb3_datatermino=tb3_cal_dataencerramento.get_date()
        dados=(tb3_nome_banco,tb3_datainicio,tb3_datatermino,tb3_fob)
        conexao=mysql.connector.connect(
            host='localhost',
            port='1200',
            user='root',
            password='alunolab',
            database='tcc'
        )
        cursor=conexao.cursor()
        comando=f'insert into evento(nome,data_inicio,data_termino,imagem) values (%s,%s,%s,%s)'
        cursor.execute(comando,dados)
        conexao.commit()
        try:
            messagebox.showinfo('Sucesso','O Evento foi Inserido com Sucesso')
            tb3_entry_nome.delete(0,END)
            tb3_cal_dataInicio.delete(0,END)
            tb3_cal_dataencerramento.delete(0,END)
            tb3_label_carregaimagem.configure(image="")
            data=dt.datetime.now()
            data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
            arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
            arquivo.writelines("\n"+data_texto+" || Evento Inserido com Sucesso")
            arquivo.close()
        except mysql.connector.errors.ProgrammingError:
            messagebox.showerror('Erro','Erro ao Inserir Evento')
            data=dt.datetime.now()
            data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
            arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
            arquivo.writelines("\n"+data_texto+" || Erro ao Inserir Evento")
            arquivo.close()
        finally:
            tb3_popular()
            cursor.close()
            conexao.close()
def tb5_salvar():
    global tb5_login_banco,tb5_senha_banco,tb5_nivel_banco,tb5_email_banco
    tb5_login_banco=tb5_login.get()
    tb5_senha_banco=tb5_senha.get()
    tb5_nivel_banco=tb5_nivel.get()
    tb5_email_banco=tb5_email.get()
    dados=(tb5_login_banco,tb5_senha_banco,tb5_nivel_banco,tb5_email_banco)
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f'insert into entrada(login,senha,nivel,email) values (%s,%s,%s,%s)'
    cursor.execute(comando,dados)
    conexao.commit()
    try:
        messagebox.showinfo('Sucesso','O Login foi Inserido com Sucesso')
        tb5_login.delete(0,END)
        tb5_senha.delete(0,END)
        tb5_nivel.delete(0,END)
        tb5_email.delete(0,END)
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Login Inserido com Sucesso")
        arquivo.close()
    except mysql.connector.errors.ProgrammingError:
        messagebox.showerror('Erro','Erro ao Inserir Login')
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Erro ao Inserir Login")
        arquivo.close()
    finally:
        tb5_popular()
        cursor.close()
        conexao.close()
def pesquisar():
    tv.delete(*tv.get_children())
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando="select id,nome,tipo,andar,bloco from ambiente where nome like '"+nome_consulta.get()+"%'"
    cursor.execute(comando)
    resultado=cursor.fetchall()
    for linha in resultado:
        tv.insert("","end",values=linha)
def tb2_pesquisar():
    tb2_tv.delete(*tb2_tv.get_children())
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando="select id,nome,sala,ano,andar,bloco from turma where nome like '"+tb2_nome_consulta.get()+"%'"
    cursor.execute(comando)
    resultado=cursor.fetchall()
    for linha in resultado:
        tb2_tv.insert("","end",values=linha)
def tb3_pesquisar():
    tb3_tv.delete(*tb3_tv.get_children())
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando="select id,nome,data_inicio,data_termino from evento where nome like '"+tb3_nome_consulta.get()+"%'"
    cursor.execute(comando)
    resultado=cursor.fetchall()
    for linha in resultado:
        tb3_tv.insert("","end",values=linha)
def tb5_pesquisar():
    tb5_tv.delete(*tb5_tv.get_children())
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando="select login,password(senha) as senha,nivel,email from entrada where login like '"+tb5_login_consulta.get()+"%'"
    cursor.execute(comando)
    resultado=cursor.fetchall()
    for linha in resultado:
        tb5_tv.insert("","end",values=linha)
def getrow(event):
    from PIL import Image, ImageTk
    import PIL
    import io
    global id_exclude,id_exclude1,id_exclusao
    nome.delete(0,END)
    tipo.delete(0,END)
    andar.delete(0,END)
    bloco.delete(0,END)
    item=tv.item(tv.focus())
    id_exclude= 0,item['values'] [0]
    id_exclusao= int(''.join(map(str,id_exclude)))
    nome.insert(0,item['values'] [1])
    tipo.insert(0,item['values'] [2])
    andar.insert(0,item['values'] [3])
    bloco.insert(0,item ['values'] [4])
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f'select imagem from ambiente where nome="{nome.get()}"'
    cursor.execute(comando)
    resultado=cursor.fetchall()
    imagem=resultado[0][0]
    img=PIL.Image.open(io.BytesIO(imagem))
    img.thumbnail((350,350))
    img=PIL.ImageTk.PhotoImage(img)
    label6.configure(image=img)
    label6.image=img
def tb2_getrow(event):
    global tb2_id_exclude,tb2_id_exclusao
    tb2_nome.delete(0,END)
    tb2_andar.delete(0,END)
    tb2_ano.delete(0,END)
    tb2_bloco.delete(0,END)
    tb2_Sala.delete(0,END)
    tb2_item=tb2_tv.item(tb2_tv.focus())
    tb2_id_exclude= 0,tb2_item['values'] [0]
    tb2_id_exclusao= int(''.join(map(str,tb2_id_exclude)))
    tb2_nome.insert(0,tb2_item['values'] [1])
    tb2_Sala.insert(0,tb2_item['values'] [2])
    tb2_ano.insert(0,tb2_item['values'] [3])
    tb2_andar.insert(0,tb2_item['values'] [4])
    tb2_bloco.insert(0,tb2_item['values'] [5])
def tb3_getrow(event):
    from PIL import Image, ImageTk
    import PIL
    import io
    global tb3_id_exclude,tb3_id_exclusao
    tb3_entry_nome.delete(0,END)
    tb3_cal_dataInicio.delete(0,END)
    tb3_cal_dataencerramento.delete(0,END)
    tb3_item=tb3_tv.item(tb3_tv.focus())
    tb3_id_exclude= 0,tb3_item['values'] [0]
    tb3_id_exclusao= int(''.join(map(str,tb3_id_exclude)))
    tb3_entry_nome.insert(0,tb3_item['values'] [1])
    tb3_cal_dataInicio.insert(0,tb3_item['values'] [2])
    tb3_cal_dataencerramento.insert(0,tb3_item['values'] [3])
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f'select imagem from evento where nome="{tb3_entry_nome.get()}"'
    cursor.execute(comando)
    resultado=cursor.fetchall()
    imagem=resultado[0][0]
    img=PIL.Image.open(io.BytesIO(imagem))
    img.thumbnail((350,350))
    img=PIL.ImageTk.PhotoImage(img)
    tb3_label_carregaimagem.configure(image=img)
    tb3_label_carregaimagem.image=img
def tb5_getrow(event):
    from PIL import Image, ImageTk
    import PIL
    import io
    global tb5_id_exclude,tb5_id_exclusao
    tb5_login.delete(0,END)
    tb5_senha.delete(0,END)
    tb5_nivel.delete(0,END)
    tb5_email.delete(0,END)
    tb5_item=tb5_tv.item(tb5_tv.focus())
    tb5_login.insert(0,tb5_item['values'] [0])
    tb5_senha.insert(0,tb5_item['values'] [1])
    tb5_nivel.insert(0,tb5_item['values'] [2])
    tb5_email.insert(0,tb5_item['values'] [3])
def adicionar():
    nome.delete(0,END)
    tipo.delete(0,END)
    andar.delete(0,END)
    bloco.delete(0,END)
    label6.configure(image="")
def tb2_adicionar():
    tb2_nome.delete(0,END)
    tb2_andar.delete(0,END)
    tb2_ano.delete(0,END)
    tb2_bloco.delete(0,END)
    tb2_Sala.delete(0,END)
def tb3_adicionar():
    tb3_entry_nome.delete(0,END)
    tb3_cal_dataInicio.delete(0,END)
    tb3_cal_dataencerramento.delete(0,END)
    tb3_label_carregaimagem.configure(image="")
def tb5_adicionar():
    tb5_login.delete(0,END)
    tb5_senha.delete(0,END)
    tb5_nivel.delete(0,END)
    tb5_email.delete(0,END)
def excluir():
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f'delete from ambiente where id="{id_exclusao}"'
    cursor.execute(comando)
    conexao.commit()
    try:
        messagebox.showinfo('Sucesso','O Ambiente foi Excluído com Sucesso')
        nome.delete(0,END)
        tipo.delete(0,END)
        andar.delete(0,END)
        bloco.delete(0,END)
        label6.configure(image="")
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Ambiente Excluído com Sucesso")
        arquivo.close()
    except mysql.connector.errors.ProgrammingError:
        messagebox.showerror('Erro','Erro ao Excluir Ambiente')
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Erro ao Excluir Ambiente")
        arquivo.close()
    finally:
        popular()
        cursor.close()
        conexao.close()
def tb2_excluir():
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f'delete from turma where id="{tb2_id_exclusao}"'
    cursor.execute(comando)
    conexao.commit()
    try:
        messagebox.showinfo('Sucesso','A Turma foi Excluída com Sucesso')
        tb2_nome.delete(0,END)
        tb2_andar.delete(0,END)
        tb2_ano.delete(0,END)
        tb2_bloco.delete(0,END)
        tb2_Sala.delete(0,END)
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Turma Excluída com Sucesso")
        arquivo.close()
    except mysql.connector.errors.ProgrammingError:
        messagebox.showerror('Erro','Erro ao Excluir Turma')
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Erro ao Excluir Turma")
        arquivo.close()
    finally:
        tb2_popular()
        cursor.close()
        conexao.close()
def tb3_excluir():
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f'delete from evento where id="{tb3_id_exclusao}"'
    cursor.execute(comando)
    conexao.commit()
    try:
        messagebox.showinfo('Sucesso','O Evento foi Excluído com Sucesso')
        tb3_entry_nome.delete(0,END)
        tb3_cal_dataInicio.delete(0,END)
        tb3_cal_dataencerramento.delete(0,END)
        tb3_label_carregaimagem.configure(image="")
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Evento Excluído com Sucesso")
        arquivo.close()
    except mysql.connector.errors.ProgrammingError:
        messagebox.showerror('Erro','Erro ao Excluir Evento')
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Erro ao Excluir Evento")
        arquivo.close()
    finally:
        tb3_popular()
        cursor.close()
        conexao.close()
def tb5_excluir():
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f'delete from entrada where login="{tb5_login.get()}"'
    cursor.execute(comando)
    conexao.commit()
    try:
        messagebox.showinfo('Sucesso','O Login foi Excluído com Sucesso')
        tb5_login.delete(0,END)
        tb5_senha.delete(0,END)
        tb5_nivel.delete(0,END)
        tb5_email.delete(0,END)
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Login Excluído com Sucesso")
        arquivo.close()
    except mysql.connector.errors.ProgrammingError:
        messagebox.showerror('Erro','Erro ao Excluir Login')
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Erro ao Excluir Login")
        arquivo.close()
    finally:
        tb5_popular()
        cursor.close()
        conexao.close()
def atualizar():
    fob= open(get_image,'rb')
    fob=fob.read()
    dados=(nome.get(),tipo.get(),andar.get(),bloco.get(),fob)
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f'update ambiente set nome=%s, tipo=%s, andar=%s, bloco=%s,imagem=%s where id="{id_exclusao}"'
    cursor.execute(comando,dados)
    try:
        conexao.commit()
        messagebox.showinfo('Sucesso','O Ambiente foi Atualizado com Sucesso')
        nome.delete(0,END)
        tipo.delete(0,END)
        andar.delete(0,END)
        bloco.delete(0,END)
        label6.configure(image="")
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Ambiente Atualizado com Sucesso")
        arquivo.close()
    except mysql.connector.errors.ProgrammingError:
        messagebox.showerror('Erro','Erro ao Atualizar Ambiente')
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Erro ao Atualizar Ambiente")
        arquivo.close()
    except NameError:
        return "Ocorreu um erro na nomeação de um método ou variável"
    finally:
        popular()
        cursor.close()
        conexao.close()
def tb2_atualizar():
    dados=(tb2_nome.get(),tb2_Sala.get(),tb2_ano.get(),tb2_andar.get(),tb2_bloco.get())
    conexao=mysql.connector.connect(
        host='localhost',
        port='1200',
        user='root',
        password='alunolab',
        database='tcc'
    )
    cursor=conexao.cursor()
    comando=f'update turma set nome=%s, sala=%s, ano=%s, andar=%s, bloco=%s where id="{tb2_id_exclusao}"'
    cursor.execute(comando,dados)
    try:
        conexao.commit()
        messagebox.showinfo('Sucesso','A turma foi Atualizada com Sucesso')
        tb2_nome.delete(0,END)
        tb2_andar.delete(0,END)
        tb2_ano.delete(0,END)
        tb2_bloco.delete(0,END)
        tb2_Sala.delete(0,END)
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Turma Atualizada com Sucesso")
        arquivo.close()
    except mysql.connector.errors.ProgrammingError:
        messagebox.showerror('Erro','Erro ao Atualizar Turma')
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Erro ao Atualizar Turma")
        arquivo.close()
    except NameError:
        return "Ocorreu um erro na nomeação de um método ou variável"
    finally:
        tb2_popular()
        cursor.close()
        conexao.close()
def tb3_atualizar():
    tb3_fob= open(tb3_get_image,'rb')
    tb3_fob=tb3_fob.read()
    tb3_data_inicial=datetime.strptime(str(tb3_cal_dataInicio.get_date()),"%Y-%m-%d")
    tb3_data_final=datetime.strptime(str(tb3_cal_dataencerramento.get_date()),"%Y-%m-%d")
    dados=(tb3_entry_nome.get(),tb3_cal_dataInicio.get(),tb3_cal_dataencerramento.get(),tb3_fob)
    if(tb3_data_inicial>tb3_data_final):
        messagebox.showerror('Erro','Data de Início não pode ser maior que a Data Final')
    else:
        conexao=mysql.connector.connect(
            host='localhost',
            port='1200',
            user='root',
            password='alunolab',
            database='tcc'
        )
        cursor=conexao.cursor()
        comando=f'update evento set nome=%s, data_inicio=%s, data_termino=%s, imagem=%s where id="{tb3_id_exclusao}"'
        cursor.execute(comando,dados)
        try:
            conexao.commit()
            messagebox.showinfo('Sucesso','O Evento foi Atualizado com Sucesso')
            tb3_entry_nome.delete(0,END)
            tb3_cal_dataInicio.delete(0,END)
            tb3_cal_dataencerramento.delete(0,END)
            tb3_label_carregaimagem.configure(image="")
            data=dt.datetime.now()
            data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
            arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
            arquivo.writelines("\n"+data_texto+" || Evento Atualizado com Sucesso")
            arquivo.close()
        except mysql.connector.errors.ProgrammingError:
            messagebox.showerror('Erro','Erro ao Atualizar Evento')
            data=dt.datetime.now()
            data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
            arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
            arquivo.writelines("\n"+data_texto+" || Erro ao Atualizar Evento")
            arquivo.close()
        except NameError:
            return "Ocorreu um erro na nomeação de um método ou variável"
        finally:
            tb3_popular()
            cursor.close()
            conexao.close()
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
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"\\logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Erro ao Criar Backup")
        arquivo.close()
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
        os.system("mysql -uroot -P1200 -palunolab< "+file_restaurar)
        messagebox.showinfo("Sucesso","Backup Restaurado com Sucesso!")
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open("logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Backup Restaurado com Sucesso")
        arquivo.close()
    if(file_restaurar==""):
        messagebox.showerror("Erro","Erro ao Restaurar Backup")
        data=dt.datetime.now()
        data_texto=data.strftime("%d/%m/%Y %H:%M:%S")
        arquivo = open(pastaApp+"logs\\arquivo.log", "a")
        arquivo.writelines("\n"+data_texto+" || Erro ao Restaurar Backup")
        arquivo.close()

def tb4_filtro(event):
    tb4_Escolha.place(x=330,y=100,width=150,height=30)
    tb4_botao1.place(x=330,y=140,width=220,height=50)
    if(tb4_area.get()=="Eventos"):
        tb4_Escolha.configure(values=["Nome","Data"])
        tb4_cal_datainicio.configure(state="normal")
    else:
        tb4_cal_datainicio.configure(state="disabled")
        tb4_Escolha.configure(values=["Nome"])
def gerarRelatorio():
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4,letter
    from reportlab.lib.units import inch
    from  datetime import date,datetime
    if(tb4_area.get()=="Ambientes" and tb4_Escolha.get()=="Nome"):
        conexao=mysql.connector.connect(
            host='localhost',
            port='1200',
            user='root',
            password='alunolab',
            database='tcc'
        )
        cursor=conexao.cursor()
        comando="select id,nome,tipo,andar,bloco from ambiente where nome like'"+tb4_texto.get()+"%'"
        cursor.execute(comando)
        resultado=cursor.fetchall()
        for linha in resultado:
            print(linha)
        try:
            global file
            file=tkinter.filedialog.asksaveasfilename(defaultextension='.pdf',filetypes=[("PDF File",".pdf")])
            if(file !=""):
                cnv=canvas.Canvas(file,pagesize=letter)
                cnv.setFillColorRGB(1,0,0)
                cnv.setFont("Helvetica", 40)
                cnv.drawRightString(7*inch,7.5*inch,'Relatório de Ambientes')
                cnv.setFillColorRGB(0,0,0)
                cnv.setFont("Helvetica", 24)
                cnv.drawRightString(2.5*inch,6.8*inch,'ID:')
                cnv.drawRightString(2.5*inch,6*inch,'Nome:')
                cnv.drawRightString(2.5*inch,5*inch,'Tipo:')
                cnv.drawRightString(2.5*inch,4*inch,'Andar:')
                cnv.drawRightString(2.5*inch,3*inch,'Bloco:')
                cnv.setFillColorRGB(0,0,1)
                cnv.setFont("Helvetica", 20)
                cnv.drawString(3*inch,6.8*inch,str(linha[0]))
                cnv.drawString(3*inch,6*inch,str(linha[1]))
                cnv.drawString(3*inch,5*inch,str(linha[2]))
                cnv.drawString(3*inch,4*inch,str(linha[3]))
                cnv.drawString(3*inch,3*inch,str(linha[4]))
                cnv.setFont("Helvetica", 14)
                cnv.setStrokeColorRGB(0.1,0.8,0.1)
                cnv.setFillColorRGB(0,0,1) # font colour
                cnv.drawImage(pastaApp+"\\img\\robo_img.png",0*inch,9.3*inch) 
                cnv.drawString(0, 9*inch, "Acesso Restrito")
                cnv.drawString(0, 8.7*inch, "Rio de Janeiro - RJ")
                cnv.setFillColorRGB(0,0.5,1) # font colour
                cnv.drawString(2.5*inch, 8.7*inch, "Escola Firjan Senai Sesi")
                cnv.setFillColorRGB(0,0,0) # font colour
                cnv.line(0,8.6*inch,7.3*inch,8.6*inch)
                dt = date.today().strftime('%d/%m/%Y') 
                cnv.drawString(5.6*inch,9.3*inch,dt) 
                cnv.setFont("Helvetica", 8)
                cnv.drawString(3*inch,9.6*inch,'Relatório de Ambientes')
                cnv.line(0,-0.7*inch,6.8*inch,-0.7*inch)
                cnv.setFillColorRGB(1,0,0) 
                cnv.drawString(6.4, -0.9*inch, u"\u00A9"+"Escola Firjan Senai Sesi")
                cnv.rotate(45)
                cnv.setFillColorCMYK(0,0,0,0.08) 
                cnv.setFont("Helvetica", 100)
                cnv.rotate(-45)
                cnv.save()
                messagebox.showinfo("Sucesso","PDF Gerado com Sucesso!")
            if(file==""):
                messagebox.showerror("Erro","Erro ao Gerar Relatório")
        except:
            messagebox.showerror("Erro","Erro ao Criar PDF!")
            return
    if(tb4_area.get()=="Turmas" and tb4_Escolha.get()=="Nome"):
        conexao2=mysql.connector.connect(
            host='localhost',
            port='1200',
            user='root',
            password='alunolab',
            database='tcc'
        )
        cursor2=conexao2.cursor()
        comando2="select id,nome,sala,ano,andar,bloco from turma where nome like'"+tb4_texto.get()+"%'"
        cursor2.execute(comando2)
        resultado2=cursor2.fetchall()
        for linha2 in resultado2:
            print(linha2)
        try:
            global file2
            file2=tkinter.filedialog.asksaveasfilename(defaultextension='.pdf',filetypes=[("PDF File",".pdf")])
            if(file2 !=""):
                cnv=canvas.Canvas(file2,pagesize=letter)
                cnv.setFillColorRGB(1,0,0)
                cnv.setFont("Helvetica", 40)
                cnv.drawRightString(7*inch,7.5*inch,'Relatório de Turmas')
                cnv.setFillColorRGB(0,0,0)
                cnv.setFont("Helvetica", 24)
                cnv.drawRightString(2.5*inch,6.8*inch,'ID:')
                cnv.drawRightString(2.5*inch,6*inch,'Nome:')
                cnv.drawRightString(2.5*inch,5*inch,'Sala:')
                cnv.drawRightString(2.5*inch,4*inch,'Ano:')
                cnv.drawRightString(2.5*inch,3*inch,'Andar:')
                cnv.drawRightString(2.5*inch,2*inch,'Bloco:')
                cnv.setFillColorRGB(0,0,1)
                cnv.setFont("Helvetica", 20)
                cnv.drawString(3*inch,6.8*inch,str(linha2[0]))
                cnv.drawString(3*inch,6*inch,str(linha2[1]))
                cnv.drawString(3*inch,5*inch,str(linha2[2]))
                cnv.drawString(3*inch,4*inch,str(linha2[3]))
                cnv.drawString(3*inch,3*inch,str(linha2[4]))
                cnv.drawString(3*inch,2*inch,str(linha2[5]))
                cnv.setFont("Helvetica", 14)
                cnv.setStrokeColorRGB(0.1,0.8,0.1)
                cnv.setFillColorRGB(0,0,1) # font colour
                cnv.drawImage(pastaApp+"\\img\\robo_img.png",0*inch,9.3*inch) 
                cnv.drawString(0, 9*inch, "Acesso Restrito")
                cnv.drawString(0, 8.7*inch, "Rio de Janeiro - RJ")
                cnv.setFillColorRGB(0,0.5,1) # font colour
                cnv.drawString(2.5*inch, 8.7*inch, "Escola Firjan Senai Sesi")
                cnv.setFillColorRGB(0,0,0) # font colour
                cnv.line(0,8.6*inch,7.3*inch,8.6*inch)
                dt = date.today().strftime('%d/%m/%Y') 
                cnv.drawString(5.6*inch,9.3*inch,dt) 
                cnv.setFont("Helvetica", 8)
                cnv.drawString(3*inch,9.6*inch,'Relatório de Turmas')
                cnv.line(0,-0.7*inch,6.8*inch,-0.7*inch)
                cnv.setFillColorRGB(1,0,0) 
                cnv.drawString(6.4, -0.9*inch, u"\u00A9"+"Escola Firjan Senai Sesi")
                cnv.rotate(45)
                cnv.setFillColorCMYK(0,0,0,0.08) 
                cnv.setFont("Helvetica", 100)
                cnv.rotate(-45)
                cnv.save()
                messagebox.showinfo("Sucesso","PDF Gerado com Sucesso!")
            if(file2==""):
                messagebox.showerror("Erro","Erro ao Gerar Relatório")
        except:
            messagebox.showerror("Erro","Erro ao Criar PDF!")
            return
    if(tb4_area.get()=="Eventos" and tb4_Escolha.get()=="Nome"):
        conexao3=mysql.connector.connect(
            host='localhost',
            port='1200',
            user='root',
            password='alunolab',
            database='tcc'
        )
        cursor3=conexao3.cursor()
        comando3="select id,nome,data_inicio,data_termino from evento where nome like'"+tb4_texto.get()+"%'"
        cursor3.execute(comando3)
        resultado3=cursor3.fetchall()
        for linha3 in resultado3:
            print(linha3)
        try:
            global file3
            file3=tkinter.filedialog.asksaveasfilename(defaultextension='.pdf',filetypes=[("PDF File",".pdf")])
            if(file3!=""):
                data_inicial1=datetime.strptime(str(linha3[2]),'%Y-%m-%d')
                data_final1=datetime.strptime(str(linha3[3]),'%Y-%m-%d')
                data_inicial=datetime.strftime(data_inicial1,'%d/%m/%Y')
                data_final=datetime.strftime(data_final1,'%d/%m/%Y')
                cnv=canvas.Canvas(file3,pagesize=letter)
                cnv.setFillColorRGB(1,0,0)
                cnv.setFont("Helvetica", 40)
                cnv.drawRightString(7*inch,7.5*inch,'Relatório de Eventos')
                cnv.setFillColorRGB(0,0,0)
                cnv.setFont("Helvetica", 24)
                cnv.drawRightString(2.5*inch,6.8*inch,'ID:')
                cnv.drawRightString(2.5*inch,6*inch,'Nome:')
                cnv.drawRightString(2.5*inch,5*inch,'Data Inicial:')
                cnv.drawRightString(2.5*inch,4*inch,'Data Final:')
                cnv.setFillColorRGB(0,0,1)
                cnv.setFont("Helvetica", 20)
                cnv.drawString(3*inch,6.8*inch,str(linha3[0]))
                cnv.drawString(3*inch,6*inch,str(linha3[1]))
                cnv.drawString(3*inch,5*inch,str(data_inicial))
                cnv.drawString(3*inch,4*inch,str(data_final))
                cnv.setFont("Helvetica", 14)
                cnv.setStrokeColorRGB(0.1,0.8,0.1)
                cnv.setFillColorRGB(0,0,1) # font colour
                cnv.drawImage(pastaApp+"\\img\\robo_img.png",0*inch,9.3*inch) 
                cnv.drawString(0, 9*inch, "Acesso Restrito")
                cnv.drawString(0, 8.7*inch, "Rio de Janeiro - RJ")
                cnv.setFillColorRGB(0,0.5,1) # font colour
                cnv.drawString(2.5*inch, 8.7*inch, "Escola Firjan Senai Sesi")
                cnv.setFillColorRGB(0,0,0) # font colour
                cnv.line(0,8.6*inch,7.3*inch,8.6*inch)
                dt = date.today().strftime('%d/%m/%Y') 
                cnv.drawString(5.6*inch,9.3*inch,dt) 
                cnv.setFont("Helvetica", 8)
                cnv.drawString(3*inch,9.6*inch,'Relatório de Eventos')
                cnv.line(0,-0.7*inch,6.8*inch,-0.7*inch)
                cnv.setFillColorRGB(1,0,0) 
                cnv.drawString(6.4, -0.9*inch, u"\u00A9"+"Escola Firjan Senai Sesi")
                cnv.rotate(45)
                cnv.setFillColorCMYK(0,0,0,0.08) 
                cnv.setFont("Helvetica", 100)
                cnv.rotate(-45)
                cnv.save()
                messagebox.showinfo("Sucesso","PDF Gerado com Sucesso!")
            if(file3==""):
                messagebox.showerror("Erro","Erro ao Gerar Relatório")
        except:
            messagebox.showerror("Erro","Erro ao Criar PDF!")
            return
    if(tb4_area.get()=="Eventos" and tb4_Escolha.get()=="Data"):
        conexao4=mysql.connector.connect(
            host='localhost',
            port='1200',
            user='root',
            password='alunolab',
            database='tcc'
        )
        cursor4=conexao4.cursor()
        comando4=f'select id,nome,data_inicio,data_termino from evento where data_inicio="{tb4_cal_datainicio.get_date()}"'
        cursor4.execute(comando4)
        resultado4=cursor4.fetchall()
        for linha4 in resultado4:
            print(linha4)
        try:
            global file4
            file4=tkinter.filedialog.asksaveasfilename(defaultextension='.pdf',filetypes=[("PDF File",".pdf")])
            if(file4!=""):
                data_inicial1=datetime.strptime(str(linha4[2]),'%Y-%m-%d')
                data_final1=datetime.strptime(str(linha4[3]),'%Y-%m-%d')
                data_inicial=datetime.strftime(data_inicial1,'%d/%m/%Y')
                data_final=datetime.strftime(data_final1,'%d/%m/%Y')
                cnv=canvas.Canvas(file4,pagesize=letter)
                cnv.setFillColorRGB(1,0,0)
                cnv.setFont("Helvetica", 40)
                cnv.drawRightString(7*inch,7.5*inch,'Relatório de Eventos')
                cnv.setFillColorRGB(0,0,0)
                cnv.setFont("Helvetica", 24)
                cnv.drawRightString(2.5*inch,6.8*inch,'ID:')
                cnv.drawRightString(2.5*inch,6*inch,'Nome:')
                cnv.drawRightString(2.5*inch,5*inch,'Data Inicial:')
                cnv.drawRightString(2.5*inch,4*inch,'Data Final:')
                cnv.setFillColorRGB(0,0,1)
                cnv.setFont("Helvetica", 20)
                cnv.drawString(3*inch,6.8*inch,str(linha4[0]))
                cnv.drawString(3*inch,6*inch,str(linha4[1]))
                cnv.drawString(3*inch,5*inch,str(data_inicial))
                cnv.drawString(3*inch,4*inch,str(data_final))
                cnv.setFont("Helvetica", 14)
                cnv.setStrokeColorRGB(0.1,0.8,0.1)
                cnv.setFillColorRGB(0,0,1) # font colour
                cnv.drawImage(pastaApp+"\\img\\robo_img.png",0*inch,9.3*inch) 
                cnv.drawString(0, 9*inch, "Acesso Restrito")
                cnv.drawString(0, 8.7*inch, "Rio de Janeiro - RJ")
                cnv.setFillColorRGB(0,0.5,1) # font colour
                cnv.drawString(2.5*inch, 8.7*inch, "Escola Firjan Senai Sesi")
                cnv.setFillColorRGB(0,0,0) # font colour
                cnv.line(0,8.6*inch,7.3*inch,8.6*inch)
                dt = date.today().strftime('%d/%m/%Y') 
                cnv.drawString(5.6*inch,9.3*inch,dt) 
                cnv.setFont("Helvetica", 8)
                cnv.drawString(3*inch,9.6*inch,'Relatório de Eventos')
                cnv.line(0,-0.7*inch,6.8*inch,-0.7*inch)
                cnv.setFillColorRGB(1,0,0) 
                cnv.drawString(6.4, -0.9*inch, u"\u00A9"+"Escola Firjan Senai Sesi")
                cnv.rotate(45)
                cnv.setFillColorCMYK(0,0,0,0.08) 
                cnv.setFont("Helvetica", 100)
                cnv.rotate(-45)
                cnv.save()
                messagebox.showinfo("Sucesso","PDF Gerado com Sucesso!")
            if(file4==""):
                messagebox.showerror("Erro","Erro ao Gerar Relatório")
        except:
            messagebox.showerror("Erro","Erro ao Criar PDF!")
            return

btn_menu=PhotoImage(file="img\\menu.png")
btn_fechar=PhotoImage(file="img\\fechar.png")
btn_cadastrar=PhotoImage(file="img\\cadastro.png")
btn_aluno=PhotoImage(file="img\\aluno.png")
btn_relatorio=PhotoImage(file="img\\pdf.png")
btn_backup=PhotoImage(file="img\\backup.png")
btn_criaconta=PhotoImage(file="img\\adicionar.png")
btn_evento=PhotoImage(file="img\\evento.png")
btn_adicionar=PhotoImage(file="img\\adicao.png")
btn_salvar=PhotoImage(file="img\\salvar.png")
btn_excluir=PhotoImage(file="img\\excluir.png")
btn_atualizar=PhotoImage(file="img\\atualizar.png")
btn_consulta=PhotoImage(file="img\\lupa.png")
btn_criarbackup=PhotoImage(file="img\\otimizacao.png")
btn_enviar=PhotoImage(file="img\\enviar.png")

nb=ttk.Notebook(app)
nb.place(x=0,y=0,width=680,height=640)

tb1=Frame(nb)
nb.add(tb1,image=btn_cadastrar,compound="left",text="Ambientes")

label6=tkinter.Label(tb1)
label6.place(x=190,y=130,width=300,height=180)

label1=Label(tb1,text="Nome:",foreground="black",font=("Century Gothic", 14, font.BOLD))
label1.place(x=30,y=10,width=90,height=30)

nome=Entry(tb1,foreground="black",font=("Arial", 12))
nome.place(x=115,y=10,width=200,height=30)

label2=Label(tb1,text="Tipo:",foreground="black",font=("Century Gothic", 14, font.BOLD))
label2.place(x=290,y=10,width=90,height=30)

listTipo=["Sala","Ambiente","Estoque","Outros"]
tipo=ttk.Combobox(tb1,values=listTipo,font=("Arial", 12))
tipo.set("Sala")
tipo.place(x=370,y=10,width=175,height=30)

label3=Label(tb1,text="Andar:",foreground="black",font=("Century Gothic", 14, font.BOLD))
label3.place(x=30,y=50,width=90,height=30)

listAndar=["Acesso", "2","3","4"]
andar=ttk.Combobox(tb1,values=listAndar,font=("Arial", 12))
andar.set("Acesso")
andar.place(x=115,y=50,width=175,height=30)

label4=Label(tb1,text="Bloco:",foreground="black",font=("Century Gothic", 14, font.BOLD))
label4.place(x=290,y=50,width=90,height=30)

listBloco=["A","B","Externo"]
bloco=ttk.Combobox(tb1,values=listBloco,font=("Arial", 12))
bloco.set("A")
bloco.place(x=370,y=50,width=175,height=30)

label5=Label(tb1,text="Imagem:",foreground="black",font=("Century Gothic", 14, font.BOLD))
label5.place(x=25,y=90,width=90,height=30)

botao1=Button(tb1,text="Abrir Imagem",foreground="black",font=("Century Gothic", 14, font.BOLD),command=abririmagem)
botao1.place(x=115,y=90,width=170,height=30)

botao2=Button(tb1,text="Adicionar",image=btn_adicionar,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=adicionar)
botao2.place(x=10,y=325,width=150,height=50)

botao3=Button(tb1,text="Salvar",image=btn_salvar,compound="left",foreground="black",command=salvar,font=("Century Gothic", 14, font.BOLD))
botao3.place(x=180,y=325,width=150,height=50)

botao4=Button(tb1,text="Excluir",image=btn_excluir,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=excluir)
botao4.place(x=350,y=325,width=150,height=50)

botao5=Button(tb1,text="Atualizar",image=btn_atualizar,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=atualizar)
botao5.place(x=520,y=325,width=150,height=50)

label7=Label(tb1,text="Digite o Nome:",foreground="black",font=("Century Gothic", 14, font.BOLD))
label7.place(x=10,y=390,width=150,height=30)

nome_consulta=Entry(tb1,foreground="black",font=("Arial", 12))
nome_consulta.place(x=170,y=390,width=200,height=35)

botao6=Button(tb1,text="Pesquisar",image=btn_consulta,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=pesquisar)
botao6.place(x=380,y=390,width=150,height=35)

scrollbary=Scrollbar(tb1,orient=VERTICAL)
scrollbary.place(x=570,y=440,width=22,height=220)

tv=ttk.Treeview(tb1,columns=('ID','Nome','Tipo','Andar','Bloco'),show='headings',yscrollcommand=scrollbary.set)
tv.column('ID',minwidth=0,width=50)
tv.column('Nome',minwidth=0,width=100)
tv.column('Tipo',minwidth=0,width=100)
tv.column('Andar',minwidth=0,width=100)
tv.column('Bloco',minwidth=0,width=100)
tv.heading('ID',text='ID')
tv.heading('Nome',text='Nome')
tv.heading('Tipo',text='Tipo')
tv.heading('Andar',text='Andar')
tv.heading('Bloco',text='Bloco')
tv.place(x=10,y=440,width=550,height=170)
scrollbary.configure(command=tv.yview)
popular()
tv.bind('<Double 1>',getrow)


tb2=Frame(nb)
nb.add(tb2,image=btn_aluno,compound="left",text="Turmas")

tb2_label1=Label(tb2,text="Nome:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb2_label1.place(x=30,y=10,width=90,height=30)

tb2_nome=Entry(tb2,foreground="black",font=("Arial", 12))
tb2_nome.place(x=115,y=10,width=200,height=30)

tb2_label2=Label(tb2,text="Ano:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb2_label2.place(x=290,y=10,width=90,height=30)

tb2_listAno=["1º Ano EM","2º Ano EM","3º Ano EM"]
tb2_ano=ttk.Combobox(tb2,values=tb2_listAno,font=("Arial", 12))
tb2_ano.set("1º Ano EM")
tb2_ano.place(x=370,y=10,width=175,height=30)

tb2_label3=Label(tb2,text="Andar:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb2_label3.place(x=30,y=50,width=90,height=30)

tb2_listAndar=["Acesso", "2","3","4"]
tb2_andar=ttk.Combobox(tb2,values=tb2_listAndar,font=("Arial", 12))
tb2_andar.set("Acesso")
tb2_andar.place(x=115,y=50,width=175,height=30)

tb2_label4=Label(tb2,text="Bloco:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb2_label4.place(x=290,y=50,width=90,height=30)

tb2_listBloco=["A","B"]
tb2_bloco=ttk.Combobox(tb2,values=tb2_listBloco,font=("Arial", 12))
tb2_bloco.set("A")
tb2_bloco.place(x=370,y=50,width=175,height=30)

tb2_label5=Label(tb2,text="Sala:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb2_label5.place(x=30,y=90,width=90,height=30)

conexao=mysql.connector.connect(
    host='localhost',
    port='1200',
    user='root',
    password='alunolab',
    database='tcc'
)
cursor=conexao.cursor()
comando="select nome from ambiente where tipo='sala'"
cursor.execute(comando)
resultado=cursor.fetchall()
tb2_listSala=[linha[0] for linha in resultado]
tb2_Sala=ttk.Combobox(tb2,values=tb2_listSala,font=("Arial", 12))
tb2_Sala.set("Pedagogia")
tb2_Sala.place(x=115,y=90,width=175,height=30)

tb2_botao2=Button(tb2,text="Adicionar",image=btn_adicionar,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb2_adicionar)
tb2_botao2.place(x=10,y=250,width=150,height=50)

tb2_botao3=Button(tb2,text="Salvar",image=btn_salvar,compound="left",foreground="black",command=tb2_salvar,font=("Century Gothic", 14, font.BOLD))
tb2_botao3.place(x=180,y=250,width=150,height=50)

tb2_botao4=Button(tb2,text="Excluir",image=btn_excluir,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb2_excluir)
tb2_botao4.place(x=350,y=250,width=150,height=50)

tb2_botao5=Button(tb2,text="Atualizar",image=btn_atualizar,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb2_atualizar)
tb2_botao5.place(x=520,y=250,width=150,height=50)

tb2_label7=Label(tb2,text="Digite o Nome:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb2_label7.place(x=10,y=320,width=150,height=30)

tb2_nome_consulta=Entry(tb2,foreground="black",font=("Arial", 12))
tb2_nome_consulta.place(x=170,y=320,width=200,height=35)

tb2_botao6=Button(tb2,text="Pesquisar",image=btn_consulta,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb2_pesquisar)
tb2_botao6.place(x=380,y=320,width=150,height=35)

scrollbary=Scrollbar(tb2,orient=VERTICAL)
scrollbary.place(x=570,y=380,width=22,height=280)

tb2_tv=ttk.Treeview(tb2,columns=('ID','Nome','Sala','Ano','Andar','Bloco'),show='headings',yscrollcommand=scrollbary.set)
tb2_tv.column('ID',minwidth=0,width=50)
tb2_tv.column('Nome',minwidth=0,width=100)
tb2_tv.column('Sala',minwidth=0,width=100)
tb2_tv.column('Ano',minwidth=0,width=100)
tb2_tv.column('Andar',minwidth=0,width=100)
tb2_tv.column('Bloco',minwidth=0,width=100)
tb2_tv.heading('ID',text='ID')
tb2_tv.heading('Nome',text='Nome')
tb2_tv.heading('Sala',text='Sala')
tb2_tv.heading('Ano',text='Ano')
tb2_tv.heading('Andar',text='Andar')
tb2_tv.heading('Bloco',text='Bloco')
tb2_tv.place(x=10,y=380,width=550,height=220)
scrollbary.configure(command=tb2_tv.yview)
tb2_popular()
tb2_tv.bind('<Double 1>',tb2_getrow)

tb3=Frame(nb)
nb.add(tb3,image=btn_evento,compound="left",text="Eventos")

tb3_label_nome=Label(tb3,text="Nome:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb3_label_nome.place(x=30,y=10,width=90,height=30)

tb3_entry_nome=Entry(tb3,foreground="black",font=("Arial", 12))
tb3_entry_nome.place(x=115,y=10,width=200,height=30)

tb3_label_dataInicio=Label(tb3,text="Data Inicial:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb3_label_dataInicio.place(x=320,y=10,width=150,height=30)

tb3_cal_dataInicio=DateEntry(tb3,selectmode='day',font=("Century Gothic", 12))
tb3_cal_dataInicio.place(x=460,y=10,width=150,height=30)

tb3_label_imagem=Label(tb3,text="Imagem:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb3_label_imagem.place(x=20,y=50,width=90,height=30)

tb3_botao1=Button(tb3,text="Abrir Imagem",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb3_abririmagem)
tb3_botao1.place(x=115,y=50,width=170,height=30)

tb3_label_dataencerramento=Label(tb3,text="Data Final:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb3_label_dataencerramento.place(x=300,y=50,width=180,height=30)

tb3_cal_dataencerramento=DateEntry(tb3,selectmode='day',font=("Century Gothic", 12))
tb3_cal_dataencerramento.place(x=460,y=50,width=150,height=30)

tb3_label_carregaimagem=Label(tb3)
tb3_label_carregaimagem.place(x=115,y=90,width=300,height=180)

tb3_botao2=Button(tb3,text="Adicionar",image=btn_adicionar,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb3_adicionar)
tb3_botao2.place(x=10,y=325,width=150,height=50)

tb3_botao3=Button(tb3,text="Salvar",image=btn_salvar,compound="left",foreground="black",command=tb3_salvar,font=("Century Gothic", 14, font.BOLD))
tb3_botao3.place(x=180,y=325,width=150,height=50)

tb3_botao4=Button(tb3,text="Excluir",image=btn_excluir,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb3_excluir)
tb3_botao4.place(x=350,y=325,width=150,height=50)

tb3_botao5=Button(tb3,text="Atualizar",image=btn_atualizar,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb3_atualizar)
tb3_botao5.place(x=520,y=325,width=150,height=50)

tb3_label7=Label(tb3,text="Digite o Nome:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb3_label7.place(x=10,y=390,width=150,height=30)

tb3_nome_consulta=Entry(tb3,foreground="black",font=("Arial", 12))
tb3_nome_consulta.place(x=170,y=390,width=200,height=35)

tb3_botao6=Button(tb3,text="Pesquisar",image=btn_consulta,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb3_pesquisar)
tb3_botao6.place(x=380,y=390,width=150,height=35)

scrollbary=Scrollbar(tb3,orient=VERTICAL)
scrollbary.place(x=570,y=440,width=22,height=280)

tb3_tv=ttk.Treeview(tb3,columns=('ID','Nome','Data_Inicio','Data_Termino'),show='headings',yscrollcommand=scrollbary.set)
tb3_tv.column('ID',minwidth=0,width=50)
tb3_tv.column('Nome',minwidth=0,width=100)
tb3_tv.column('Data_Inicio',minwidth=0,width=100)
tb3_tv.column('Data_Termino',minwidth=0,width=100)
tb3_tv.heading('ID',text='ID')
tb3_tv.heading('Nome',text='Nome')
tb3_tv.heading('Data_Inicio',text='Data Inicial')
tb3_tv.heading('Data_Termino',text='Data Final')
tb3_tv.place(x=10,y=440,width=550,height=170)
scrollbary.configure(command=tb3_tv.yview)
tb3_popular()
tb3_tv.bind('<Double 1>',tb3_getrow)

tb4=Frame(nb)
nb.add(tb4,image=btn_relatorio,compound="left",text="Dashboard")


tb4_Label1=Label(tb4,text="Informe:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb4_Label1.place(x=10,y=50,width=100,height=30)

tb4_vfiltro=StringVar()

tb4_texto=Entry(tb4,foreground="black",font=("Century Gothic", 12))
tb4_texto.place(x=100,y=50,width=200,height=30)

tb4_cal_datainicio=DateEntry(tb4,foreground="black",font=("Century Gothic", 12),state="normal")
tb4_cal_datainicio.place(x=100,y=100,width=200,height=30)


tb4_listArea=["Ambientes","Turmas","Eventos"]
tb4_area=ttk.Combobox(tb4,values=tb4_listArea,font=("Arial", 12))
tb4_area.place(x=330,y=50,width=150,height=30)
tb4_area.bind("<<ComboboxSelected>>",tb4_filtro)

tb4_listEscolha=["Nome"]
tb4_Escolha=ttk.Combobox(tb4,values=tb4_listEscolha,font=("Arial",12))

tb4_botao1=Button(tb4,text="Gerar Relatório",image=btn_relatorio,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=gerarRelatorio)


tb5=Frame(nb)
nb.add(tb5,image=btn_criaconta,compound="left",text="Criar Conta")

tb5_label1=Label(tb5,text="Login:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb5_label1.place(x=30,y=10,width=90,height=30)

tb5_login=Entry(tb5,foreground="black",font=("Arial", 12))
tb5_login.place(x=115,y=10,width=200,height=30)

tb5_label2=Label(tb5,text="Senha:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb5_label2.place(x=290,y=10,width=90,height=30)

tb5_senha=Entry(tb5,foreground="black",font=("Arial", 12))
tb5_senha.place(x=370,y=10,width=250,height=30)

tb5_label3=Label(tb5,text="Nível:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb5_label3.place(x=30,y=50,width=90,height=30)

tb5_listNivel=["Administrador","Padrão"]
tb5_nivel=ttk.Combobox(tb5,values=tb5_listNivel,font=("Arial", 12))
tb5_nivel.set("Padrão")
tb5_nivel.place(x=115,y=50,width=175,height=30)

tb5_label4=Label(tb5,text="E-mail:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb5_label4.place(x=290,y=50,width=90,height=30)

tb5_email=Entry(tb5,foreground="black",font=("Arial", 12))
tb5_email.place(x=370,y=50,width=250,height=30)

tb5_botao1=Button(tb5,text="Adicionar",image=btn_adicionar,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb5_adicionar)
tb5_botao1.place(x=10,y=150,width=150,height=50)

tb5_botao2=Button(tb5,text="Salvar",image=btn_salvar,compound="left",foreground="black",command=tb5_salvar,font=("Century Gothic", 14, font.BOLD))
tb5_botao2.place(x=180,y=150,width=150,height=50)

tb5_botao3=Button(tb5,text="Excluir",image=btn_excluir,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb5_excluir)
tb5_botao3.place(x=350,y=150,width=150,height=50)

tb5_label5=Label(tb5,text="Digite o Login:",foreground="black",font=("Century Gothic", 14, font.BOLD))
tb5_label5.place(x=10,y=240,width=150,height=30)

tb5_login_consulta=Entry(tb5,foreground="black",font=("Arial", 12))
tb5_login_consulta.place(x=170,y=240,width=200,height=35)

tb5_botao4=Button(tb5,text="Pesquisar",image=btn_consulta,compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb5_pesquisar)
tb5_botao4.place(x=380,y=240,width=150,height=35)

tb5_scrollbary=Scrollbar(tb5,orient=VERTICAL)
tb5_scrollbary.place(x=570,y=290,width=22,height=320)

tb5_tv=ttk.Treeview(tb5,columns=('Login','Senha','Nivel','Email'),show='headings',yscrollcommand=tb5_scrollbary.set)
tb5_tv.column('Login',minwidth=0,width=50)
tb5_tv.column('Senha',minwidth=0,width=100)
tb5_tv.column('Nivel',minwidth=0,width=50)
tb5_tv.column('Email',minwidth=0,width=100)
tb5_tv.heading('Login',text='Login')
tb5_tv.heading('Senha',text='Senha')
tb5_tv.heading('Nivel',text='Nível')
tb5_tv.heading('Email',text='E-mail')
tb5_tv.place(x=10,y=290,width=550,height=320)
tb5_tv.bind('<Double 1>',tb5_getrow)
tb5_popular()

tb6=Frame(nb)
nb.add(tb6,image=btn_backup,compound="left",text="Backup")

tb6_botao1=Button(tb6,image=btn_criarbackup,text="Criar Backup",compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb6_criarbackup)
tb6_botao1.place(x=240,y=120,width=200,height=40)

tb6_botao2=Button(tb6,image=btn_enviar,text="Restaurar Backup",compound="left",foreground="black",font=("Century Gothic", 14, font.BOLD),command=tb6_restaurarbackup)
tb6_botao2.place(x=240,y=170,width=200,height=40)

app.mainloop()