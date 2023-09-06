import os
from random import randint

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

x = "D:\\Archivos\\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_2_Procesamiento_Lotes_ll\\Practica"

if __name__ == "__main__":


    os.chdir(x)
    list_origin_directory.append(x)

    copy_folder = x.split("\\")
    name_folder = "Copia_"  + copy_folder[len(copy_folder)-1]

    copy_folder.pop()
    copy_folder = "\\".join(copy_folder)
    os.chdir(copy_folder)
    create_folder(name_folder)

    copy_folder = x.split("\\")
    copy_folder.pop()
    copy_folder.append(name_folder)
    copy_folder = "\\".join(copy_folder) 

    list_copies_directory.append(copy_folder)

    Batch_processing()


