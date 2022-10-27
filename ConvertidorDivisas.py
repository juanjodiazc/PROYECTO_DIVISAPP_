import tkinter as tk
from tkinter import ttk

def convertir_divs():
    pesos_c = float(caja_conv_colombianos.get())
    conv_dolares = pesos_c * 0.00020477317
    conv_euro = pesos_c*0.00020298273

#Etiquetas
    Conv_dolares.config(text=f"Pesos colombia en Dolares:{conv_dolares} ")
    Conv_euro.config(text=f"Pesos colombia en Euro: {conv_euro} " )

ventana = tk.Tk()
ventana.title("Conversor de divisas")
ventana.config(width=400, height=300)

#Etiqueta
conv_colombianos = ttk.Label(text="Pesos colombianos --> ")
conv_colombianos.place(x=20, y=20)

#Caja
caja_conv_colombianos = ttk.Entry()
caja_conv_colombianos.place(x=140,y=20,width=60)

#Botón
boton_convertir = ttk.Button(text="Convertir", command = convertir_divs)
boton_convertir.place(x=20,y=60)

#Dolares
Conv_dolares = ttk.Label(text="Valor en Dolares --> n/a")
Conv_dolares.place(x=20, y=120)

#Euros
Conv_euro = ttk.Label(text="Valor en Euros --> n/a")
Conv_euro.place(x=20, y=160)


ventana.mainloop()


