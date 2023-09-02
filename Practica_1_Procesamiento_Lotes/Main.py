
def Read_file():
    with open("Practica_1_Procesamiento_Lotes//prueba.txt","r") as file:
        content = file.readlines()
    return content

def Edit_file(line):
    with open("Practica_1_Procesamiento_Lotes//prueba.txt","a") as file:
        file.write(line)

def hexadecimal_to_decimal(letter):
    return str(int(letter,16))


if __name__ == "__main__":
    lines = Read_file()

    print(hexadecimal_to_decimal("A"))
    