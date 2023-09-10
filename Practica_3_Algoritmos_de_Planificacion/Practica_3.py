import time

def Read_file():
    with open("D:\\Archivos\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_3_Algoritmos_de_Planificacion\\procesos.txt", "r") as file:
        return file.readlines()

def lowest_to_highest(list_process, position):
    for count in range(len(list_process)):
        for count_process in range(len(list_process)):
            if count_process + 1 < len(list_process):
                first_process = list_process[count_process].split(",")
                second_process = list_process[count_process + 1].split(",")
                if int(second_process[position]) < int(first_process[position]):
                    first_process = first_process[0] + ", " + first_process[1] + ", " + first_process[2]
                    second_process = second_process[0] + "," + second_process[1] + "," + second_process[2]
                    list_process[count_process] = second_process
                    list_process[count_process + 1] = first_process
    return list_process

def Round_Robin(file):
    while len(file) != 0:
        process = file[0].split(",")
        print("\nProceso: ",process[0])
        process_time = int(process[2])
        for count_quantum in range(3):
            if process_time != 0:
                print(count_quantum + 1, ", ", end="")
                process_time -= 1
                time.sleep(1)
            else:
                break
        file.pop(0)
        if process_time > 0:
            process[2] = process_time
            file.append(process[0] + ", " + process[1] + ", " + str(process[2]))

def SJF(file):
    list_process = lowest_to_highest(file,1)

    for count_process in range(len(list_process)):
        process = list_process[count_process].split(",")
        print("\nProceso: ", process[0])
        for count_time in range(int(process[2])):
            print(count_time + 1, ", ", end="")
            time.sleep(1)
    
def FIFO(file):

    for count_process in range(len(file)):
        process = file[count_process].split(",")
        print("\nProceso: ", process[0])
        for count_time in range(int(process[2])):
            print(count_time + 1, ", ", end="")
            time.sleep(1)

def prioridad(file):
    list_process = lowest_to_highest(file,2)

    for count_process in range(len(list_process)):
        process = list_process[count_process].split(",")
        print("\nProceso: ", process[0])
        for count_time in range(int(process[2])):
            print(count_time + 1, ", ", end="")
            time.sleep(1)
        
if __name__ == "__main__":
    file_process = Read_file()
    #FIFO(file_process)
    #prioridad(file_process)
    #SJF(file_process)
    Round_Robin(file_process)