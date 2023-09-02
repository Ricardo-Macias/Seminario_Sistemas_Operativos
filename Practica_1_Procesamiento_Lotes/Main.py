
def Read_file():
    with open("Practica_1_Procesamiento_Lotes//prueba.txt","r") as file:
        content = file.readlines()
    return content

def Edit_file(line):
    with open("Practica_1_Procesamiento_Lotes//prueba.txt","a") as file:
        file.write(line)


if __name__ == "__main__":
    lines = Read_file()
    print(lines[0])
    Edit_file("Line")