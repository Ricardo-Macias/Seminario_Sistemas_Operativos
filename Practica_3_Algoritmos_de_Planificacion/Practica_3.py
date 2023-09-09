import time

def Read_file():
    with open("D:\\Archivos\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_3_Algoritmos_de_Planificacion\\procesos.txt", "r") as file:
        return file.readlines()
    

def FIFO(file):

    for count_process in range(len(file)):
        process = file[count_process].split(",")
        print("\nProceso: ", process[0])
        for count_time in range(int(process[2])):
            print(count_time + 1, ", ", end="")
            time.sleep(1)

def prioridad(file):
    list_process = lowest_to_highest(file)

    for count_process in range(len(list_process)):
        process = list_process[count_process].split(",")
        print("\nProceso: ", process[0])
        for count_time in range(int(process[2])):
            print(count_time + 1, ", ", end="")
            time.sleep(1)
        


if __name__ == "__main__":
    file_process = Read_file()
    #FIFO(file_process)
    
