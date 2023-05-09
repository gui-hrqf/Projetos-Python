from tkinter import *

class calculaLucro:
    
    def __init__(self):
        self.calculaLucro_GUI()
        
    def calculaLucro_GUI(self):
        self.janela=Tk()
        self.janela.title('LUCRO PRODUTO')
        self.janela.geometry('460x530')
        self.janela.resizable(False,False)

        self.lb_preco_compra=Label(text='PREÇO DE COMPRA:',font=('Bahnschrift',12,'bold'))
        self.lb_preco_compra.pack()

        self.entry_preco_compra=Entry(font=('Bahnschrift',12,'bold'))
        self.entry_preco_compra.pack()
        self.entry_preco_compra.focus()
        self.entry_preco_compra.bind('<Return>',self.focusEntryMargem, lambda event: self.focusEntryMargem(event))

        self.lb_margem=Label(text='MARGEM:',font=('Bahnschrift',12,'bold'))
        self.lb_margem.pack()

        self.entry_margem=Entry(font=('Bahnschrift',12,'bold'))
        self.entry_margem.pack()
        self.entry_margem.bind('<Return>',self.focusEntryComissaoFornecedor, lambda event: self.focusEntryComissaoFornecedor(event))

        self.lb_comissao_fornecedor=Label(text='CUSTO COMISSÕES [%]:',font=('Bahnschrift',12,'bold'))
        self.lb_comissao_fornecedor.pack()

        self.entry_comissao_fornecedor=Entry(font=('Bahnschrift',12,'bold'))
        self.entry_comissao_fornecedor.pack()
        self.entry_comissao_fornecedor.bind('<Return>',self.calculaValor, lambda event:self.calculaValor(event))

        self.lb_frame_custo=LabelFrame(self.janela,text='CONSIDERAR RESULTADO',font=('Bahnschrift',12,'bold'))
        self.lb_frame_custo.pack()

        self.radio_opcao=IntVar()
        self.radio_opcao.set(1)

        self.r1=Radiobutton(self.lb_frame_custo,text='COM COMISSÃO',font=('Bahnschrift',9),value=1,variable=self.radio_opcao)
        self.r1.pack()

        self.r2=Radiobutton(self.lb_frame_custo,text='SEM COMISSÃO',font=('Bahnschrift',9),value=2,variable=self.radio_opcao)
        self.r2.pack()

        self.frame_resultados=LabelFrame(self.janela,text='RESULTADOS',font=('Bahnschrift',12,'bold'))
        self.frame_resultados.pack(fill=BOTH)

        self.btn_calcula=Button(text='CALCULAR', command=self.calculaValor,font=('Bahnschrift',12,'bold'))
        self.btn_calcula.pack()
        self.btn_calcula.bind('<Return>',self.calculaValor, lambda event: self.calculaValor(event))

        self.btn_limpa_resultado=Button(text='LIMPAR', command=self.limpaValores,font=('Bahnschrift',12,'bold'))
        self.btn_limpa_resultado.pack()

        self.lb_versao=Label(text='VERSÃO: 1.03 - DESENVOLVIDO POR: GUILHERME FERREIRA',font=('consolas',8,'italic'))
        self.lb_versao.pack(anchor='s',side='right')

        self.janela.mainloop()

    def focusEntryMargem(self,event):
        self.entry_margem.focus()

    def focusEntryComissaoFornecedor(self,event):
        self.entry_comissao_fornecedor.focus()

    def calculaValor(self,event):

        self.preco_compra=float(self.entry_preco_compra.get())
        self.margem=float(self.entry_margem.get())
        self.comissao_fornecedor_percentual=float(self.entry_comissao_fornecedor.get())
        self.comissao_fornecedor=(self.comissao_fornecedor_percentual/100)
        self.preco_compra_comissao=self.preco_compra+(self.comissao_fornecedor*self.preco_compra)
        self.preco_margem=self.preco_compra_comissao+((self.margem/100)*self.preco_compra_comissao)
        self.valor_sob_margem=self.preco_compra_comissao*(self.margem/100)
        self.preco_venda=self.preco_compra_comissao+self.valor_sob_margem
        self.valor_comisssao=self.comissao_fornecedor*self.preco_compra
        self.lucro_venda=self.preco_venda-self.preco_compra

        self.seleciona_radio=self.radio_opcao.get()

        if self.seleciona_radio==1:

            self.lb_valor_compra=Label(self.frame_resultados,text='')
            self.lb_valor_compra.pack()

            self.lb_valor_margem=Label(self.frame_resultados,text='')
            self.lb_valor_margem.pack()

            self.lb_porcentagem_comissao=Label(self.frame_resultados,text='')
            self.lb_porcentagem_comissao.pack()

            self.lb_valor_comissao=Label(self.frame_resultados,text='')
            self.lb_valor_comissao.pack()

            self.lb_valor_compra_comissao=Label(self.frame_resultados,text='')
            self.lb_valor_compra_comissao.pack()

            self.lb_valor_sob_margem=Label(self.frame_resultados,text='')
            self.lb_valor_sob_margem.pack()

            self.lb_valor_venda=Label(self.frame_resultados,text='')
            self.lb_valor_venda.pack()

            self.lb_valor_lucro=Label(self.frame_resultados,text='')
            self.lb_valor_lucro.pack()

            self.lb_valor_compra.config(text=('PREÇO DE COMPRA: R$ {:.2f}'.format(self.preco_compra)),font=('Bahnschrift',12))
            self.lb_valor_margem.config(text=('MARGEM: {:.2f} %'.format(self.margem)),font=('Bahnschrift',12,'bold'),fg='blue')
            self.lb_porcentagem_comissao.config(text=('PERCENTUAL COMISSÃO FORNECEDOR: {:.1f} %'.format(self.comissao_fornecedor_percentual)),font=('Bahnschrift',12,'bold'),fg='red')
            self.lb_valor_comissao.config(text=('CUSTO COMISSÃO DO FORNECEDOR: R$ {:.2f}'.format(self.valor_comisssao)),font=('Bahnschrift',12))
            self.lb_valor_compra_comissao.config(text=('CUSTO PRODUTO + COMISSÃO FORNECEDOR: R$ {:.2f}'.format(self.preco_compra_comissao)),font=('Bahnschrift',12,'bold'),fg='orange')
            self.lb_valor_sob_margem.config(text=('LUCRO SOB A MARGEM ' +'{:.2f} %'.format(self.margem) + ': R$ {:.2f}'.format(self.valor_sob_margem)),font=('Bahnschrift',12))
            self.lb_valor_venda.config(text=('PREÇO DE VENDA PROPOSTO PELA MARGEM: R$ {:.2f}'.format(self.preco_venda)),font=('Bahnschrift',12))
            self.lb_valor_lucro.config(text=('LUCRO: R$ {:.2f}'.format(self.lucro_venda)),font=('Bahnschrift',12,'bold'),fg='green')

            self.entry_preco_compra.delete(0,'end')
            self.entry_margem.delete(0,'end')
            self.entry_comissao_fornecedor.delete(0,'end')
            self.entry_preco_compra.focus()
        
        if self.seleciona_radio==2:

            self.lb_valor_compra=Label(self.frame_resultados,text='')
            self.lb_valor_compra.pack()

            self.lb_valor_margem=Label(self.frame_resultados,text='')
            self.lb_valor_margem.pack()

            self.lb_valor_compra_comissao=Label(self.frame_resultados,text='')
            self.lb_valor_compra_comissao.pack()

            self.lb_valor_sob_margem=Label(self.frame_resultados,text='')
            self.lb_valor_sob_margem.pack()

            self.lb_valor_venda=Label(self.frame_resultados,text='')
            self.lb_valor_venda.pack()

            self.lb_valor_lucro=Label(self.frame_resultados,text='')
            self.lb_valor_lucro.pack()

            self.lb_valor_compra.config(text=('PREÇO DE COMPRA: R$ {:.2f}'.format(self.preco_compra)),font=('Bahnschrift',12))
            self.lb_valor_margem.config(text=('MARGEM: {:.2f} %'.format(self.margem)),font=('Bahnschrift',12,'bold'),fg='blue')
            self.lb_valor_compra_comissao.config(text=('CUSTO TOTAL PRODUTO: R$ {:.2f}'.format(self.preco_compra)),font=('Bahnschrift',12,'bold'),fg='orange')
            self.lb_valor_sob_margem.config(text=('LUCRO SOB A MARGEM {:.2f} %: R$ {:.2f}'.format(self.margem,self.valor_sob_margem)),font=('Bahnschrift',12))
            self.lb_valor_venda.config(text=('PREÇO DE VENDA PROPOSTO PELA MARGEM: R$ {:.2f}'.format(self.preco_venda)),font=('Bahnschrift',12))
            self.lb_valor_lucro.config(text=('LUCRO: R$ {:.2f}'.format(self.lucro_venda)),font=('Bahnschrift',12,'bold'),fg='green')
            self.entry_preco_compra.delete(0,'end')
            self.entry_margem.delete(0,'end')
            self.entry_comissao_fornecedor.delete(0,'end')
            self.entry_preco_compra.focus()

    def limpaValores(self):

        if self.seleciona_radio==1:

            self.lb_valor_compra.destroy()
            self.lb_valor_margem.destroy()
            self.lb_porcentagem_comissao.destroy()
            self.lb_valor_comissao.destroy()
            self.lb_valor_compra_comissao.destroy()
            self.lb_valor_sob_margem.destroy()
            self.lb_valor_venda.destroy()
            self.lb_valor_lucro.destroy()
        
        if self.seleciona_radio==2:

            self.lb_valor_compra.destroy()
            self.lb_valor_margem.destroy()
            self.lb_valor_compra_comissao.destroy()
            self.lb_valor_sob_margem.destroy()
            self.lb_valor_venda.destroy()
            self.lb_valor_lucro.destroy()

inicia_programa=calculaLucro()