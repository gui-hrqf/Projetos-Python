from tkinter import *
from tkinter import messagebox

class calculadoraIMC:

    def __init__(self):
        self.calculadoraIMC_GUI()

    def calculadoraIMC_GUI(self):

        self.janela=Tk()
        self.janela.title('CALCULADORA IMC')
        self.janela.geometry('300x230')
        self.janela.resizable(False,False)

        self.label_peso=Label(text='PESO (Kg):',fg='black',font=('consolas',15,'bold'))
        self.label_peso.pack()

        self.entry_peso=Entry(width=10,fg='black',font=('consolas',15,'bold'))
        self.entry_peso.pack()
        self.entry_peso.focus()
        self.entry_peso.bind('<Return>',self.focusEntry_altura, lambda event: self.focusEntry_altura(event))


        self.label_altura=Label(text='ALTURA (M):',fg='black',font=('consolas',15,'bold'))
        self.label_altura.pack()

        self.entry_altura=Entry(width=10,fg='black',font=('consolas',15,'bold'))
        self.entry_altura.pack()

        self.entry_altura.bind('<Return>',self.calcula_imc, lambda event:self.calcula_imc(event))


        self.botao_calcular=Button(text='CALCULAR IMC',fg='black',font=('consolas',15,'bold'),command=self.calcula_imc)
        self.botao_calcular.pack()
        self.botao_calcular.bind('<Return>',self.calcula_imc, lambda event:self.calcula_imc(event))

        self.label_resultado=Label(text='')
        self.label_resultado.pack()

        self.label_inf_imc=Label(text='')
        self.label_inf_imc.pack()

        self.janela.mainloop()

    def focusEntry_altura(self,event):
        self.entry_altura.focus()
    
    def calcula_imc(self,event):
        try:
            self.peso=float(self.entry_peso.get())
            self.altura=float(self.entry_altura.get())
            self.imc=(self.peso)/(self.altura)**2
            self.label_resultado.config(text='IMC: {:.2f}'.format(self.imc),fg='green',font=('consolas',15,'bold'))
            if self.imc < 18.5:
                self.label_inf_imc.config(text='ABAIXO DO PESO',fg='red',font=('consolas',15,'bold'))
            elif 18.5 <= self.imc <= 24.9:
                self.label_inf_imc.config(text='PESO ADEQUADO',fg='green',font=('consolas',15,'bold'))
            elif 25.0 < self.imc < 29.9:
                self.label_inf_imc.config(text='SOBREPESO',fg='#FFA500',font=('consolas',15,'bold'))
            elif 30 < self.imc < 34.9:
                self.label_inf_imc.config(text='OBESIDADE',fg='red',font=('consolas',15,'bold'))

            self.entry_peso.delete(0,'end')
            self.entry_altura.delete(0,'end')
            self.entry_peso.focus()
        except:
            messagebox.showerror(title='CALCULADORA IMC',message='EXISTEM VALORES INVÁLIDOS, VERIFICAR!')
            self.entry_peso.delete(0,'end')
            self.entry_altura.delete(0,'end')
            self.entry_peso.focus()

chama_calculadora=calculadoraIMC()