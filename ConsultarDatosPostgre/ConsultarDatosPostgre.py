import tkinter
import openpyxl
from tkinter import *
from tkinter import messagebox, filedialog, Tk, ttk

#funciones
def cargar_archivo():
    try:
        filename = filedialog.askopenfilename() #lectura de direccion de archivo(Direccion del archivo)
        workbook = openpyxl.load_workbook(filename) # lectura de archivo
        sheet = workbook.active #lectura de la hoja activa 
        lista_valores = list(sheet.values) #crea una lista de los valores que hay en la hoja activa

        #LLenado de datos 
        for value_tuple in lista_valores[1:]:
            tabla.insert('',tkinter.END, values=value_tuple)

        #mesaje de carga completa
        messagebox.showinfo("Carga completada","Carga completada de archivo excel")

    except:
        messagebox.showwarning("Error en la carga","Error")
        




#Inicio de programa

#ventana
root = Tk()
root.title("Consulta de tablas")

#frame1
frame1 = Frame(root, height=750, width=1500, bg="red")
frame1.grid(row=0, column=0)

#frame2
frame2 = Frame(root, height=100, width=200, bg="blue")
frame2.grid(row=1, column=0, )

#tabla
tabla = ttk.Treeview(frame1,columns=("Bitacora","Razon social","Rfc"))
tabla.heading("#0",text="Fecha", anchor=W)
tabla.heading("#1",text="Bitacora", anchor=W)
tabla.heading("#2",text="Razon social", anchor=W)
tabla.heading("#3",text="Rfc", anchor=W)
tabla.grid(row=1,column=0)

#Barra de dislizar de la tabla
scrollbar = ttk.Scrollbar(frame1, orient=tkinter.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=1, sticky='ns')

#boton
buttonCarga = Button(frame2, text="Abrir Excell", command=lambda:cargar_archivo())
buttonCarga.grid(row=2, column=0)

root.mainloop()
