import os
from random import randint
import customtkinter
from tkinter import filedialog

list_folder = []
list_file = []
list_origin_directory = []
list_copies_directory = []

def Read_file(name):
    with open(name, "r") as file:
        contents = file.read()
    return contents

def create_file(name,text):
    with open(name, "a") as file:
        file.write(text)

def create_folder(name):
    os.mkdir(name)

def ASCII(text):
    new_text = ""
    for count_text in range(len(text)):
        if ord(text[count_text]) >= 65 and ord(text[count_text]) <= 90:
            number_or_letter = chr(randint(48,57))
        elif ord(text[count_text]) >= 48 and ord(text[count_text]) <= 57:
            number_or_letter = chr(randint(65,90))
        else:
            number_or_letter = text[count_text]
        new_text += number_or_letter
    return new_text

def folder_contents():
    list_contents = os.listdir()
    for count_contents in range(len(list_contents)):
        if ".txt" in list_contents[count_contents]:
            list_file.append(list_contents[count_contents])
        else:
            list_folder.append(list_contents[count_contents])
            list_origin_directory.append(os.getcwd() + "\\" + list_contents[count_contents])

def create_copies(text):
    print(list_copies_directory[0])
    os.chdir(list_copies_directory[0])
    for count_file in range(len(list_file)):
        create_file(list_file.pop(0),text)
    for count_folder in range(len(list_folder)):
        folder = list_folder.pop(0)
        create_folder(folder)
        list_copies_directory.append(list_copies_directory[0] + "\\" + folder)

def Batch_processing():
    while len(list_origin_directory) != 0:
        os.chdir(list_origin_directory[0])
        folder_contents()
        if len(list_file) != 0:
            text = Read_file(list_file[0])
            new_text = ASCII(text)
        create_copies(new_text)
        list_origin_directory.pop(0)
        list_copies_directory.pop(0)

def search():
    directory = filedialog.askdirectory(title="Carpeta")
    lbl_directory = customtkinter.CTkLabel(root, text=directory)
    lbl_directory.place(x=10,y=60)
    
    os.chdir(directory)
    list_origin_directory.append(directory)

    copy_folder = directory.split("/")
    name_folder = "Copia_" + copy_folder[len(copy_folder)-1]

    copy_folder.pop()
    origin = copy_folder
    copy_directory = copy_folder

    origin = "\\".join(origin)
    os.chdir(origin)
    create_folder(name_folder)

    copy_directory.append(name_folder)
    copy_directory = "\\".join(copy_directory)

    list_copies_directory.append(copy_directory)
    Batch_processing()
    

if __name__ == "__main__":

    root = customtkinter.CTk()
    root.geometry("600x150")

    btn_search = customtkinter.CTkButton(root,text="Buscar", command=search)
    btn_search.place(x=10,y=10)

    root.mainloop()

