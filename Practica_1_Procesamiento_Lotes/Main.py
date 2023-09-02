
def Read_file():
    with open("Practica_1_Procesamiento_Lotes//prueba.txt","r") as file:
        content = file.readlines()
    return content

def Edit_file(line):
    with open("Practica_1_Procesamiento_Lotes//prueba.txt","a") as file:
        file.write(line)

def hexadecimal_to_decimal(letter):
    return str(int(letter,16))

def decimal_to_hexadecimal(number):
    return str(hex(int(number)))


if __name__ == "__main__":
    lines = Read_file()

    print(decimal_to_hexadecimal(10))

    