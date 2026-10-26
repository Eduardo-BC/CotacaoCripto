from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


#IMportando-------------
import requestsimport json



#Cores-----
co0 = "#444466" #preto
co1 = "#feffff" #branco
co2 = "#6f9fbd" #azul
fundo = "#484f60"


#Criando a Janela-------
janela = Tk()
janela.title('')
janela.geometry('320x350')


ttk.Separator(janela,orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_cima = Frame(janela, width=320, heigth=50, bg=co1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=320, heigth=300, bg=fundo, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=2, column=0, sticky=NW)


api_link ='https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CAOA%2CBRL'

response = request.get(api_link)

#Convertendo os dados em dicionario
dados = response.json()

# USD---
valor_Dolar = float(dados['USD'])



#Configurando o frame cima-----------
#colocar imagem 
imagem = Image.open('Cripta_Python/simboloBit.jpg')
imagem = imagem.resize((30,30), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem)

#IMAGEM--------
l_icon = Label(frame_cima, image=imagem, compound=LEFT, bg = co1, relief='flat')
l_icon.place(x=10, y=10)

#NOME-------

l_nome = Label(frame_cima, text='Bitcoin Price Tracker', bg = co1,fg=co2, relief='flat', anchor='center', font=('Arial 20'))
l_nome.place(x=50, y=5)


#Configuraçoes do frame baixo---------

l_priceDoll = Label(frame_baixo, text='$10,000,00',width=14, bg = co1,fg=co2, relief='flat', anchor='center', font=('Arial 20'))
l_priceDoll.place(x=0, y=50)

l_priceEuro = Label(frame_baixo, text='$10,000,00',width=14, bg = co1,fg=co2, relief='flat', anchor='center', font=('Arial 20'))
l_priceEuro.place(x=0, y=50)

l_priceReal = Label(frame_baixo, text='$10,000,00',width=14, bg = co1,fg=co2, relief='flat', anchor='center', font=('Arial 20'))
l_priceReal.place(x=0, y=50)








janela.mainloop()