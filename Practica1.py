import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext
ventana=tk.Tk()
ventana.title("Sistema Escolar")
ventana.geometry("520x320")
#Pestañas
tabControl = ttk.Notebook(ventana)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Datos Personales')
tabControl.pack(expand=2, fill="both")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Datos extras')

#Menu ventana
def funcion_caja_mensaje():
    mBox.showinfo('Mensaje','Christian Ingenieria en Sistemas 4to Semestre\n         Lizarx Co')
def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()
def funcion_imprimir():
    if(Direccion.get() is "" or ApellidoP.get() is "" or ApellidoM.get() is "" or nombre.get() is "" or str(Objetivo.get(0.0,tk.END)) == "" or opcion.get() == ""):
        mBox.showerror('Error','Hay datos que aún no se han ingresado')
    elif(opcion_1.get() is 0 and opcion_2.get() is 0 and opcion_3.get() is 0 and opcion_4.get() is 0 and opcion_5.get() is 0):
        ventana4=tk.Tk()
        ventana4.title("Info")
        ventana4.geometry("520x340")
        ttk.Label(ventana4, text="Nombre: ").grid(column=0, row=0)
        ttk.Label(ventana4, text=nombre.get()+' '+ApellidoP.get()+' '+ApellidoM.get()).grid(column=1, row=0)
        ttk.Label(ventana4, text="Dirección: ").grid(column=0, row=1)
        ttk.Label(ventana4, text=Direccion.get()+" Col."+Colonia.get()).grid(column=1, row=1)
        ttk.Label(ventana4, text="Ciudad: ").grid(column=0, row=2)
        ttk.Label(ventana4, text=Ciudad.get()).grid(column=1, row=2)
        ttk.Label(ventana4, text="Municipio: ").grid(column=0, row=3)
        ttk.Label(ventana4, text=Municipio.get()).grid(column=1, row=3)
        ttk.Label(ventana4, text="No tiene pasatiempos").grid(column=0, row=4)
        ttk.Label(ventana4, text="Estado: ").grid(column=0, row=5)
        ttk.Label(ventana4, text=opcion.get()).grid(column=1, row=5)
        ttk.Label(ventana4, text="Objetivo en la vida: ").grid(column=0, row=6)
        ttk.Label(ventana4, text=Objetivo.get(0.0,tk.END)).place(x=194, y=122)
    else:
        ventana4=tk.Tk()
        ventana4.title("Info")
        ventana4.geometry("520x340")
        ttk.Label(ventana4, text="Nombre: ").grid(column=0, row=0)
        ttk.Label(ventana4, text=nombre.get()+' '+ApellidoP.get()+' '+ApellidoM.get()).grid(column=1, row=0)
        ttk.Label(ventana4, text="Dirección: ").grid(column=0, row=1)
        ttk.Label(ventana4, text=Direccion.get()+" Col."+Colonia.get()).grid(column=1, row=1)
        ttk.Label(ventana4, text="Ciudad: ").grid(column=0, row=2)
        ttk.Label(ventana4, text=Ciudad.get()).grid(column=1, row=2)
        ttk.Label(ventana4, text="Municipio: ").grid(column=0, row=3)
        ttk.Label(ventana4, text=Municipio.get()).grid(column=1, row=3)
        ttk.Label(ventana4, text="Pasatiempos: ").grid(column=0, row=4)
        if(opcion_1.get() == 1): 
            ttk.Label(ventana4, text="Leer ").grid(column=1,row=4)
        if(opcion_2.get() == 1): 
            ttk.Label(ventana4, text="Futbol ").grid(column=2,row=4)
        if(opcion_3.get() == 1): 
            ttk.Label(ventana4, text="Correr ").grid(column=3,row=4)
        if(opcion_4.get() == 1): 
            ttk.Label(ventana4, text="Pintar ").grid(column=4,row=4)
        if(opcion_5.get() == 1): 
            ttk.Label(ventana4, text="Salir").grid(column=5,row=4)
        ttk.Label(ventana4, text="Estado: ").grid(column=0, row=5)
        ttk.Label(ventana4, text=opcion.get()).grid(column=1, row=5)
        ttk.Label(ventana4, text="Objetivo en la vida: ").grid(column=0, row=6)
        ttk.Label(ventana4, text=Objetivo.get(0.0,tk.END)).place(x=194, y=122)
