
def Read_file():
    with open("Practica_1_Procesamiento_Lotes//prueba.txt","r") as file:
        content = file.readlines()
    return content

def Edit_file(line):
    with open("Practica_1_Procesamiento_Lotes//Salida.txt","a") as file:
        file.write(line)

def hexadecimal_to_decimal(letter):
    return str(int(letter,16))

def decimal_to_hexadecimal(number):
    return str(hex(int(number)))

def Clean_IPv6(IPv6):
    aux_IPv6 = ""
    IPv6_to_decimal = ""
    for count in range(len(IPv6)):
        if IPv6[count] == "/":
            return IPv6_to_decimal + hexadecimal_to_decimal(aux_IPv6)
        elif IPv6[count] == ":":
            IPv6_to_decimal += hexadecimal_to_decimal(aux_IPv6) + ":"
            aux_IPv6 = ""
        else:
            aux_IPv6 += IPv6[count]


if __name__ == "__main__":
    lines = Read_file()

    line = lines[0].split(',')
    print(Clean_IPv6(line[0]))

    