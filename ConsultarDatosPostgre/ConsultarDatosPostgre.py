from math import e
from sys import exception
import pandas as pd
import openpyxl as op
from tkinter import filedialog, Tk, ttk, W, E, Canvas, Frame,Button, messagebox

#funciones
def cargar_archivo():
    filename = filedialog.askopenfilename()
    try:
        openFile = pd.read_excel(filename,engine="openpyxl",sheet_name="Hoja1" )
        data = openFile.values
    except(exception):
        print("Hubo un error inesperado"+ e)
    finally:
        print(messagebox.Message("Carga de archivos completa"))

    #for i  in data:
        #print(data)
        #tabla.insert('',0,)





#Inicio de programa

root = Tk()
root.title("Consulta de tablas")

#canvas
canvas = Canvas(root, height=600, width=1500)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

tabla = ttk.Treeview(frame,columns=("Fecha","Bitacora","Razon social","Rfc"))
tabla.grid(row=1,column=1,columnspan=1,)
tabla.heading("#0",text="Fecha")
tabla.heading("#1",text="Bitacora")
tabla.heading("#2",text="Razon social")
tabla.heading("#3",text="Rfc")

buttonCarga = Button(frame, text="Abrir Excell", command=lambda:cargar_archivo())
buttonCarga.grid(row=2, column=1)

root.mainloop()

   


#for i in data:
    #print(i)
