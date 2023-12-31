from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import randint
import time as tm
import threading

class car_park:
    def __init__(self,app,car):
        self.app = app
        self.img_car = car
        self.time = [0.5, 1, 2]
        self.carPark = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.time_producer = "Aleatorio"
        self.time_consumer = "Aleatorio"

        barMenu = Menu(self.app)
        editMenu = Menu(barMenu)
        editMenu.add_command(label="Edit", command=self.edit)
        barMenu.add_cascade(label="time",menu=editMenu)
        self.app.config(menu=barMenu)
    
    def edit(self):
        root = Tk()
        root.title("Edit")
        root.geometry("180x180")

        Label(root, text="Productor").place(x=10, y=10)
        variable_producer = StringVar()
        self.cmb_time_producer = ttk.Combobox(
            root, width=17, textvariable=variable_producer)
        self.cmb_time_producer["values"] = ("Aleatorio", "0.5", "1", "2")
        self.cmb_time_producer.place(x=10, y=40)
        self.cmb_time_producer.current(0)

        Label(root, text="Consumidor").place(x=10, y=80)
        variable_consumer = StringVar()
        self.cmb_time_consumer = ttk.Combobox(
            root, width=17, textvariable=variable_consumer)
        self.cmb_time_consumer["values"] = ("Aleatorio", "0.5", "1", "2")
        self.cmb_time_consumer.place(x=10, y=110)
        self.cmb_time_consumer.current(0)

        btn_save = Button(root, text="Guardar", command=self.edit_time)
        btn_save.place(x=20, y=150)

        root.mainloop()
    
    def edit_time(self):
        self.time_consumer = self.cmb_time_consumer.get()
        self.time_producer = self.cmb_time_producer.get()
    
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
    
    def remove(self,position):
        if position == 0:
            self.lbl_car_1.destroy()
        elif position == 1:
            self.lbl_car_2.destroy()
        elif position == 2:
            self.lbl_car_3.destroy()
        elif position == 3:
            self.lbl_car_4.destroy()
        elif position == 4:
            self.lbl_car_5.destroy()
        elif position == 5:
            self.lbl_car_6.destroy()
        elif position == 6:
            self.lbl_car_7.destroy()
        elif position == 7:
            self.lbl_car_8.destroy()
        elif position == 8:
            self.lbl_car_9.destroy()
        elif position == 9:
            self.lbl_car_10.destroy()
        elif position == 10:
            self.lbl_car_11.destroy()
        elif position == 11:
            self.lbl_car_12.destroy()
    
    def start_producer(self):
        count_car = 0
        while True:
            if self.carPark[count_car] == 0:
                self.parking(count_car)
                self.carPark[count_car] = 1
                count_car = count_car + 1
            if count_car > 11:
                count_car = 0
            if self.time_producer == "Aleatorio":
                tm.sleep(self.second())
            else:
                tm.sleep(float(self.time_producer))
    
    def start_consumer(self):
        count_car = 0
        while True:
            if self.carPark[count_car] == 1:
                self.remove(count_car)
                self.carPark[count_car] = 0
                count_car += 1
            if count_car > 11:
                count_car = 0
            if self.time_consumer == "Aleatorio":
                tm.sleep(self.second())
            else:
                tm.sleep(float(self.time_consumer))

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

    productor = threading.Thread(name="Productor", target=carPark.start_producer)
    consumidor = threading.Thread(name="Consumidor", target=carPark.start_consumer)
    productor.start()
    consumidor.start()

    app.mainloop()