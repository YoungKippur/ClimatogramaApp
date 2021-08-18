from tkinter.constants import W
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import numpy as np

# auto-py-to-exe

# Parte de la interfaz ----------------------------------------------------------------------

ventana = tk.Tk()
ventana.geometry("850x400")
ventana.title("Climatogramas By M.S")

textoTittle = tk.StringVar(value = "Climatograma")
textoButtonTemp = tk.StringVar(value = "Off")
textoButtonCuadro = tk.StringVar(value = "Off")

estadoButtonTemp = tk.BooleanVar(value = False)
estadoButtonCuadro = tk.BooleanVar(value = False) 

textoNotas1 = tk.StringVar()
textoNotas2 = tk.StringVar()
textoNotas3 = tk.StringVar()
textoNotas4 = tk.StringVar()
textoNotas5 = tk.StringVar()
textoNotas6 = tk.StringVar()
textoNotas7 = tk.StringVar()

def buttonCuadro():
    if estadoButtonCuadro.get() == True:
        textoButtonCuadro.set("Off")
        estadoButtonCuadro.set(False)
        B3 = tk.Button(ventana, text = textoButtonCuadro.get(), command = buttonCuadro)
        B3.place (x = 355, y = 335)

    else:
        textoButtonCuadro.set("On")
        estadoButtonCuadro.set(True)
        B3 = tk.Button(ventana, text = textoButtonCuadro.get(), command = buttonCuadro)
        B3.place (x = 355, y = 335)

def buttonTemp():
    if estadoButtonTemp.get() == True:
        textoButtonTemp.set("Off")
        estadoButtonTemp.set(False)
        B2 = tk.Button(ventana, text = textoButtonTemp.get(), command = buttonTemp)
        B2.place (x = 355, y = 365)

    else:
        textoButtonTemp.set("On")
        estadoButtonTemp.set(True)
        B2 = tk.Button(ventana, text = textoButtonTemp.get(), command = buttonTemp)
        B2.place (x = 355, y = 365)


