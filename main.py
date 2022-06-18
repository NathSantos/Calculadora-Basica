from tkinter import *
from tkinter import ttk

# Definição de cores utilizadas
color1 = "#30522b"  # verde pastel (mostrador)
color2 = "#63805e"  # verde calro (teclas)
color3 = "#acbdaa"  # verde cinza claro
color4 = "#ffffff"  # branco


# -------------------------------
# Criando a janela da Calculadora
# -------------------------------
root = Tk()                 # cria uma instância da classe Tk.
root.title("Calculadora")         
root.geometry("370x467") 


# -------------------------------------------------------
# Criando os frames mostrador (cálculos) e corpo (teclas)
# -------------------------------------------------------
screen_frame = Frame(root, width=370, height=100, bg=color3)   # tamanho e cor do mostrador
screen_frame.grid(row=0, column=0)                             # localização do mostrador

body_frame = Frame(root, width=370, height=400)   # tamanho e cor do corpo
body_frame.grid(row=1, column=0)                             # localização do corpo


# ------------------
# Criando os botões 
# ------------------

# bg -> cor de fundo
# fg -> cor da letra
# font -> especificações da fonte usada

button_C = Button(body_frame, text="C", width=14, height=3, bg=color2, font=('Comfortaa 10 bold'))
button_C.place(x=0, y=0) 
button_porc = Button(body_frame, text="%", width=6, height=3, bg=color2, font=('Comfortaa 10'))
button_porc.place(x=184, y=0) 
button_div = Button(body_frame, text="/", width=6, height=3, bg=color1, fg=color4, font=('Comfortaa 10'))
button_div.place(x=276, y=0) 

button_7 = Button(body_frame, text="7", width=6, height=3, bg=color2, font=('Comfortaa 10'))
button_7.place(x=0, y=73)
button_8 = Button(body_frame, text="8", width=6, height=3, bg=color2, font=('Comfortaa 10'))
button_8.place(x=92, y=73) 
button_9 = Button(body_frame, text="9", width=6, height=3, bg=color2, font=('Comfortaa 10'))
button_9.place(x=184, y=73) 
button_mult = Button(body_frame, text="x", width=6, height=3, bg=color1, fg=color4, font=('Comfortaa 10'))
button_mult.place(x=276, y=73) 

button_4 = Button(body_frame, text="4", width=6, height=3, bg=color2, font=('Comfortaa 10'))
button_4.place(x=0, y=146)
button_5 = Button(body_frame, text="5", width=6, height=3, bg=color2, font=('Comfortaa 10'))
button_5.place(x=92, y=146) 
button_6 = Button(body_frame, text="6", width=6, height=3, bg=color2, font=('Comfortaa 10'))
button_6.place(x=184, y=146) 
button_sub = Button(body_frame, text="-", width=6, height=3, bg=color1, fg=color4, font=('Comfortaa 10'))
button_sub.place(x=276, y=146)

button_1 = Button(body_frame, text="1", width=6, height=3, bg=color2, font=('Comfortaa 10'))
button_1.place(x=0, y=219)
button_2 = Button(body_frame, text="2", width=6, height=3, bg=color2, font=('Comfortaa 10'))
button_2.place(x=92, y=219) 
button_3 = Button(body_frame, text="3", width=6, height=3, bg=color2, font=('Comfortaa 10'))
button_3.place(x=184, y=219) 
button_add = Button(body_frame, text="+", width=6, height=3, bg=color1, fg=color4, font=('Comfortaa 10'))
button_add.place(x=276, y=219) 

button_0 = Button(body_frame, text="0", width=14, height=3, bg=color2, font=('Comfortaa 10'))
button_0.place(x=0, y=292) 
button_dot = Button(body_frame, text=".", width=6, height=3, bg=color2, font=('Comfortaa 10'))
button_dot.place(x=184, y=292) 
button_equal = Button(body_frame, text="=", width=6, height=3, bg=color1, fg=color4, font=('Comfortaa 10'))
button_equal.place(x=276, y=292) 

root.mainloop()