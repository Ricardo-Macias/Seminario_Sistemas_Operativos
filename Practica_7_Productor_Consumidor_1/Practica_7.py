from tkinter import *
from PIL import Image, ImageTk
from random import randint

class car_park:
    def __init__(self,app,car):
        self.app = app
        self.img_car = car
        self.time = [0.5, 1, 2]
        self.carPark = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    def second(self):
        time = randint(0,2)
        return self.time[time]
    
    def start_producer(self):
        lbl = Label(self.app, image=self.img_car)
        lbl.place(x=0,y=40)


def loading_image( name, width, height):
    img = Image.open(name)
    new_image = img.resize((width, height))
    return ImageTk.PhotoImage(new_image)

if __name__ == "__main__":
    app = Tk()
    app.geometry("700x500")
    app.title("Practica 7: Producto Consumidor 1")

    image_carPark = loading_image(
        "D:\\Archivos\\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_7_Productor_Consumidor_1\\Estacionamiento.png", 700, 500)
    lbl_image_carPark = Label(app, image=image_carPark).pack()

    img_car = loading_image(
        "D:\\Archivos\\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_7_Productor_Consumidor_1\\Vehiculo.png", 100, 195)

    carPark = car_park(app,img_car)

    
    carPark.start_producer()

    app.mainloop()