def buttonGraficar():
    tm1 = float(E1.get())
    tm2 = float(E2.get())
    tm3 = float(E3.get())
    tm4 = float(E4.get())
    tm5 = float(E5.get())
    tm6 = float(E6.get())
    tm7 = float(E7.get())
    tm8 = float(E8.get())
    tm9 = float(E9.get())
    tm10 = float(E10.get())
    tm11 = float(E11.get())
    tm12 = float(E12.get())

    m1 = float(EM1.get())
    m2 = float(EM2.get())
    m3 = float(EM3.get())
    m4 = float(EM4.get())
    m5 = float(EM5.get())
    m6 = float(EM6.get())
    m7 = float(EM7.get())
    m8 = float(EM8.get())
    m9 = float(EM9.get())
    m10 = float(EM10.get())
    m11 = float(EM11.get())
    m12 = float(EM12.get())

    M1 = float(EMM1.get())
    M2 = float(EMM2.get())
    M3 = float(EMM3.get())
    M4 = float(EMM4.get())
    M5 = float(EMM5.get())
    M6 = float(EMM6.get())
    M7 = float(EMM7.get())
    M8 = float(EMM8.get())
    M9 = float(EMM9.get())
    M10 = float(EMM10.get())
    M11 = float(EMM11.get())
    M12 = float(EMM12.get())

    p1 = float(EP1.get())
    p2 = float(EP2.get())
    p3 = float(EP3.get())
    p4 = float(EP4.get())
    p5 = float(EP5.get())
    p6 = float(EP6.get())
    p7 = float(EP7.get())
    p8 = float(EP8.get())
    p9 = float(EP9.get())
    p10 = float(EP10.get())
    p11 = float(EP11.get())
    p12 = float(EP12.get())

    l1 = float(EL1.get())
    l2 = float(EL2.get())
    l3 = float(EL102.get())

    et1 = ET1.get()

    x = [1,2,3,4,5,6,7,8,9,10,11,12]  # Meses
    y = [tm1,tm2,tm3,tm4,tm5,tm6,tm7,tm8,tm9,tm10,tm11,tm12] # Temperaturas (media)
    y1 = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12] # Minima
    y2 = [M1,M2,M3,M4,M5,M6,M7,M8,M9,M10,M11,M12] # Maxima
    z = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12] # Precipitaciones (o algo asi)

    # Aca va el cuadro
    if estadoButtonCuadro.get() == True:
        ventana2 = tk.Tk()
        ventana2.title("Cuadro de " + et1)
        ventana2.geometry("960x200")

        cuadro = ttk.Treeview(ventana2)

        cuadro['columns'] = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        
        cuadro.column("#0", width = 150, minwidth = 25)
        cuadro.column("Enero", anchor = W, width = 60)
        cuadro.column("Febrero", anchor = W, width = 60)
        cuadro.column("Marzo", anchor = W, width = 60)
        cuadro.column("Abril", anchor = W, width = 60)
        cuadro.column("Mayo", anchor = W, width = 60)
        cuadro.column("Junio", anchor = W, width = 60)
        cuadro.column("Julio", anchor = W, width = 60)
        cuadro.column("Agosto", anchor = W, width = 60)
        cuadro.column("Septiembre", anchor = W, width = 80)
        cuadro.column("Octubre", anchor = W, width = 60)
        cuadro.column("Noviembre", anchor = W, width = 80)
        cuadro.column("Diciembre", anchor = W, width = 80)
        
        cuadro.heading("#0", text = " ", anchor = W)
        cuadro.heading("Enero", text = "Enero", anchor = W)
        cuadro.heading("Febrero", text = "Febrero", anchor = W)
        cuadro.heading("Marzo", text = "Marzo", anchor = W)
        cuadro.heading("Abril", text = "Abril", anchor = W)
        cuadro.heading("Mayo", text = "Mayo", anchor = W)
        cuadro.heading("Junio", text = "Junio", anchor = W)
        cuadro.heading("Julio", text = "Julio", anchor = W)
        cuadro.heading("Agosto", text = "Agosto", anchor = W)
        cuadro.heading("Septiembre", text = "Septiembre", anchor = W)
        cuadro.heading("Octubre", text = "Octubre", anchor = W)
        cuadro.heading("Noviembre", text = "Noviembre", anchor = W)
        cuadro.heading("Diciembre", text = "Diciembre", anchor = W)

        vacio = [" "," "," "," "," "," "," "," "," "," "," "," "]
        amplitudTermMes = list(np.array(y2) - np.array(y1))

        if estadoButtonTemp.get() == True:
            cuadro.insert(parent = '', index = 'end', iid = "0", text = "Temp Maxima (°C)", values = y2)
        
        cuadro.insert(parent = '', index = 'end', iid = "1", text = "Temp Promedio (°C)", values = y)
        
        if estadoButtonTemp.get() == True:
            cuadro.insert(parent = '', index = 'end', iid = "2", text = "Temp Minima (°C)", values = y1)
        
        cuadro.insert(parent = '', index = 'end', iid = "3", text = "Precipitación (mm)", values = z)
        
        if estadoButtonTemp.get() == True:
            cuadro.insert(parent = '', index = 'end', iid = "4", text = " ", values = vacio)
            cuadro.insert(parent = '', index = 'end', iid = "5", text = "Amp. Termica Mensual", values = amplitudTermMes)

        cuadro.pack(pady=20)

    # Aca van las notas (Falta:  Amplitud termica)

    promedioT = sum(y) / 12
    presipitacionAnual = sum(z)
    # mayorMes = y.index(max(y)) + 1
    # menorMes = y.index(min(y)) + 1

    amplitudTermAnual = max(y) - min(y)


    if promedioT >= 20:
        textoNotas1.set("Clima CALIDO (Temp Promedio: " + str(promedioT) + ")             ")
        L21 = tk.Label (ventana, text = textoNotas1.get())
        L21.place(x = 550, y = 80)
    elif promedioT <= 9:
        textoNotas1.set("Clima FRIO (Temp Promedio: " + str(promedioT) + ")             ")
        L21 = tk.Label (ventana, text = textoNotas1.get())
        L21.place(x = 550, y = 80)
    else:
        textoNotas1.set("Clima TEMPLADO (Temp. Promedio: " + str(promedioT) + ")             ")
        L21 = tk.Label (ventana, text = textoNotas1.get())
        L21.place(x = 550, y = 80)

    if presipitacionAnual >= 1000:
        textoNotas2.set("Clima HUMEDO (Presi. Anuales: " + str(presipitacionAnual) + ")             ")
        L2102 = tk.Label (ventana, text = textoNotas2.get())
        L2102.place(x = 550, y = 100)
    elif presipitacionAnual < 1000 and presipitacionAnual >= 500:
        textoNotas2.set("Clima SEMIHUMEDO (Presi. Anuales: " + str(presipitacionAnual) + ")             ")
        L2102 = tk.Label (ventana, text = textoNotas2.get())
        L2102.place(x = 550, y = 100)
    elif presipitacionAnual < 500 and presipitacionAnual >= 200:
        textoNotas2.set("Clima SEMIARIDO (Presi. Anuales: " + str(presipitacionAnual) + ")             ")
        L2102 = tk.Label (ventana, text = textoNotas2.get())
        L2102.place(x = 550, y = 100)
    else:
        textoNotas2.set("Clima ARIDO (Presi. Anuales: " + str(presipitacionAnual) + ")             ")
        L2102 = tk.Label (ventana, text = textoNotas2.get())
        L2102.place(x = 550, y = 100)
    
    if estadoButtonTemp.get() == True:
        textoNotas3.set("Mayor Temperatura: " + str(max(y2)) + "             ")
        L2103 = tk.Label (ventana, text = textoNotas3.get())
        L2103.place(x = 550, y = 120)
    else:
        textoNotas3.set("Mayor Temperatura: " + str(max(y)) + "             ")
        L2103 = tk.Label (ventana, text = textoNotas3.get())
        L2103.place(x = 550, y = 120)

    if estadoButtonTemp.get() == True:
        textoNotas4.set("Menor Temperatura: " + str(min(y1)) + "             ")
        L2104 = tk.Label (ventana, text = textoNotas4.get())
        L2104.place(x = 550, y = 140)
    else:
        textoNotas4.set("Menor Temperatura: " + str(min(y)) + "             ")
        L2104 = tk.Label (ventana, text = textoNotas4.get())
        L2104.place(x = 550, y = 140)

    textoNotas5.set("Amplitud Termica Anual: " + str(amplitudTermAnual) + "             ")
    L2105 = tk.Label (ventana, text = textoNotas5.get())
    L2105.place(x = 550, y = 160)


    textoNotas6.set("Para ver la Amplitud Termica mensual active las")
    L2106 = tk.Label (ventana, text = textoNotas6.get())
    L2106.place(x = 550, y = 200)

    textoNotas7.set("opciones de cuadro y Temp maxima y minima")
    L2107 = tk.Label (ventana, text = textoNotas7.get())
    L2107.place(x = 550, y = 220)

    # Fin De Las Notas

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.set_xticks(x)

    ax1.set_ylim(0,  l2)
    ax2.set_ylim(l3,  l1)

    ax1.yaxis.set_label_position("right")
    ax1.yaxis.tick_right()
    ax2.yaxis.set_label_position("left")
    ax2.yaxis.tick_left()
    ax1.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)

    ax2.plot(x, y, label="Media", color='g')
    if estadoButtonTemp.get() == True:
        ax2.plot(x, y2, label="Maxima", color='r')
        ax2.plot(x, y1, label="Minima", color='b')
    ax1.bar(x, z, label="Y2", color='pink', width=0.9)

    plt.scatter(x, y, color='g')
    if estadoButtonTemp.get() == True:
        plt.scatter(x, y2, color='r')
        plt.scatter(x, y1, color='b')

    ax1.set_ylabel("Precipitación (mm)")
    ax2.set_ylabel("Temperatura (°C)")
    ax2.legend(loc = "upper left")

    plt.suptitle(et1)
    #plt.title("By Young Kippur")
    plt.show()

    if estadoButtonCuadro.get() == True:
        cuadro.mainloop()

    


