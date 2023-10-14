import customtkinter
from tkinter import *



if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x500")
    app.title("Practica 8: Producto Consumidor")


    txt_edit = customtkinter.CTkTextbox(app, width=250, height=400)
    txt_edit.place(x=10, y=50)
    txt_2 = customtkinter.CTkTextbox(app, width=250, height=400)
    txt_2.place(x=270, y=50)
    txt_3 = customtkinter.CTkTextbox(app, width=250, height=400)
    txt_3.place(x=530, y=50)

    btn_read = customtkinter.CTkButton(app, text="Leer", width=50)
    btn_read.place(x=10, y=20)
    btn_save = customtkinter.CTkButton(app, text="Guardar", width=50)
    btn_save.place(x=70, y=20)
    btn_edit = customtkinter.CTkButton(app, text="Editar", width=50)
    btn_edit.place(x=140, y=20)



    app.mainloop()