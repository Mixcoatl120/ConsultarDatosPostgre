import tkinter
import openpyxl
from Conexion_postgre import est_conexion
from tkinter import *
from tkinter import messagebox, filedialog, Tk, ttk, Label

#funciones
def cargar_archivo():
    try:
        filename = filedialog.askopenfilename() #lectura de direccion de archivo(Direccion del archivo)
        workbook = openpyxl.load_workbook(filename) # lectura de archivo
        sheet = workbook.active #lectura de la hoja activa 
        lista_valores = list(sheet.values) #crea una lista de los valores que hay en la hoja activa

        #LLenado de datos 
        for value_tuple in lista_valores[1:]:
            i = 0
            i = i + 1
            tabla.insert('',tkinter.END,text=str(i) ,values=value_tuple)

        #mesaje de carga completa
        messagebox.showinfo("Carga completada","Carga completada de archivo excel")

    except Exception as ex:
        messagebox.showwarning("Error en la carga",ex)
        




#Inicio de programa

#ventana
root = Tk()
root.title("Consulta de tablas")
root.geometry("1500x750")
root.resizable(width=False, height=False)

#frame de tabla de xlsx
framexlsx = Frame(root, border=25)
framexlsx.place(x=5,y=10)

#frame de botones
FrameBotones = Frame(root, border=5,relief=RIDGE)
FrameBotones.place(x=30, y=280)

#Frame de postgre
framepostgre = Frame(root, border=25)
framepostgre.place(x=5,y=380)


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

#Tabla de postgres
tablapost = ttk.Treeview(framepostgre ,columns=("Fecha","Bitacora","Razon social","Rfc"))
tablapost.heading("#0",text="Num.", anchor=W)
tablapost.column("#0",width=50, stretch=False)

tablapost.heading("#1",text="Fecha", anchor=W)
tablapost.column("Fecha",width=85, stretch=False)

tablapost.heading("#2",text="Bitacora", anchor=W)
tablapost.column("Bitacora",width=130, stretch=False)

tablapost.heading("#3",text="Razon social", anchor=W)
tablapost.column("Razon social",width=400, stretch=False)

tablapost.heading("#4",text="Rfc", anchor=W)
tablapost.column("Rfc",width=100, stretch=False)
tablapost.grid(row=1,column=0)

#Barra de deslizar de la tabla postgres
scrollbarpos = ttk.Scrollbar(framepostgre, orient=tkinter.VERTICAL, command=tablapost.yview)
tablapost.configure(yscroll = scrollbarpos.set)
scrollbarpos.grid(row=1, column=1, sticky='ns')

#-----------------------------------------------------------------------Botones-------------------------------------------------------------------------

#boton carga de archivos .xlsx
buttonCarga = Button(FrameBotones, text="Abrir Excell", command=lambda:cargar_archivo())
buttonCarga.grid(row=0, column=0,sticky='ns')

#boton para establecer la conexion
buttonconexion = Button(FrameBotones, text="Conexion postgres", command=lambda:est_conexion())
buttonconexion.grid(row=0, column=1)

#-----------------------------------------------------------------------Labels--------------------------------------------------------------------------

#tituli de tabla postgres
titulopostgre = Label(framepostgre,text="Visualizacion de postgre", anchor=W)
titulopostgre.grid(row=0,column=0)

root.mainloop()