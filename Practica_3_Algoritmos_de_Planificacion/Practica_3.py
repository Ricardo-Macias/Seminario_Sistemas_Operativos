import time

def Read_file():
    with open("D:\\Archivos\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_3_Algoritmos_de_Planificacion\\procesos.txt", "r") as file:
        return file.readlines()

def FIFO(file):

    for count_process in range(len(file)):
        print(file[count_process])

        



if __name__ == "__main__":
    file = Read_file()
    print(file)
    #FIFO(file)
    
