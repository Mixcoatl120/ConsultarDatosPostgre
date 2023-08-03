import pandas as pd
from tkinter import * 






path = "SS.xlsx"
openFile = pd.read_excel(path,engine="openpyxl",sheet_name="Hoja1" )
data = openFile.values

for i in data:
    print(i)
