from tkinter import *
from PIL import Image, ImageTk
from random import randint

class car_park:
    def __init__(self,app):
        self.app = app
        self.time = [0.5, 1, 2]
        self.carPark = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    def second(self):
        time = randint(0,2)
        return self.time[time]

    def loading_image(self, name, width, height):
        img = Image.open(name)
        new_image = img.resize((width, height))
        return ImageTk.PhotoImage(new_image)


if __name__ == "__main__":
    app = Tk()
    app.geometry("700x500")
    app.title("Practica 7: Producto Consumidor 1")

    carPark = car_park(app)

    image_carPark = carPark.loading_image(
        "D:\\Archivos\\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_7_Productor_Consumidor_1\\Estacionamiento.png", 700, 500)
    lbl_image_carPark = Label(app, image=image_carPark)
    lbl_image_carPark.place(x=0, y=0)

    app.mainloop()
