import tkinter
from tkinter import *
import insertar as inse


def btn_registro():
	inse.insert(El_Nombre.get(),El_Apellido.get(),El_Codigo.get())

def btn_rostro():
	print("orale")


mi_ventana = Tk()
mi_ventana.geometry("640x480")
#mi_ventana.iconbitmap("udg.ico")
mi_ventana.title("Ventana registro")

miFrame=Frame(mi_ventana,width=500,height=400)
miFrame.pack()


Label(miFrame, text="Registro de alumnos", fg ="blue", font=("Comic Sans MS",18)).place(x=130,y=0)

female = PhotoImage(file="f.ico")
Label(miFrame,image=female).place(x=0,y=0)

male = PhotoImage(file="m.ico")
Label(miFrame,image=male).place(x=400,y=0)

Label(miFrame,text="Guarda tu rostro").place(x=210,y=50)
rostro = PhotoImage(file="rostro.ico")
Button(miFrame,image=rostro, command=btn_rostro).place(x=210,y=70)

Label(miFrame,text="Nombre").place(x=200,y=200)
El_Nombre = Entry(miFrame)
El_Nombre.place(x=200,y=220)


Label(miFrame,text="Apellidos").place(x=200,y=240)
El_Apellido = Entry(miFrame)
El_Apellido.place(x=200,y=260)

Label(miFrame,text="Codigo").place(x=200,y=280)
El_Codigo = Entry(miFrame)
El_Codigo.place(x=200,y=300)


Button(miFrame,text="Registrarme", command=btn_registro).place(x=220,y=350)


mi_ventana.mainloop()
