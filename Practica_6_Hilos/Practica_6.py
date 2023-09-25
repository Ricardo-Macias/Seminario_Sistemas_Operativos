from tkinter import *
from PIL import Image, ImageTk
import threading
import time

class move_image:
    def __init__(self,app ,image, x_or_y=int):
        self.app = app
        self.image = image
        self.x_or_y = x_or_y
    
    def limit(self):
        if self.x_or_y >= 450:
            self.band = True
        elif self.x_or_y <= 0:
            self.band = False
    
    def left_to_right(self):
        lbl_image = Label(self.app, image=self.image)
        while True:
            self.limit()
            if self.band:
                self.x_or_y -= 10
            else:
                self.x_or_y += 10
            lbl_image.place(x=self.x_or_y, y=0)
            time.sleep(0.15)

    def up_to_down(self):
        lbl_image = Label(self.app, image=self.image)
        while True:
            self.limit()
            if self.band:
                self.x_or_y -= 10
            else:
                self.x_or_y += 10
            lbl_image.place(x=0, y=self.x_or_y)
            time.sleep(0.15)

def imagen(name):
    img = Image.open(name)
    new_img = img.resize((50,50))
    return ImageTk.PhotoImage(new_img)

if __name__ == "__main__":
    app = Tk()
    app.title("Practica 6: Hilos")
    app.geometry("500x500")

    img = imagen(
        "D:\\Archivos\\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_6_Hilos\\DVD.jpg")
    
    obj_img_1 = move_image(app,img,0)
    obj_img_2 = move_image(app,img, 0)

    t1 = threading.Thread(name="Hilo_1", target=obj_img_1.left_to_right)
    t2 = threading.Thread(name="Hilo_2", target=obj_img_2.up_to_down)

    t1.start()
    t2.start()

    app.mainloop()