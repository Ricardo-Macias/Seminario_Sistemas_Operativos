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
        self.letter_textbox_2 = ""

        self.txt_writer = customtkinter.CTkTextbox(self.app, width=250, height=400)
        self.txt_writer.place(x=10, y=50)
        self.txt_read = customtkinter.CTkTextbox(self.app, width=250, height=400)
        self.txt_read.place(x=270, y=50)
        self.txt_read_2 = customtkinter.CTkTextbox(self.app, width=250, height=400)
        self.txt_read_2.place(x=530, y=50)

        self.btn_read = customtkinter.CTkButton(
            self.app, text="Leer", width=50, command=self.reader_writer)
        self.btn_read.place(x=10, y=20)
        self.btn_save = customtkinter.CTkButton(
            self.app, text="Guardar", width=50, command=self.save)
        self.btn_save.place(x=70, y=20)
        self.btn_edit = customtkinter.CTkButton(
            self.app, text="Editar", width=50, command=self.edit)
        self.btn_edit.place(x=140, y=20)

        self.txt_writer.configure(state="disabled")
        self.txt_read.configure(state="disabled")
        self.txt_read_2.configure(state="disabled")

    def edit(self):
        self.txt_writer.configure(state="normal")

    def save(self):
        self.text_txtbox = self.txt_writer.get("1.0", "end-1c")
        self.txt_writer.configure(state="disabled")
    
    def reader_writer(self):
        self.txt_read.configure(state="normal")
        self.txt_read_2.configure(state="normal")

        read = threading.Thread(name="Lector", target=self.reader)
        read2 = threading.Thread(name="Lector_2", target=self.reader)
        write = threading.Thread(name="Escritor", target=self.writer)
        write2 = threading.Thread(name="Escritor_2", target=self.writer_textbox_2)

        read.start()
        read2.start()
        write.start()
        write2.start()
    
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
    
    def writer_textbox_2(self):
            tm = [0.5, 1,2]
            count = 0
            while count < len(self.text_txtbox):
                if self.letter_textbox_2 != "":
                    self.sem.acquire()
                    self.txt_read_2.insert(customtkinter.END, self.letter_textbox_2)
                    self.letter_textbox_2 = ""
                    self.sem.release()
                    time.sleep(tm[random.randint(0, 2)])
                    count += 1
            self.txt_read_2.configure(state="disabled")

if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x500")
    app.title("Practica 8: Producto Consumidor")

    lector_escritor = Interfaz(app)

    app.mainloop()