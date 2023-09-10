import sys
sys.path.append("D:\\Archivos\\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos")
from Practica_3_Algoritmos_de_Planificacion import Practica_3

import customtkinter
import time

def process(list_process,position=None):
    y = 0
    if position == 1 or position == 2:
        list_process = Practica_3.lowest_to_highest(list_process,position)
    for count_process in range(len(file)):
        y += 20
        process = list_process[count_process].split(",")
        customtkinter.CTkLabel(root, text=process[0]).place(x=30,y=y)
        x = 300
        for count_time in range(int(process[2])):
            customtkinter.CTkLabel(root, text=count_time + 1).place(x=x,y=y)
            root.update()
            x += 20
            time.sleep(1)

def option(option_process):

    if option_process == "FIFO":
        process(file)
    elif option_process == "SJF":
        process(file,2)
    elif option_process == "Prioridad":
        process(file,1)
    elif option_process == "Round Robin":
        Practica_3.Round_Robin(file)
 
if __name__ == "__main__":
    file = Practica_3.Read_file()

    root = customtkinter.CTk()
    root.title("Algoritmos de planificacion")
    root.geometry("200x200")
    
    optionMenu = customtkinter.CTkOptionMenu(root, values=['','FIFO','SJF','Round Robin','Prioridad'], command=option)
    optionMenu.place(x=5,y=5)

    root.mainloop()