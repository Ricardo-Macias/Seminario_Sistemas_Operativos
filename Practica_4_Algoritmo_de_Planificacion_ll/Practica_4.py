import sys
sys.path.append("D:\\Archivos\\Practicas\\6_Semestre\\Seminario_Sistemas_Operativos")
from Practica_3_Algoritmos_de_Planificacion import Practica_3

import customtkinter
import time

def process(list_process,position=None):
    Frame_process = customtkinter.CTkFrame(root, width=400, height=400)
    Frame_process.place(x=50,y=50)
    y = 0
    if position == 1 or position == 2:
        list_process = Practica_3.lowest_to_highest(list_process,position)
    for count_process in range(len(file)):
        y += 20
        process = list_process[count_process].split(",")
        customtkinter.CTkLabel(Frame_process, text=process[0]).place(x=10, y=y)
        x = 200
        for count_time in range(int(process[2])):
            customtkinter.CTkLabel(Frame_process, text=count_time + 1).place(x=x, y=y)
            root.update()
            x += 20
            time.sleep(1)
    time.sleep(2)
    Frame_process.destroy()

def Round_Robin(file):
    Frame_process = customtkinter.CTkFrame(root, width=400, height=400)
    Frame_process.place(x=50, y=50)
    y = 0
    while len(file) != 0:
        process = file[0].split(",")
        y += 20
        customtkinter.CTkLabel(Frame_process, text=process[0]).place(x=10, y=y)
        process_time = int(process[2])
        x = 200
        for count_quantum in range(3):
            if process_time != 0:
                customtkinter.CTkLabel(Frame_process, text=count_quantum + 1).place(x=x, y=y)
                root.update()
                x += 20
                process_time -= 1
                time.sleep(1)
            else:
                break
        file.pop(0)
        if process_time > 0:
            process[2] = process_time
            file.append(process[0] + ", " + process[1] + ", " + str(process[2]))
    time.sleep(2)
    Frame_process.destroy()
        

def option(option_process):

    if option_process == "FIFO":
        process(file)
    elif option_process == "SJF":
        process(file,2)
    elif option_process == "Prioridad":
        process(file,1)
    elif option_process == "Round Robin":
        Round_Robin(file)

def Register():
    Frame_register = customtkinter.CTkFrame(root, width=400, height=400)
    Frame_register.place(x=50, y=50)

    def exit_register():
        Frame_register.destroy()
        return 0
    
    def add_process():
        new_process = txt_name.get() + ", " + txt_priority.get() + ", " + txt_time.get()
        if cmb_position.get() == "inicio":
            file.insert(0,new_process)
        elif cmb_position.get() == "final":
            file.append(new_process)
        
        txt_name.delete(0, customtkinter.END)
        txt_priority.delete(0, customtkinter.END)
        txt_time.delete(0, customtkinter.END)

    lbl_name = customtkinter.CTkLabel(Frame_register, text="Nombre de Proceso")
    lbl_name.place(x=5,y=5)
    txt_name = customtkinter.CTkEntry(Frame_register)
    txt_name.place(x=5,y=30)

    lbl_time = customtkinter.CTkLabel(Frame_register, text="Tiempo")
    lbl_time.place(x=5, y=70)
    txt_time = customtkinter.CTkEntry(Frame_register)
    txt_time.place(x=5, y=95)

    lbl_priority = customtkinter.CTkLabel(Frame_register, text="Prioridad")
    lbl_priority.place(x=5, y=135)
    txt_priority = customtkinter.CTkEntry(Frame_register)
    txt_priority.place(x=5, y=160)

    cmb_position = customtkinter.CTkComboBox(Frame_register,values=['inicio','final'])
    cmb_position.place(x=5, y=200)

    btn_add = customtkinter.CTkButton(Frame_register, text="Agregar", command=add_process,width=100)
    btn_add.place(x=50, y=250)

    btn_exit = customtkinter.CTkButton(Frame_register, text="Salir", command=exit_register, width=100)
    btn_exit.place(x=160, y=250)
 
if __name__ == "__main__":
    file = Practica_3.Read_file()

    root = customtkinter.CTk()
    root.title("Algoritmos de planificacion")
    root.geometry("500x500")
    
    optionMenu = customtkinter.CTkOptionMenu(root, values=['','FIFO','SJF','Round Robin','Prioridad'], command=option)
    optionMenu.place(x=5,y=5)

    btn = customtkinter.CTkButton(root,text="Registrar",command=Register)
    btn.place(x=200,y=5)

    root.mainloop()