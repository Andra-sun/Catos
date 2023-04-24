import tkinter as tk


    
#master
def sair_master(master):
    master.destroy()

def toggle_fullscreen(master):
    state = master.attributes("-fullscreen")
    master.attributes("-fullscreen", not state)
    
    
#informaçoes
def sair_informacoes(infos, master):
    infos.destroy()
    master.destroy()

def minimizar_informacoes(infos):
    state = infos.attributes("-fullscreen")
    infos.attributes("-fullscreen", not state)

def voltar_informacoes(infos, master):
    infos.destroy()
    master.deiconify()
    
    
#primeiro gato
def sair_primeiro(primeiro_gato, master):
    primeiro_gato.destroy()
    master.destroy()
    
def minimizar_primeiro(primeiro_gato):
    state = primeiro_gato.attributes('-fullscreen')
    primeiro_gato.attributes('-fullscreen', not state)
    
def voltar_primeiro(primeiro_gato, master):
    primeiro_gato.destroy()
    master.deiconify()
    

#segundo gato
def sair_segundo(segundo, master):
    segundo.destroy()
    master.destroy()
    
def minimizar_segundo(segundo):
    state = segundo.attributes('-fullscreen')
    segundo.attributes('-fullscreen', not state)
    
def voltar_segundo(segundo, primeiro_gato):
    segundo.destroy()
    primeiro_gato.deiconify()
    

#terceiro gato
def sair_terceiro(terceiro, master):
    terceiro.destroy()
    master.destroy()
    
def minimizar_terceiro(terceiro):
    state = terceiro.attributes('-fullscreen')
    terceiro.attributes('-fullscreen', not state)
    
def voltar_terceiro(terceiro, segundo):
    terceiro.destroy()
    segundo.deiconify() 
    
#quarto gato
def sair_quarto(quarto, master):
    quarto.destroy()
    master.destroy()
    
def minimizar_quarto(quarto):
    state = quarto.attributes('-fullscreen')
    quarto.attributes('-fullscreen', not state)
    
def voltar_quarto(quarto, terceiro):
    quarto.destroy()
    terceiro.deiconify() 