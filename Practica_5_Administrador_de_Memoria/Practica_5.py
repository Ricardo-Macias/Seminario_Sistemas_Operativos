
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

def split_memory(kb,position):
    memory_space.append(kb)
    for count in range(len(memory_space)):
        if count >= position:
            aux = memory_space[count]
            memory_space[count] = kb
            kb = aux

def Primer_ajuste(list_file):
    for count_file in range(len(list_file)):
        file = list_file[count_file].split(",")
        size_file = string_to_int(file[1])
        for count_memory_space in range(len(memory_space)):
            if "." not in memory_space[count_memory_space]:
                memory = string_to_int(memory_space[count_memory_space])
                if size_file <= memory:
                    memory_space[count_memory_space] = file[0] + " (" + str(size_file) + "kb)"
                    kilobytes = str(memory - size_file) + "kb"
                    split_memory(kilobytes, count_memory_space + 1)
                    break

def Mejor_ajuste(list_file):
    for count_file in range(len(list_file)):
        file = list_file[count_file].split(",")
        size_file = string_to_int(file[1])
        aux_memory = 2000
        position = None
        for count_memory_space in range(len(memory_space)):
            if "." not in memory_space[count_memory_space]:
                memory = string_to_int(memory_space[count_memory_space])
                if size_file <= memory and memory <= aux_memory:
                    position = count_memory_space
                    aux_memory = memory
        if position != None:
            memory_space[position] = file[0] + " (" + str(size_file) + "kb)"
            kilobytes = str(aux_memory - size_file) + "kb"
            split_memory(kilobytes, position)

def Peor_ajuste(list_file):
    for count_file in range(len(list_file)):
        file = list_file[count_file].split(",")
        size_file = string_to_int(file[1])
        aux_memory = 0
        position = None
        for count_memory_space in range(len(memory_space)):
            if "." not in memory_space[count_memory_space]:
                memory = string_to_int(memory_space[count_memory_space])
                if size_file <= memory and memory > aux_memory:
                    position = count_memory_space
                    aux_memory = memory
        if position != None:
            memory_space[position] = file[0] + " (" + str(size_file) + "kb)"
            kilobytes = str(aux_memory - size_file) + "kb"
            split_memory(kilobytes, position)

def siguiente_ajuste(list_file):
    count_file = 0
    count_memory_space = 0
    while count_file < len(list_file):
        if count_file == 0:
            file = list_file[count_file].split(",")
            size_file = string_to_int(file[1])
            current_file = file[0]
            position = len(memory_space)
        while count_memory_space < len(memory_space):
            if "." not in memory_space[count_memory_space]:
                memory = string_to_int(memory_space[count_memory_space])
                if size_file <= memory:
                    memory_space[count_memory_space] = file[0] + " (" + str(size_file) + "kb)"
                    kilobytes = str(memory - size_file) + "kb"
                    split_memory(kilobytes, count_memory_space + 1)
                    count_file += 1
                    file = list_file[count_file].split(",")
                    size_file = string_to_int(file[1])
                    current_file = file[0]
                    position = count_memory_space - 1

                elif current_file == file[0] and position == count_memory_space:
                    print("NO hay suficiente espacio pára guardar ", file[0])
                    count_file += 1

            count_memory_space += 1
        count_memory_space = 0


if __name__ == "__main__":
    #Primer_ajuste(Read_file())
    #Mejor_ajuste(Read_file())
    #Peor_ajuste(Read_file())
    siguiente_ajuste(Read_file())
    print(memory_space)
