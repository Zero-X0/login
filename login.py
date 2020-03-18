from tkinter import *
ventana= Tk()
ventana.geometry("630x360")
miFrame=Frame(ventana, width="315",height="180")
miFrame.place(x=170,y=100)
Frame=Frame(ventana, width="315",height="180")
Frame.place(x=170,y=170)

L01= Label(text="Inicio de sesion") #Esto crea un label
L01.place(x=200, y=1)#Esto es la ubicacion del label
L01.config( fg="blue")#color de fondo y de las letras en el label
L01.config(fon=("arial black",20))

L02= Label(text="Usuario:") #Esto crea un label
L02.place(x=50, y=100)#Esto es la ubicacion del label
L02.config( fg="blue")#color de fondo y de las letras en el label
L02.config(fon=("arial black",16))

L03= Label(text="Password:") #Esto crea un label
L03.place(x=45, y=170)#Esto es la ubicacion del label
L03.config( fg="blue")#color de fondo y de las letras en el label
L03.config(fon=("arial black",16))

#def imprimir():
 #   l01=Label(text="Usuario:"+t01.get()+" Password:" +t02.get())
  #  l01.pack()
   # l01.place(x=1,y=1)
    #l01.config(bg="orange", fg="white")
    #l01.config(fon=("arial", 10))

#Campo de texto
#t01= Entry(miFrame)
#t01.pack()
#t01.config(fon=("arial black", 16))
#t01.config(bg="red",fg="blue")
#t02= Entry(Frame)
#t02.pack()
#t02.config(fon=("arial black", 16))
#t02.config(bg="red",fg="blue")


#b01=Button(text="Login", command=imprimir)
#b01.pack()
#b01.place(x=270,y=250)
#b02=Button(text="Registro")
#b02.pack()
#b02.place(x=320,y=250)

ventana.mainloop()