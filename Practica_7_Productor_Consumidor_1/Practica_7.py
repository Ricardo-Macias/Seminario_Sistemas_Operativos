from tkinter import *
from PIL import Image, ImageTk
from random import randint
import time as tm

class car_park:
    def __init__(self,app,car):
        self.app = app
        self.img_car = car
        self.time = [0.5, 1, 2]
        self.carPark = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    def second(self):
        time = randint(0,2)
        return self.time[time]
    
    def parking(self,position):
        if position == 0:
            self.lbl_car_1 = Label(self.app, image=self.img_car)
            self.lbl_car_1.place(x=0, y=35)
        elif position == 1:
            self.lbl_car_2 = Label(self.app, image=self.img_car)
            self.lbl_car_2.place(x=117, y=35)
        elif position == 2:
            self.lbl_car_3 = Label(self.app, image=self.img_car)
            self.lbl_car_3.place(x=240, y=35)
        elif position == 3:
            self.lbl_car_4 = Label(self.app, image=self.img_car)
            self.lbl_car_4.place(x=360, y=35)
        elif position == 4:
            self.lbl_car_5 = Label(self.app, image=self.img_car)
            self.lbl_car_5.place(x=480, y=35)
        elif position == 5:
            self.lbl_car_6 = Label(self.app, image=self.img_car)
            self.lbl_car_6.place(x=600, y=35)
        elif position == 6:
            self.lbl_car_7 = Label(self.app, image=self.img_car)
            self.lbl_car_7.place(x=0, y=260)
        elif position == 7:
            self.lbl_car_8 = Label(self.app, image=self.img_car)
            self.lbl_car_8.place(x=117, y=260)
        elif position == 8:
            self.lbl_car_9 = Label(self.app, image=self.img_car)
            self.lbl_car_9.place(x=240, y=260)
        elif position == 9:
            self.lbl_car_10 = Label(self.app, image=self.img_car)
            self.lbl_car_10.place(x=360, y=260)
        elif position == 10:
            self.lbl_car_11 = Label(self.app, image=self.img_car)
            self.lbl_car_11.place(x=480, y=260)
        elif position == 11:
            self.lbl_car_12 = Label(self.app, image=self.img_car)
            self.lbl_car_12.place(x=600, y=260)
    
    def start_producer(self):
        count_car = 0
        while True:
            if self.carPark[count_car] == 0:
                self.parking(count_car)
                self.carPark[count_car] = 1
                count_car += 1
            if count_car > 11:
                count_car = 0
            tm.sleep(self.second())


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
