import time

def Read_file():
    with open("D:\\Archivos\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_3_Algoritmos_de_Planificacion\\procesos.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    process = Read_file()
    print(process)