# Labels

L1 = tk.Label (ventana, text = "Mes")
L1.place(x = 20, y = 10)

L2 = tk.Label (ventana, text = "Temp Media")
L2.place(x = 60, y = 10)

L3 = tk.Label (ventana, text = "Temp Minima")
L3.place(x = 180, y = 10)

L4 = tk.Label (ventana, text = "Temp Maxima")
L4.place(x = 300, y = 10)

L5 = tk.Label (ventana, text = "Precipitaciones")
L5.place(x = 420, y = 10)

L6 = tk.Label (ventana, text = "1")
L6.place(x = 25, y = 35)

L7 = tk.Label (ventana, text = "2")
L7.place(x = 25, y = 60)

L8 = tk.Label (ventana, text = "3")
L8.place(x = 25, y = 85)

L9 = tk.Label (ventana, text = "4")
L9.place(x = 25, y = 110)

L10 = tk.Label (ventana, text = "5")
L10.place(x = 25, y = 135)

L11 = tk.Label (ventana, text = "6")
L11.place(x = 25, y = 160)

L12 = tk.Label (ventana, text = "7")
L12.place(x = 25, y = 185)

L13 = tk.Label (ventana, text = "8")
L13.place(x = 25, y = 210)

L14 = tk.Label (ventana, text = "9")
L14.place(x = 25, y = 235)

