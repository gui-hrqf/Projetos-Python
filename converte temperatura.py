from tkinter import *

class ConverteTemperatura:

    def __init__(self):
        self.ConverteTemperatura_GUI()
    
    def converteKelvin(self):
        self.temp_c=float(self.entry.get())
        print(f'INFORMADO {self.temp_c}ºC')
        self.temp_k=self.temp_c+273.15
        print(f'{self.temp_c}ºC = {self.temp_k}K')
        self.atualiza_GUI()

    def atualiza_GUI(self):
        self.lb_result.config(text=self.temp_k)

    
    def ConverteTemperatura_GUI(self):
        self.janela=Tk()
        self.janela.title('CONVERSOR TEMPERATURA')
        self.janela.geometry('300x200')

        self.lb1=Label(text='INFORME A TEMPERATURA:')
        self.lb1.grid(column=0,row=0)

        self.entry=Entry()
        self.entry.grid(column=1,row=0)

        self.btn=Button(text='CONVERTER', command=self.converteKelvin)
        self.btn.grid(column=0,row=1)

        self.lb_result=Label(text='')
        self.lb_result.grid(column=1,row=1)


        self.janela.mainloop()




    
temperatura=ConverteTemperatura()
