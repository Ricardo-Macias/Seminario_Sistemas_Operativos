
memory_space = ['1000kb', '400kb', '1800kb','700kb', '900kb', '1200kb', '1500kb']

def Read_file():
    with open("D:\\Archivos\\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos\\Practica_5_Administrador_de_Memoria\\archivos.txt", "r") as file:
        content = file.readlines()
    return content

def string_to_int(kb):
    kilobytes = ""
    for count_kb in kb:
        if count_kb == "k":
            return int(kilobytes)
        else:
            kilobytes += count_kb


if __name__ == "__main__":
    print(string_to_int(memory_space[1]))