L15 = tk.Label (ventana, text = "10")
L15.place(x = 25, y = 260)

L16 = tk.Label (ventana, text = "11")
L16.place(x = 25, y = 285)

L17 = tk.Label (ventana, text = "12")
L17.place(x = 25, y = 310)

L18 = tk.Label (ventana, text = "By Marcos Strauss") # El importante
L18.place(x = 10, y = 370)

L18 = tk.Label (ventana, text = "LimMax. Grados:")
L18.place(x = 400, y = 365)

L1802 = tk.Label (ventana, text = "LimMin. Grados:")
L1802.place(x = 400, y = 335)


L18 = tk.Label (ventana, text = "Lim. Precipitaciones:")
L18.place(x = 520, y = 365)

L19 = tk.Label (ventana, text = "Temp Max & Min:")
L19.place(x = 245, y = 365)

L20 = tk.Label (ventana, text = "Notas:")
L20.place(x = 540, y = 60)

L21 = tk.Label (ventana, text = textoNotas1.get())
L21.place(x = 550, y = 80)

L2102 = tk.Label (ventana, text = textoNotas2.get())
L2102.place(x = 550, y = 100)

L2103 = tk.Label (ventana, text = textoNotas3.get())
L2103.place(x = 550, y = 120)

L2104 = tk.Label (ventana, text = textoNotas4.get())
L2104.place(x = 550, y = 140)

L2105 = tk.Label (ventana, text = textoNotas5.get())
L2105.place(x = 550, y = 160)

L2106 = tk.Label (ventana, text = textoNotas6.get())
L2106.place(x = 550, y = 180)

L2107 = tk.Label (ventana, text = textoNotas7.get())
L2107.place(x = 550, y = 220)

L22 = tk.Label (ventana, text = "Nombre:")
L22.place(x = 575, y = 10)

L23 = tk.Label (ventana, text = "Cuadro:")
L23.place(x = 300, y = 335)

# Entrys "Temp Media"

