from tkinter import *
from PIL import Image, ImageTk

class car_park:
    def __init__(self,app):
        self.app = app
        image_carPark = self.loading_image(
            "D:\\Archivos\\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_7_Productor_Consumidor_1\\Estacionamiento.png", 500, 500)
        lbl_image_carPark = Label(self.app, image=image_carPark)

    def loading_image(self, name, width, height):
        img = Image.open(name)
        new_image = img.resize((width, height))
        return ImageTk.PhotoImage(new_image)


if __name__ == "__main__":
    app = Tk()
    app.geometry("500x500")
    app.title("Practica 7: Producto Consumidor 1")

    carPark = car_park(app)

    app.mainloop()
