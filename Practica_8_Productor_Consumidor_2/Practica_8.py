import customtkinter
from tkinter import *

def edit():
    txt_writer.configure(state="normal")
    txt_read.configure(state="normal")
    txt_read_2.configure(state="normal")

if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x500")
    app.title("Practica 8: Producto Consumidor")


    txt_writer = customtkinter.CTkTextbox(app, width=250, height=400)
    txt_writer.place(x=10, y=50)
    txt_read = customtkinter.CTkTextbox(app, width=250, height=400)
    txt_read.place(x=270, y=50)
    txt_read_2 = customtkinter.CTkTextbox(app, width=250, height=400)
    txt_read_2.place(x=530, y=50)

    btn_read = customtkinter.CTkButton(app, text="Leer", width=50)
    btn_read.place(x=10, y=20)
    btn_save = customtkinter.CTkButton(app, text="Guardar", width=50)
    btn_save.place(x=70, y=20)
    btn_edit = customtkinter.CTkButton(app, text="Editar", width=50, command=edit)
    btn_edit.place(x=140, y=20)

    txt_writer.configure(state="disabled")
    txt_read.configure(state="disabled")
    txt_read_2.configure(state="disabled")


    app.mainloop()