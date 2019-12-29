import requests
import tkinter
from tkinter import *

def btn_rostro():
    id = "849259281"
 
    token = "913814519:AAHDEuPkcGDDL5un2lAwzTIpvHPUDe4Q4xw"
     
    url = "https://api.telegram.org/bot" + token + "/sendMessage"
    params = {
    'chat_id': id,
     
    'text' : str(El_Nombre.get())
    }
     
    requests.post(url, params=params)


mi_ventana = Tk()
mi_ventana.geometry("640x480")
#mi_ventana.iconbitmap("udg.ico")
mi_ventana.title("Ventana registro")

miFrame=Frame(mi_ventana,width=500,height=400)
miFrame.pack()

Label(miFrame,text="Nombre").place(x=200,y=200)
El_Nombre = Entry(miFrame)
El_Nombre.place(x=200,y=220)


Button(miFrame,text="Registrarme", command=btn_rostro).place(x=220,y=350)

mi_ventana.mainloop()
