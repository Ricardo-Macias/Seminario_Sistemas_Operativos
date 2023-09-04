import os

list_folder = []
list_file = []

def Read_file(name):
    with open(name, "r") as file:
        contents = file.read()
    return contents

def craete_file(name,text):
    with open(name, "a") as file:
        file.write(text)

def folder_contents():
    list_contents = os.listdir()
    for count_contents in range(len(list_contents)):
        if ".txt" in list_contents[count_contents]:
            list_file.append(list_contents[count_contents])
        else:
            list_folder.append(list_contents[count_contents])


x = "D:\\Archivos\\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_2_Procesamiento_Lotes_ll\\Practica"

if __name__ == "__main__":
    os.chdir(x)
    folder_contents()
    print(list_file)
    print(list_folder)