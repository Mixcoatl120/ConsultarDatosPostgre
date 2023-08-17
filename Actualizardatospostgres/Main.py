#Funciones
import tkinter
import openpyxl
from Conexion import Actualizar_datos,Insertar_datos
from tkinter import *
from tkinter import Tk, ttk, Label, filedialog, messagebox, W, E

#Funciones
def cargar_archivo():
    try:
        filename = filedialog.askopenfilename() #lectura de direccion de archivo(Direccion del archivo)
        workbook = openpyxl.load_workbook(filename) # lectura de archivo
        sheet = workbook.active #lectura de la hoja activa 
        lista_valores = list(sheet.values) #crea una lista de los valores que hay en la hoja activa

        #LLenado de datos 
        for value_tuple in lista_valores[1:]:
            tabla.insert('',tkinter.END,text="#" ,values=value_tuple)

        #mesaje de carga completa
        messagebox.showinfo("Carga completada","Carga completada de archivo excel sea cargado la ruta: " +filename)

    except Exception as ex:
        messagebox.showwarning("Error en la carga",ex)
    return filename

#Inicio de programa
#ventana
root = Tk()
root.title("Consulta de tablas")
root.geometry("950x300")
root.resizable(width=False, height=False)

#frame de tabla de xlsx
framexlsx = Frame(root, border=25)
framexlsx.place(x=5,y=10)

#frame de botones
FrameBotones = Frame(root, border=5,relief=RIDGE)
FrameBotones.place(x=850, y=35)

#Frame de postgre
framepostgre = Frame(root, border=25)
framepostgre.place(x=5,y=315)


#-------------------------------------------------------------Tablas------------------------------------------------------------------------------------
#tabla archivo excell
#Esta tabla muestra los datos extraidos del excel
tabla = ttk.Treeview(framexlsx,columns=("Fecha","Bitacora","Razon social","Rfc"))
tabla.heading("#0",text="Num.", anchor=W)
tabla.column("#0",width=50, stretch=False)

tabla.heading("#1",text="Fecha", anchor=W)
tabla.column("Fecha",width=85, stretch=False)

tabla.heading("#2",text="Bitacora", anchor=W)
tabla.column("Bitacora",width=130, stretch=False)

tabla.heading("#3",text="Razon social", anchor=W)
tabla.column("Razon social",width=400, stretch=False)

tabla.heading("#4",text="Rfc", anchor=W)
tabla.column("Rfc",width=100, stretch=False)
tabla.grid(row=1,column=0)

#Barra de deslizar de la tabla excell
scrollbar = ttk.Scrollbar(framexlsx, orient=tkinter.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=1, sticky='ns')


#-----------------------------------------------------------------------Botones-------------------------------------------------------------------------

#boton carga de archivos framexlsx
buttonCarga = Button(FrameBotones, text="Abrir Excell", command=lambda:cargar_archivo())
buttonCarga.grid(row=0, column=0, sticky=W+E)

#Boton de actualizar
buttonActualizar = Button(FrameBotones, text="Actualizar", command=lambda:Actualizar_datos(ruta))
buttonActualizar.grid(row=1, column=0,sticky=W+E)

#boton de insertar datos 
buttonconexion = Button(FrameBotones, text="Insertar datos", command=lambda:Insertar_datos(ruta))
buttonconexion.grid(row=2, column=0,sticky=W+E)

ruta = cargar_archivo()

root.mainloop()