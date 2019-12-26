from tkinter import * 

def accion_de_mi_boton():
    print("Mi boton ha sido presionado!")


mi_ventana = Tk()
mi_ventana.geometry("640x480")
mi_ventana.iconbitmap("udg.ico")
mi_ventana.title("Ventana registro")

miFrame=Frame(mi_ventana,width=500,height=400)
miFrame.pack()



Label(miFrame, text="Hola mundo", fg ="blue", font=("Comic Sans MS",18))

udg = PhotoImage(file="udg.ico")
Label(miFrame,image=udg).place(x=100,y=0)

Button(miFrame,text="Mi botón!", command=accion_de_mi_boton).place(x=100,y=300)

Button(miFrame,text="Mi botón 2!", command=accion_de_mi_boton).place(x=300,y=300)

mi_ventana.mainloop()
