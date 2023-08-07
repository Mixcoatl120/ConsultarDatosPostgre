from distutils.util import change_root
import tkinter
import openpyxl
from Conexion_postgre import est_conexion
from tkinter import *
from tkinter import messagebox, filedialog, Tk, ttk, Canvas

#funciones
def cargar_archivo():
    try:
        filename = filedialog.askopenfilename() #lectura de direccion de archivo(Direccion del archivo)
        workbook = openpyxl.load_workbook(filename) # lectura de archivo
        sheet = workbook.active #lectura de la hoja activa 
        lista_valores = list(sheet.values) #crea una lista de los valores que hay en la hoja activa

        #LLenado de datos 
        for value_tuple in lista_valores[1:]:
            tabla.insert('',tkinter.END,text="1" ,values=value_tuple)

        #mesaje de carga completa
        messagebox.showinfo("Carga completada","Carga completada de archivo excel")

    except Exception as ex:
        messagebox.showwarning("Error en la carga",ex)
        




#Inicio de programa

#ventana
root = Tk()
root.title("Consulta de tablas")

#Canvas
canvas = Canvas(root,height=750, width=1500,)
canvas.pack()

#frame1
frame1 = Frame(root, border=25, )
frame1.place(x=5,y=10)

#frame2
frame2 = Frame(root, border=5,relief=RIDGE)
frame2.place(width=190,height=35,x=30, y=280)


#tabla0
#Esta tabla muestra los datos extraidos del excel
tabla = ttk.Treeview(frame1,columns=("Fecha","Bitacora","Razon social","Rfc"))
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

#Barra de deslizar de la tabla
scrollbar = ttk.Scrollbar(frame1, orient=tkinter.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=1, sticky='ns')

#boton carga de archivos .xlsx
buttonCarga = Button(frame2, text="Abrir Excell", command=lambda:cargar_archivo())
buttonCarga.grid(row=0, column=0,sticky='ns')

#boton para establecer la conexion
buttonconexion = Button(frame2, text="Conexion postgres", command=lambda:est_conexion())
buttonconexion.grid(row=0, column=1)



root.mainloop()
