from tkinter import *
from PIL import Image, ImageTk

class car_park:
    def _init(self,app):
        self.app = app

    def loading_image(self, name, width, height):
        img = Image.open(name)
        new_image = img.resize(width, height)
        return ImageTk.PhotoImage(new_image)


if __name__ == "__main__":
    app = Tk()
    app.geometry("500x500")
    app.title("Practica 7: Producto Consumidor 1")

    app.mainloop()
