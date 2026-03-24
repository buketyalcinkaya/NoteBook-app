from tkinter import *

screen = Tk()           #bana boş bir uygulama penceresi hazırla.
screen.geometry("500x500")
canvas = Canvas(screen, background="pink")     #tuval oluşturduk.
canvas.place(relx=0.0 , rely=0.0, relheight=1.0, relwidth=1.0)   #bu tuval, ana ekran ne kadar büyütülürse büyütülsün, ekranın tamamını kaplayacak şekilde esner.

#*** FRAME(ÇERÇEVE) ALANI ***
color = "#FFFFCC"
topframe = Frame(screen, bg=color)
topframe.place(relx=0.02 , rely=0.01, relheight=0.1, relwidth=0.96)

subframe_right = Frame(screen, bg=color) #sağ frame ayarları
subframe_right.place(relx=0.3 , rely=0.13, relheight=0.85, relwidth=0.68)

subframe_left = Frame(screen, bg=color) #sol frame ayarları
subframe_left.place(relx=0.02 , rely=0.13, relheight=0.85, relwidth=0.26)

#**** FRAME (ÇERÇEVE)ALANI BİTİŞ ****

option = StringVar(topframe)
option.set("/t")

option_menu = OptionMenu(topframe, option, "year","month", "week","day")
option_menu.place(relx=0.0, rely=0.0, relheight=0.5, relwidth=0.2)

#--------------------------

create_text = Text(topframe,bg="#fffaf0")
create_text.place(relx=0.25 , rely=0.05, relheight=0.90, relwidth=0.73)

#--------------------------
def save_a():
    x = create_text.get("1.0","end")
    with open("Save Text","a" ,encoding= "utf-8") as file:
        file.write(x)


def save_w():
    x = create_text.get("1.0", "end")
    with open("Save_Text.", "w", encoding="utf-8") as file:
        file.write(x)


var = IntVar()
r_button1 = Radiobutton(subframe_left,text="Temiz Kayıt",variable=var,value=1, bg=color, font="verdana 8 bold")
r_button1.place(relx=0.01 , rely=0.1, relheight=0.1, relwidth=0.8)

r_button2 = Radiobutton(subframe_left,text="Ekle            ",variable=var,value=2, bg=color, font="verdana 8 bold")
r_button2.place(relx=0.01 , rely=0.2, relheight=0.1, relwidth=0.8)
#--------------------------
def note_func():
    if var.get():
        save_w()
    elif var.get() ==2:
        save_a()

text_button = Button(topframe, text="oluştur", command=note_func)
text_button.place(relx=0.0, rely=0.5, relwidth=0.2, relheight=0.5)

#--------------------------
with open('Save_Text', "a" , encoding="utf-8") as file:
    pass
with open("Save_Text","r",encoding="utf-8") as file:
      n = file.read()

note = Text(subframe_right,bg="#fffaf0")
note.place(relx=0.03, rely=0.03, relheight=0.94, relwidth=0.94)
note.insert("1.0", n)


#----------------------------

screen.mainloop()

#-----------
