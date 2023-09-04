import os

list_folder = []
list_file = []
original = []
copies = []

def Read_file(name):
    with open(name, "r") as file:
        contents = file.read()
    return contents

def create_file(name,text):
    with open(name, "a") as file:
        file.write(text)

def create_folder(name):
    os.mkdir(name)

def folder_contents():
    list_contents = os.listdir()
    for count_contents in range(len(list_contents)):
        if ".txt" in list_contents[count_contents]:
            list_file.append(list_contents[count_contents])
        else:
            list_folder.append(list_contents[count_contents])
            original.append(os.getcwd() + "\\" + list_contents[count_contents])


def create_copies(text):
    print(copies[0])
    os.chdir(copies[0])
    for count_file in range(len(list_file)):
        create_file(list_file.pop(0),text)
    for count_folder in range(len(list_folder)):
        folder = list_folder.pop(0)
        create_folder(folder)
        copies.append(copies[0] + "\\" + folder)



def Batch_processing():
    while len(original) != 0:
        os.chdir(original[0])
        folder_contents()
        if len(list_file) != 0 or len(list_folder) != 0:
            create_copies("Hola")
        original.pop(0)
        copies.pop(0)

x = "D:\\Archivos\\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_2_Procesamiento_Lotes_ll\\Practica"

if __name__ == "__main__":


    os.chdir(x)
    original.append(x)

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

    copies.append(copy_folder)

    Batch_processing()

    
    