
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

def Clean_IPv4(IPv4):
    IPv4 = IPv4.split(".")
    aux_IPv4,IPv4_to_hexadecimal = "",""
    for count in range(len(IPv4)):
        aux_IPv4 = decimal_to_hexadecimal(IPv4[count])
        for count_IPv4 in range(len(aux_IPv4)):
            if count_IPv4 > 1:
                IPv4_to_hexadecimal += aux_IPv4[count_IPv4]
        if count != len(IPv4)-1:
            IPv4_to_hexadecimal += "."
    
    return IPv4_to_hexadecimal.upper()

if __name__ == "__main__":
    lines = Read_file()
    new_file = ""

    for count_lines in range(len(lines)):
        line = lines[count_lines].split(",")
        name = line[2]
        IPv6 = Clean_IPv6(line[0])
        IPv4 = Clean_IPv4(line[5])
        new_file = name + " : " + IPv6 + " : " + IPv4 + "\n"
        Edit_file(new_file)


    