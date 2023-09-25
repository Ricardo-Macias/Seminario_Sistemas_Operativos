import customtkinter as ctk
from PIL import Image, ImageTk

def imagen(name):
    img = Image.open(name)
    new_img = img.resize((50,50))
    return ImageTk.PhotoImage(new_img)

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Practica 6: Hilos")
    app.geometry("500x500")

    img = imagen(
        "D:\\Archivos\\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_6_Hilos\\DVD.jpg")
    lbl_imagen_x = ctk.CTkLabel(app, image=img, text="")
    lbl_imagen_x.place(x=10,y=10)

    app.mainloop()