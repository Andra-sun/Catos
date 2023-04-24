import tkinter as tk
import os
from funcoes import *
from widget import VidasWidget


class catsWindow:
    def __init__(self, master):
        self.master = master

        titulo = tk.Label(text='Adivinhe o gatinho', font = fontCat, bg='#f9b5f9')
        titulo.pack(pady=23)
        
        self.sair = tk.Button(master, text='X', command =lambda: sair_master(self.master), bg='#f21318')
        self.sair.place(x=self.master.winfo_screenwidth() - 10, y=10, anchor='ne')
        self.sair.configure(width=5, height=2)

        self.btn_fullscreen = tk.Button(master, text="❐", command=lambda: toggle_fullscreen(self.master))
        self.btn_fullscreen.configure(width=5, height=2)
        self.btn_fullscreen.place(x=self.master.winfo_screenwidth() - 80, y=10, anchor='ne')
        
        self.botao1 = tk.Button(master, text="Começar", command=self.abrir_primeiro_gato, font=fonte1, bg='#75d281')
        self.botao1.configure(width=34, height=2)
        self.botao1.pack(pady=90)
        
        self.botao11 = tk.Button(master, text="Informações", command=self.abrir_informacoes, font=fonte1, bg='#75d281')
        self.botao11.configure(width=34, height=2)
        self.botao11.pack(pady=7)
        
        legenda = tk.Label(text='feito por: Camile :D', font=fonte1, bg='#f9b5f9')
        legenda.pack(anchor='se', side='bottom')
        
    def abrir_informacoes(self):
        self.infos = tk.Toplevel(self.master)
        self.infos.config(bg='#f9b5f9')
        
        self.sair1 = tk.Button(self.infos, text='X', command =lambda: sair_informacoes(self.infos, self.master), bg='#f21318')
        self.sair1.place(x=self.infos.winfo_screenwidth() - 10, y=10, anchor='ne')
        self.sair1.configure(width=5, height=2)

        self.btn1_fullscreen = tk.Button(self.infos, text="❐", command=lambda: minimizar_informacoes(self.infos))
        self.btn1_fullscreen.configure(width=5, height=2)
        self.btn1_fullscreen.place(x=self.infos.winfo_screenwidth() - 80, y=10, anchor='ne')
        
        self.voltarBT = tk.Button(self.infos, text='Voltar', bg='#75d281', command=lambda: voltar_informacoes(self.infos, self.master))
        self.voltarBT.place( x=self.infos.winfo_screenwidth() - 1350, y=10, anchor='nw')
        self.voltarBT.configure(width=7, height=2)
        
        textu = tk.Label(self.infos, text='neste quiz voce irá adivinhar o nome do gatinho que estará na foto\napenas clique na opçao que voce acha que é a correta', font=fonte1, bg='#f9b5f9')
        textu.pack(pady=150)  
        
        caminho_imagem = os.path.join(os.getcwd(),'gatos/pomada.gif')  
        imagem = tk.PhotoImage(file=caminho_imagem)
        label_imagem = tk.Label(self.infos, image=imagem)
        label_imagem.image = imagem
        label_imagem.pack()
        
        self.infos.state('zoomed')
        self.infos.minsize(1350, 700)
        self.infos.attributes('-fullscreen', True)
        
    def abrir_primeiro_gato(self):
        self.primeiro_gato = tk.Toplevel(self.master)
        self.primeiro_gato.config(bg='#f9b5f9')
        
        self.sair2 = tk.Button(self.primeiro_gato, text='X', command =lambda: sair_primeiro(self.primeiro_gato, self.master), bg='#f21318')
        self.sair2.place(x=self.primeiro_gato.winfo_screenwidth() - 10, y=10, anchor='ne')
        self.sair2.configure(width=5, height=2)

        self.btn2_fullscreen = tk.Button(self.primeiro_gato, text="❐", command=lambda: minimizar_primeiro(self.primeiro_gato))
        self.btn2_fullscreen.configure(width=5, height=2)
        self.btn2_fullscreen.place(x=self.primeiro_gato.winfo_screenwidth() - 80, y=10, anchor='ne')
        
        self.voltarBT1 = tk.Button(self.primeiro_gato, text='Voltar', bg='#75d281', command=lambda: voltar_primeiro(self.primeiro_gato, self.master))
        self.voltarBT1.place( x=self.primeiro_gato.winfo_screenwidth() - 1350, y=10, anchor='nw')
        self.voltarBT1.configure(width=7, height=2)
        
        caminho_imagem = os.path.join(os.getcwd(),'gatos/pomada.gif')  
        imagem = tk.PhotoImage(file=caminho_imagem)
        label_imagem = tk.Label(self.primeiro_gato, image=imagem)
        label_imagem.image = imagem
        label_imagem.pack(pady=38)
        
        btn_width = 140
        btn_height = 60
        x_pos = self.primeiro_gato.winfo_screenwidth() // 2.39 - btn_width

        self.certo1 = tk.Button(self.primeiro_gato, text='Pomada', command=self.abrir_segundo_gato, width=10, font=fonte1)
        self.certo1.place(x=x_pos, y=imagem.height()+80, width=btn_width, height=btn_height)

        self.certo2 = tk.Button(self.primeiro_gato, text='Dorflex', width=10, font=fonte1, command=lambda: widget.lose_life())
        self.certo2.place(x=x_pos+btn_width+40, y=imagem.height()+80, width=btn_width, height=btn_height)

        self.certo3 = tk.Button(self.primeiro_gato, text='Luna', width=10, font=fonte1, command=lambda: widget.lose_life())
        self.certo3.place(x=x_pos+2*(btn_width+40), y=imagem.height()+80, width=btn_width, height=btn_height)
        
        self.primeiro_gato.state('zoomed')
        self.primeiro_gato.minsize(1350, 700)
        self.primeiro_gato.attributes('-fullscreen', True)
        
        widget = VidasWidget(self.primeiro_gato)
        widget.pack(side='bottom', pady='30')
        
        perder_vida_buon = tk.Button(self.primeiro_gato, text="Perder Vida", command=lambda: widget.lose_life())
        perder_vida_buon.pack(side='bottom', pady='30')
        
            
    def abrir_segundo_gato(self):
        self.segundo = tk.Toplevel(self.primeiro_gato)
        self.segundo.config(bg='#f9b5f9')
        
        self.sair3 = tk.Button(self.segundo, text='X', command =lambda: sair_segundo(self.segundo, self.master), bg='#f21318')
        self.sair3.place(x=self.segundo.winfo_screenwidth() - 10, y=10, anchor='ne')
        self.sair3.configure(width=5, height=2)

        self.btn3_fullscreen = tk.Button(self.segundo, text="❐", command=lambda: minimizar_segundo(self.segundo))
        self.btn3_fullscreen.configure(width=5, height=2)
        self.btn3_fullscreen.place(x=self.segundo.winfo_screenwidth() - 80, y=10, anchor='ne')
        
        self.voltarBT1 = tk.Button(self.segundo, text='Voltar', bg='#75d281', command=lambda: voltar_segundo(self.segundo, self.primeiro_gato))
        self.voltarBT1.place( x=self.segundo.winfo_screenwidth() - 1350, y=10, anchor='nw')
        self.voltarBT1.configure(width=7, height=2)
        
        self.certo2 = tk.Button(self.segundo, text='botao certo', command=self.abrir_terceiro_gato)
        self.certo2.pack()
        
        caminho_imagem = os.path.join(os.getcwd(),'gatos/pomada.gif')  
        imagem = tk.PhotoImage(file=caminho_imagem)
        label_imagem = tk.Label(self.segundo, image=imagem)
        label_imagem.image = imagem
        label_imagem.pack()
        
        self.segundo.state('zoomed')
        self.segundo.minsize(1350, 700)
        self.segundo.attributes('-fullscreen', True)
        
        widget = VidasWidget(self.segundo)
        widget.pack()
        
        perder_vida_button = tk.Button(self.segundo, text="Perder Vida", command=lambda: widget.lose_life())
        perder_vida_button.pack()
          
    def abrir_terceiro_gato(self):
        
        self.terceiro = tk.Toplevel(self.segundo)
        self.terceiro.config(bg='#f9b5f9')
        
        self.sair4 = tk.Button(self.terceiro, text='X', command =lambda: sair_terceiro(self.terceiro, self.master), bg='#f21318')
        self.sair4.place(x=self.terceiro.winfo_screenwidth() - 10, y=10, anchor='ne')
        self.sair4.configure(width=5, height=2)

        self.btn4_fullscreen = tk.Button(self.terceiro, text="❐", command=lambda: minimizar_terceiro(self.terceiro))
        self.btn4_fullscreen.configure(width=5, height=2)
        self.btn4_fullscreen.place(x=self.terceiro.winfo_screenwidth() - 80, y=10, anchor='ne')
        
        self.voltarBT2 = tk.Button(self.terceiro, text='Voltar', bg='#75d281', command=lambda: voltar_terceiro(self.terceiro, self.segundo))
        self.voltarBT2.place( x=self.terceiro.winfo_screenwidth() - 1350, y=10, anchor='nw')
        self.voltarBT2.configure(width=7, height=2)
        
        self.certo3 = tk.Button(self.terceiro, text='botao', command=self.abrir_quarto_gato)
        self.certo3.pack()
        
        caminho_imagem = os.path.join(os.getcwd(),'gatos/pomada.gif')  
        imagem = tk.PhotoImage(file=caminho_imagem)
        label_imagem = tk.Label(self.terceiro, image=imagem)
        label_imagem.image = imagem
        label_imagem.pack()
        
        self.terceiro.state('zoomed')
        self.terceiro.minsize(1350, 700)
        self.terceiro.attributes('-fullscreen', True)
        
        widget = VidasWidget(self.terceiro)
        widget.pack()
        
        perder_vida_butt = tk.Button(self.terceiro, text="Perder", command=lambda: widget.lose_life())
        perder_vida_butt.pack()
        
    def abrir_quarto_gato(self):
        self.quarto = tk.Toplevel(self.terceiro)
        self.quarto.config(bg='#f9b5f9')
        
        self.sair5 = tk.Button(self.quarto, text='X', command =lambda: sair_quarto(self.quarto, self.master), bg='#f21318')
        self.sair5.place(x=self.quarto.winfo_screenwidth() - 10, y=10, anchor='ne')
        self.sair5.configure(width=5, height=2)

        self.btn5_fullscreen = tk.Button(self.quarto, text="❐", command=lambda: minimizar_quarto(self.quarto))
        self.btn5_fullscreen.configure(width=5, height=2)
        self.btn5_fullscreen.place(x=self.terceiro.winfo_screenwidth() - 80, y=10, anchor='ne')
        
        self.voltarBT3 = tk.Button(self.quarto, text='Voltar', bg='#75d281', command=lambda: voltar_quarto(self.quarto, self.terceiro))
        self.voltarBT3.place( x=self.quarto.winfo_screenwidth() - 1350, y=10, anchor='nw')
        self.voltarBT3.configure(width=7, height=2)
        
        self.certo4 = tk.Button(self.quarto, text='bot')
        self.certo4.pack()
        
        caminho_imagem = os.path.join(os.getcwd(),'gatos/pomada.gif')  
        imagem = tk.PhotoImage(file=caminho_imagem)
        label_imagem = tk.Label(self.quarto, image=imagem)
        label_imagem.image = imagem
        label_imagem.pack()
        
        self.quarto.state('zoomed')
        self.quarto.minsize(1350, 700)
        self.quarto.attributes('-fullscreen', True)
    
       
pastaRoot=os.path.dirname(__file__)    
root = tk.Tk()
root.config(bg='#f9b5f9')
root.attributes("-fullscreen", True)
root.state('zoomed')
root.minsize(1350, 700)
fonte1 = ('system', '20')
fontCat = ('cat', '68')
janela_principal = catsWindow(root)
root.mainloop()