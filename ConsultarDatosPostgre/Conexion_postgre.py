#Modulos
import psycopg2
import tkinter
from tkinter import *
from tkinter import messagebox

#-------------------------------------------------------------------------Funciones----------------------------------------------------------------------

#Funcion para saber si se esta estbleciendo la conexion con la base 
def est_conexion():
    try:
        conn = psycopg2.connect(      
           dbname = "siset",
           user = "postgres",
           password = "Asea2023",
           host = "localhost",
           port = "5432"
        )
        messagebox.showinfo("conexion exitosa","conexion establecida")#Dialogo para saber si se complemento la conexion
    except Exception as ex:
        messagebox.showinfo("error en la conexion",ex)#dialogo de error
    finally:
        conn.close()#Cierre de la coneccion

#funcion de actualizacion de datos
def Actualizar_datos(rfc,bitacora):
    try:
        conn = psycopg2.connect(      
           dbname = "siset",
           user = "postgres",
           password = "Asea2023",
           host = "localhost",
           port = "5432"
        )
        cursor = conn.cursor()
        query = "UPDATE seguimiento SET rfc=%s  WHERE bitacora_expediente =%s" #Sentencia // nota: los "%s" se refiere a el dato que se introducira en la union de sentencia y datos
        update = (rfc,bitacora)#Datos que se modificaran en la sentencia
        cursor.execute(query,update)#union de la sentencia y datos a modificar
    except Exception as ex:
        messagebox.showwarning("A ocurrido algo inesperado",ex)#dialogo de error 
    finally:
        conn.close()#Cierre de la conexion