E1 = tk.Entry (ventana, width = 4)
E1.insert(tk.END, '0')
E1.place(x = 65, y = 35)

E2 = tk.Entry (ventana, width = 4)
E2.insert(tk.END, '0')
E2.place(x = 65, y = 60)

E3 = tk.Entry (ventana, width = 4) # E3 (Referencia gamer no lo entenderias) 
E3.insert(tk.END, '0')
E3.place(x = 65, y = 85)

E4 = tk.Entry (ventana, width = 4)
E4.insert(tk.END, '0')
E4.place(x = 65, y = 110)

E5 = tk.Entry (ventana, width = 4)
E5.insert(tk.END, '0')
E5.place(x = 65, y = 135)

E6 = tk.Entry (ventana, width = 4)
E6.insert(tk.END, '0')
E6.place(x = 65, y = 160)

E7 = tk.Entry (ventana, width = 4)
E7.insert(tk.END, '0')
E7.place(x = 65, y = 185)

E8 = tk.Entry (ventana, width = 4)
E8.insert(tk.END, '0')
E8.place(x = 65, y = 210)

E9 = tk.Entry (ventana, width = 4)
E9.insert(tk.END, '0')
E9.place(x = 65, y = 235)

E10 = tk.Entry (ventana, width = 4)
E10.insert(tk.END, '0')
E10.place(x = 65, y = 260)

E11 = tk.Entry (ventana, width = 4)
E11.insert(tk.END, '0')
E11.place(x = 65, y = 285)

E12 = tk.Entry (ventana, width = 4)
E12.insert(tk.END, '0')
E12.place(x = 65, y = 310)

# Entrys "Temp Minima"

EM1 = tk.Entry (ventana, width = 4)
EM1.insert(tk.END, '0')
EM1.place(x = 185, y = 35)

EM2 = tk.Entry (ventana, width = 4)
EM2.insert(tk.END, '0')
EM2.place(x = 185, y = 60)

EM3 = tk.Entry (ventana, width = 4)
EM3.insert(tk.END, '0')
EM3.place(x = 185, y = 85)

EM4 = tk.Entry (ventana, width = 4)
EM4.insert(tk.END, '0')
EM4.place(x = 185, y = 110)

EM5 = tk.Entry (ventana, width = 4)
EM5.insert(tk.END, '0')
EM5.place(x = 185, y = 135)

EM6 = tk.Entry (ventana, width = 4)
EM6.insert(tk.END, '0')
EM6.place(x = 185, y = 160)

EM7 = tk.Entry (ventana, width = 4)
EM7.insert(tk.END, '0')
EM7.place(x = 185, y = 185)

EM8 = tk.Entry (ventana, width = 4)
EM8.insert(tk.END, '0')
EM8.place(x = 185, y = 210)

EM9 = tk.Entry (ventana, width = 4)
EM9.insert(tk.END, '0')
EM9.place(x = 185, y = 235)

EM10 = tk.Entry (ventana, width = 4)
EM10.insert(tk.END, '0')
EM10.place(x = 185, y = 260)

EM11 = tk.Entry (ventana, width = 4)
EM11.insert(tk.END, '0')
EM11.place(x = 185, y = 285)

EM12 = tk.Entry (ventana, width = 4)
EM12.insert(tk.END, '0')
EM12.place(x = 185, y = 310)

# Entrys "Temp Maxima"

EMM1 = tk.Entry (ventana, width = 4)
EMM1.insert(tk.END, '0')
EMM1.place(x = 305, y = 35)

EMM2 = tk.Entry (ventana, width = 4)
EMM2.insert(tk.END, '0')
EMM2.place(x = 305, y = 60)

EMM3 = tk.Entry (ventana, width = 4)
EMM3.insert(tk.END, '0')
EMM3.place(x = 305, y = 85)

EMM4 = tk.Entry (ventana, width = 4)
EMM4.insert(tk.END, '0')
EMM4.place(x = 305, y = 110)