barra_menu=Menu(ventana)
ventana.config(menu=barra_menu)
opciones_menu=Menu(barra_menu)
opciones_menu.add_command(label="Imprimir",command=funcion_imprimir)
opciones_menu.add_separator()
opciones_menu.add_command(label="Salir",command=funcion_salir)
barra_menu.add_cascade(label="Archivo",menu=opciones_menu)
menu_ayuda=Menu(barra_menu)
menu_ayuda.add_command(label="Acerca de",command=funcion_caja_mensaje)
barra_menu.add_cascade(label="Ayuda",menu=menu_ayuda)

#Pestaña 1
#Text Boxes
def clickMe():
    if(Direccion.get() is "" or ApellidoP.get() is "" or ApellidoM.get() is "" or nombre.get() is ""):
        accion.configure(text="Casillas vacías")
    else:
        accion.configure(text="Registro exitoso")
        ventana2=tk.Tk()
        ventana2.title("Info")
        ventana2.geometry("420x140")
        ttk.Label(ventana2, text="Nombre: ").grid(column=0, row=0)
        ttk.Label(ventana2, text=nombre.get()+' '+ApellidoP.get()+' '+ApellidoM.get()).grid(column=1, row=0)
        ttk.Label(ventana2, text="Dirección: ").grid(column=0, row=1)
        ttk.Label(ventana2, text=Direccion.get()+" Col."+Colonia.get()).grid(column=1, row=1)
        ttk.Label(ventana2, text="Ciudad: ").grid(column=0, row=2)
        ttk.Label(ventana2, text=Ciudad.get()).grid(column=1, row=2)
        ttk.Label(ventana2, text="Municipio: ").grid(column=0, row=3)
        ttk.Label(ventana2, text=Municipio.get()).grid(column=1, row=3)
nombre=tk.StringVar()
t1=ttk.Label(tab1, text="Nombre: ").grid(column=0, row=0)
nombreCapturado = ttk.Entry(tab1, width=12, textvariable=nombre).grid(column=1, row=0)
ApellidoP=tk.StringVar()
t2=ttk.Label(tab1, text="Apellido Paterno: ").grid(column=0, row=1)
apellidopCapturado = ttk.Entry(tab1, width=12, textvariable=ApellidoP).grid(column=1,row=1)
ApellidoM=tk.StringVar()
t3=ttk.Label(tab1, text="Apellido Materno: ").grid(column=0, row=2)
apellidomCapturado = ttk.Entry(tab1, width=12, textvariable=ApellidoM).grid(column=1,row=2)
Direccion=tk.StringVar()
t4=ttk.Label(tab1, text="Direccion: ").grid(column=0, row=3)
direccionCapturada = ttk.Entry(tab1, width=12, textvariable=Direccion).grid(column=1,row=3)

#Comboboxes
Colonia=tk.StringVar()
ttk.Label(tab1, text="Selecciona tu colonia:").grid(column=0,row=4)
coloniaSeleccionada=ttk.Combobox(tab1,width=18,textvariable=Colonia)
coloniaSeleccionada['values']=("Villa Universidad", "Residencial del Sur", "Chapultepec Norte", "Camelinas")
coloniaSeleccionada.grid(column=1, row=4)
coloniaSeleccionada.current(0)

ttk.Label(tab1, text="Selecciona tu ciudad:").grid(column=0,row=5)
Ciudad=tk.StringVar()
ciudadSeleccionada=ttk.Combobox(tab1,width=18,textvariable=Ciudad)
ciudadSeleccionada['values']=("Morelia","Queretaro","Cd.Mex","Monterrey")
ciudadSeleccionada.grid(column=1, row=5)
ciudadSeleccionada.current(0)

ttk.Label(tab1, text="Selecciona tu municipio:").grid(column=0,row=6)
Municipio=tk.StringVar()
municipioSeleccionado=ttk.Combobox(tab1,width=18,textvariable=Municipio)
municipioSeleccionado['values']=("Morelia","Pátzcuaro","Lázaro Cárdenaz","Quiroga")
municipioSeleccionado.grid(column=1, row=6)
municipioSeleccionado.current(0)

#Botón
accion=ttk.Button(tab1, text="Registro",command=clickMe)
accion.place(x=350,y=170)

