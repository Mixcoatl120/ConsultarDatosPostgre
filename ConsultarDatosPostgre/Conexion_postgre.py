from os import close
import psycopg2
from tkinter import messagebox

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



