import customtkinter
import threading
import random
import time

class Interfaz:
    def __init__(self,app):
        self.app = app
        self.sem = threading.Semaphore(1)
        self.text_txtbox = ""
        self.letter_textbox = ""

    def edit(self):
        self.txt_writer.configure(state="normal")

    def save(self):
        self.text_txtbox = self.txt_writer.get("1.0", "end-1c")
        self.txt_writer.configure(state="disabled")
    
    def reader_writer(self):
        read = threading.Thread(name="Lector", target=self.reader)
        write = threading.Thread(name="Escritor", target=self.writer)

        read.start()
        write.start()
    
    def reader(self):
        tm = [1, 1.5, 2]
        count = 0
        band_1, band_2 = False, False
        while count < len(self.text_txtbox):
            if self.letter_textbox == "":
                self.letter_textbox = self.text_txtbox[count]
                time.sleep(tm[random.randint(0, 2)])
                band_1 = True 
            elif self.letter_textbox_2 == "":
                self.letter_textbox_2 = self.text_txtbox[count]
                time.sleep(tm[random.randint(0, 2)])
                band_2 = True
            if band_1 and band_2:
                count += 1
                band_1, band_2 = False, False
    
    def writer(self):
        tm = [0.5, 1, 2]
        count = 0
        while count < len(self.text_txtbox):
            if self.letter_textbox != "":
                self.sem.acquire()
                self.txt_read.insert(customtkinter.END, self.letter_textbox)
                self.letter_textbox = ""
                self.sem.release()
                time.sleep(tm[random.randint(0, 2)])
                count += 1
        self.txt_read.configure(state="disabled")

if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x500")
    app.title("Practica 8: Producto Consumidor")

    lector_escritor = Interfaz(app)

    txt_writer = customtkinter.CTkTextbox(app, width=250, height=400)
    txt_writer.place(x=10, y=50)
    txt_read = customtkinter.CTkTextbox(
        app, width=250, height=400)
    txt_read.place(x=270, y=50)
    txt_read_2 = customtkinter.CTkTextbox(
        app, width=250, height=400)
    txt_read_2.place(x=530, y=50)

    btn_read = customtkinter.CTkButton(
        app, text="Leer", width=50, command=self.reader_writer)
    btn_read.place(x=10, y=20)
    btn_save = customtkinter.CTkButton(
        app, text="Guardar", width=50, command=self.save)
    btn_save.place(x=70, y=20)
    btn_edit = customtkinter.CTkButton(
        app, text="Editar", width=50, command=self.edit)
    btn_edit.place(x=140, y=20)

    txt_writer.configure(state="disabled")
    txt_read.configure(state="disabled")
    txt_read_2.configure(state="disabled")

    app.mainloop()