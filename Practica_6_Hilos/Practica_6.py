import customtkinter as ctk
from PIL import Image, ImageTk

class move_image:
    def __init__(self,app ,image, x, y):
        self.app = app
        self.image = image
        self.x = x
        self.y = y
    
    def limit(self):
        if self.x >= 500:
            self.band = True
        elif self.y <= 0:
            self.band = False
    
    def left_to_right(self):
        while True:
            self.limit()
            if self.band:
                self.x -= 10
            else:
                self.x += 10
            self.lbl_image = ctk.CTkLabel(self.app, image=self.image, text="")
            self.lbl_image.place(x=self.x, y=self.y)
    
    def up_to_down(self):
        while True:
            self.limit()
            if self.band:
                self.y -= 10
            else:
                self.y += 10
            self.lbl_image = ctk.CTkLabel(self.app, image=self.image, text="")
            self.lbl_image.place(x=self.x, y=self.y)

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