import customtkinter
import threading
import random
import time

class Interfaz:
    def __init__(self,app, textbox):
        self.app = app
        self.txt_read = textbox
        self.sem = threading.Semaphore(1)
        self.text_txtbox = ""
        self.letter_textbox = ""

    def save(self,text):
        self.text_txtbox = text
    
    def reader_writer(self):
        read = threading.Thread(name="Lector", target=self.reader)
        write = threading.Thread(name="Escritor", target=self.writer)

        read.start()
        write.start()
    
    def reader(self):
        tm = [1, 1.5, 2]
        count = 0
        while count < len(self.text_txtbox):
            if self.letter_textbox == "":
                self.letter_textbox = self.text_txtbox[count]
                time.sleep(tm[random.randint(0, 2)])
                count += 1
    
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

def edit():
    txt_writer.configure(state="normal")

def save_text():
    txt_writer.configure(state="disabled")
    lector_escritor.save(txt_writer.get("1.0", "end-1c"))
    lector_escritor_2.save(txt_writer.get("1.0", "end-1c"))

def reader_writer():
    txt_read.configure(state="normal")
    txt_read_2.configure(state="normal")
    lector_escritor.reader_writer()
    lector_escritor_2.reader_writer()

if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x500")
    app.title("Practica 8: Producto Consumidor")

    txt_writer = customtkinter.CTkTextbox(app, width=250, height=400)
    txt_writer.place(x=10, y=50)
    txt_read = customtkinter.CTkTextbox(
        app, width=250, height=400)
    txt_read.place(x=270, y=50)
    txt_read_2 = customtkinter.CTkTextbox(
        app, width=250, height=400)
    txt_read_2.place(x=530, y=50)

    btn_read = customtkinter.CTkButton(
        app, text="Leer", width=50, command=reader_writer)
    btn_read.place(x=10, y=20)
    btn_save = customtkinter.CTkButton(
        app, text="Guardar", width=50, command=save_text)
    btn_save.place(x=70, y=20)
    btn_edit = customtkinter.CTkButton(
        app, text="Editar", width=50, command=edit)
    btn_edit.place(x=140, y=20)

    lector_escritor = Interfaz(app, txt_read)
    lector_escritor_2 = Interfaz(app, txt_read_2)

    txt_writer.configure(state="disabled")
    txt_read.configure(state="disabled")
    txt_read_2.configure(state="disabled")

    app.mainloop()