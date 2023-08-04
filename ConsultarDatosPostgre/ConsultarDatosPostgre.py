import pandas as pd
from tkinter import filedialog, Tk, ttk, W, E, Canvas, Frame,Button

#funciones
def cargar_archivo():
    file = filedialog.askopenfilename()

#Inicio de programa

root = Tk()
root.title("Consulta de tablas")

#canvas
canvas = Canvas(root, height=350, width=800)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

tabla = ttk.Treeview(frame,columns=)
tabla.grid(row=1,column=1,columnspan=10)
tabla.heading("#0",text="Fecha")
tabla.heading("#1",text="Bitacora")
#tabla.heading("#2",text="Razon social")
#tabla.heading("#3",text="Rfc")

buttonCarga = Button(frame, text="Abrir Excell", command=lambda:cargar_archivo())
buttonCarga.grid(row=10, column=1, sticky=E+W)

root.mainloop()

   
#openFile = pd.read_excel(path,engine="openpyxl",sheet_name="Hoja1" )
#data = openFile.values

#for i in data:
    #print(i)
