from random import randint
from tkinter import *

class Sorteio:
    def __init__(self):
        self.mensagem='SORTEADOR DE NUMERO'
        self.min_num=0
        self.max_num=100
        self.sorteia_numero()
        self.sorteio_GUI()

    def sorteia_numero(self):
        self.random_num=randint(self.min_num,self.max_num)
        print('SORTEADO O NUMERO: {}'.format(self.random_num))

    def sorteio_GUI(self):
        self.janela_sorteio=Tk()
        self.janela_sorteio.title(self.mensagem)
        self.janela_sorteio.geometry('400x110')
        self.janela_sorteio.configure(background='black')



        label1=Label(self.janela_sorteio, text='NUMERO SORTEADO:',font=('consolas',20,'italic'),background='black',foreground='white')
        label1.grid(column=0, row=0)

        self.label2=Label(self.janela_sorteio,text=self.random_num,font=('consolas',35,'bold'),background='black',foreground='red')
        self.label2.grid(column=1, row=0)

        label3=Label(self.janela_sorteio, text='SORTEAR OUTRO NUMERO ? ',font=('consolas',18),background='black',foreground='white')
        label3.grid(column=0, row= 1)

        btn1=Button(text='SIM', font=('arial',18,'bold'), command=self.inserir_numero)
        btn1.grid(column=1, row=1)

        self.janela_sorteio.mainloop()
    
    def inserir_numero(self):
        self.sorteia_numero()
        self.label2.config(text=self.random_num)

sortear=Sorteio()