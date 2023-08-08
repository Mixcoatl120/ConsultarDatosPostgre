#Modulos
import psycopg2
import tkinter
from tkinter import *
from tkinter import messagebox

#Funciones
def est_conexion():
    try:
        conn = psycopg2.connect(      
           dbname = "siset",
           user = "postgres",
           password = "Asea2023",
           host = "localhost",
           port = "5432"
        )
        messagebox.showinfo("conexion exitosa","conexion establecida")
    except Exception as ex:
        messagebox.showinfo("error en la conexion",ex)
    finally:
        conn.close()

#def Actualizar_datos():
    #try:
        #conn = psycopg2.connect(      
           #dbname = "siset",
           #user = "postgres",
           #password = "Asea2023",
           #host = "localhost",
           #port = "5432"
        #)
        #cursor = conn.cursor()
        #query = "UPDATE seguimiento SET rfc=%s  WHERE bitacora_expediente =%s"
        #update = (rfc,bitacora)
        #cursor.execute(query,update)     
    #except Exception as ex:
        #messagebox.showinfo("¡A ocurrido algo inesperado!",ex)