#Pestaña 2
#Check Button
def clickMe2():
    if(str(Objetivo.get(0.0,tk.END)) == "" or opcion.get() == ""):
        accion2.configure(text="Casillas vacías")
    else:
        accion2.configure(text="Registro exitoso")
        ventana3=tk.Tk()
        ventana3.title("Info")
        ventana3.geometry("420x140")
        if(opcion_1.get() is 0 and opcion_2.get() is 0 and opcion_3.get() is 0 and opcion_4.get() is 0 and opcion_5.get() is 0):
            ttk.Label(ventana3, text="No tiene pasatiempos").grid(column=0, row=0)
            ttk.Label(ventana3, text="Estado: ").grid(column=0, row=1)
            ttk.Label(ventana3, text=opcion.get()).grid(column=1, row=1)
            ttk.Label(ventana3, text="Objetivo en la vida: ").grid(column=0, row=2)
            ttk.Label(ventana3, text=Objetivo.get(0.0,tk.END)).place(x=142, y=38)
        else:
            ttk.Label(ventana3, text="Pasatiempos: ").grid(column=0, row=0)
            if(opcion_1.get() == 1): 
                ttk.Label(ventana3, text="Leer ").grid(column=1,row=0)
            if(opcion_2.get() == 1): 
                ttk.Label(ventana3, text="Futbol ").grid(column=2,row=0)
            if(opcion_3.get() == 1): 
                ttk.Label(ventana3, text="Correr ").grid(column=3,row=0)
            if(opcion_4.get() == 1): 
                ttk.Label(ventana3, text="Pintar ").grid(column=4,row=0)
            if(opcion_5.get() == 1): 
                ttk.Label(ventana3, text="Salir").grid(column=5,row=0)
            ttk.Label(ventana3, text="Estado: ").grid(column=0, row=1)
            ttk.Label(ventana3, text=opcion.get()).grid(column=1, row=1)
            ttk.Label(ventana3, text="Objetivo en la vida: ").grid(column=0, row=2)
            ttk.Label(ventana3, text=Objetivo.get(0.0,tk.END)).place(x=142, y=38) 
ttk.Label(tab2, text="Pasatiempos").grid(column=1, row=9)
opcion_1=tk.IntVar()
casilla_1=tk.Checkbutton(tab2, text="Leer", variable=opcion_1)
casilla_1.deselect()
casilla_1.grid(column=0, row=10, sticky=tk.W)
opcion_2=tk.IntVar()
casilla_2=tk.Checkbutton(tab2, text="Futbol", variable=opcion_2)
casilla_2.deselect()
casilla_2.grid(column=1, row=10, sticky=tk.W)
opcion_3=tk.IntVar()
casilla_3=tk.Checkbutton(tab2, text="Correr", variable=opcion_3)
casilla_3.deselect()
casilla_3.grid(column=2, row=10, sticky=tk.W)
opcion_4=tk.IntVar()
casilla_4=tk.Checkbutton(tab2, text="Pintar", variable=opcion_4)
casilla_4.deselect()
casilla_4.grid(column=0, row=11, sticky=tk.W)
opcion_5=tk.IntVar()
casilla_5=tk.Checkbutton(tab2, text="Salir", variable=opcion_5)
casilla_5.deselect()
casilla_5.grid(column=1, row=11, sticky=tk.W)

#Radio Button
ttk.Label(tab2, text="Estado").grid(column=1, row=12)
opcion=tk.StringVar()
radio1=tk.Radiobutton(tab2, text="Soltero", variable=opcion,value="Soltero")
radio1.grid(column=0, row=13, sticky=tk.W)
radio2=tk.Radiobutton(tab2, text="Casado", variable=opcion,value="Casado")
radio2.grid(column=1, row=13, sticky=tk.W)
radio3=tk.Radiobutton(tab2, text="Union Libre", variable=opcion,value="Union Libre")
radio3.grid(column=2, row=13, sticky=tk.W)
radio4=tk.Radiobutton(tab2, text="Separado", variable=opcion,value="Separado")
radio4.grid(column=0, row=14, sticky=tk.W)
radio5=tk.Radiobutton(tab2, text="Viudo", variable=opcion,value="Viudo")
radio5.grid(column=1, row=14, sticky=tk.W)

#Caja de texto
scrol_ancho = 30
scrol_alto = 3
ttk.Label(tab2,text="Objetivo en la vida").grid(column=0, row=15)
Objetivo = scrolledtext.ScrolledText(tab2, width=scrol_ancho, height=scrol_alto, wrap=tk.WORD)
Objetivo.grid(column=0,columnspan=2, row=16)
accion2=ttk.Button(tab2, text="Registro",command=clickMe2)
accion2.place(x=310,y=170)
ventana.mainloop()