import customtkinter as ctk
from PIL import Image, ImageTk
import threading
import time

class move_image:
    def __init__(self,app ,image, x=int, y=int):
        self.app = app
        self.image = image
        self.x = x
        self.y = y
    
    def limit(self):
        if self.x >= 500 or self.y >= 500:
            self.band = True
        elif self.x <= 0 or self.y <= 0:
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
            time.sleep(0.15)
            self.lbl_image.destroy()

    def up_to_down(self):
        while True:
            self.limit()
            if self.band:
                self.y -= 10
            else:
                self.y += 10
            self.lbl_image = ctk.CTkLabel(self.app, image=self.image, text="")
            self.lbl_image.place(x=self.x, y=self.y)
            time.sleep(0.15)
            self.lbl_image.destroy()

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
    
    obj_img_1 = move_image(app,img,0,0)
    obj_img_2 = move_image(app,img, 0,0)

    t1 = threading.Thread(name="Hilo_1", target=obj_img_1.left_to_right)
    t2 = threading.Thread(name="Hilo_2", target=obj_img_2.up_to_down)

    t1.start()
    t2.start()

    app.mainloop()