EMM5 = tk.Entry (ventana, width = 4)
EMM5.insert(tk.END, '0')
EMM5.place(x = 305, y = 135)

EMM6 = tk.Entry (ventana, width = 4)
EMM6.insert(tk.END, '0')
EMM6.place(x = 305, y = 160)

EMM7 = tk.Entry (ventana, width = 4)
EMM7.insert(tk.END, '0')
EMM7.place(x = 305, y = 185)

EMM8 = tk.Entry (ventana, width = 4)
EMM8.insert(tk.END, '0')
EMM8.place(x = 305, y = 210)

EMM9 = tk.Entry (ventana, width = 4)
EMM9.insert(tk.END, '0')
EMM9.place(x = 305, y = 235)

EMM10 = tk.Entry (ventana, width = 4)
EMM10.insert(tk.END, '0')
EMM10.place(x = 305, y = 260)

EMM11 = tk.Entry (ventana, width = 4)
EMM11.insert(tk.END, '0')
EMM11.place(x = 305, y = 285)

EMM12 = tk.Entry (ventana, width = 4)
EMM12.insert(tk.END, '0')
EMM12.place(x = 305, y = 310)

# Entrys "Precipitaciones"

EP1 = tk.Entry (ventana, width = 4)
EP1.insert(tk.END, '0')
EP1.place(x = 425, y = 35)

EP2 = tk.Entry (ventana, width = 4)
EP2.insert(tk.END, '0')
EP2.place(x = 425, y = 60)

EP3 = tk.Entry (ventana, width = 4) 
EP3.insert(tk.END, '0')
EP3.place(x = 425, y = 85)

EP4 = tk.Entry (ventana, width = 4)
EP4.insert(tk.END, '0')
EP4.place(x = 425, y = 110)

EP5 = tk.Entry (ventana, width = 4)
EP5.insert(tk.END, '0')
EP5.place(x = 425, y = 135)

EP6 = tk.Entry (ventana, width = 4)
EP6.insert(tk.END, '0')
EP6.place(x = 425, y = 160)

EP7 = tk.Entry (ventana, width = 4)
EP7.insert(tk.END, '0')
EP7.place(x = 425, y = 185)

EP8 = tk.Entry (ventana, width = 4)
EP8.insert(tk.END, '0')
EP8.place(x = 425, y = 210)

EP9 = tk.Entry (ventana, width = 4)
EP9.insert(tk.END, '0')
EP9.place(x = 425, y = 235)

EP10 = tk.Entry (ventana, width = 4)
EP10.insert(tk.END, '0')
EP10.place(x = 425, y = 260)

EP11 = tk.Entry (ventana, width = 4)
EP11.insert(tk.END, '0')
EP11.place(x = 425, y = 285)

EP12 = tk.Entry (ventana, width = 4)
EP12.insert(tk.END, '0')
EP12.place(x = 425, y = 310)

# Entrys Limites

EL1 = tk.Entry (ventana, width = 4)
EL1.insert(tk.END, '50')
EL1.place(x = 495, y = 365)

EL102 = tk.Entry (ventana, width = 4)
EL102.insert(tk.END, '0')
EL102.place(x = 495, y = 335)

EL2 = tk.Entry (ventana, width = 4)
EL2.insert(tk.END, '150')
EL2.place(x = 640, y = 365)

# Entry Titulo

ET1 = tk.Entry (ventana)
ET1.insert(tk.END, 'Climatograma')
ET1.place(x = 640, y = 10)

# Final de los entrys (por fin)

# Buttons

B1 = tk.Button(ventana, text = "Graficar", command = buttonGraficar)
B1.place (x = 160, y = 365)

B2 = tk.Button(ventana, text = textoButtonTemp.get(), command = buttonTemp)
B2.place (x = 355, y = 365)

B3 = tk.Button(ventana, text = textoButtonCuadro.get(), command = buttonCuadro)
B3.place (x = 355, y = 335)

ventana.mainloop()