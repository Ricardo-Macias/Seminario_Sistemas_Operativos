
def Read_file():
    with open("D:\\Archivos\\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_5_Administrador_de_Memoria\\archivos.txt", "r") as file:
        content = file.readlines()
    return content


if __name__ == "__main__":
    print(Read_file())