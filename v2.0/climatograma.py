from tkinter.constants import LEFT, W
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import numpy as np

MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

WINDOW_DIM = "850x400"

ENTRIES = {}
VALUES = {}

def make_label(window, text, x, y):
    l = tk.Label(window, text=text)
    l.place(x=x, y=y)

def make_varlabel(window, text, x, y):
    l = tk.Label(window, textvariable=text, justify=LEFT)
    l.place(x=x, y=y)

def make_field(window, x, y, width, hint="", label=()):
    if label:
        l = tk.Label(window, text=label[0])
        l.place(x=label[1], y=label[2])
    f = tk.Entry(window, width=width)
    f.insert(tk.END, hint)
    f.place(x=x, y=y)
    return f

def make_button(window, x, y, text, command):
    b = tk.Button(window, text=text, command=command)
    b.place(x=x, y=y)

def make_switch(window, x, y, label=()):
    if label:
        l = tk.Label (window, text=label[0])
        l.place(x=label[1], y=label[2])
    v = tk.BooleanVar(value=False) 
    t = tk.StringVar(value="Off")
    def p():
        v.set(not v.get())
        t.set("On" if v.get() else "Off")
    b = tk.Button(window, textvariable=t, command=p)
    b.place(x=x, y=y)
    return v

def make_window():
    window = tk.Tk()
    window.geometry(WINDOW_DIM)
    window.title("Climatogramas por M.S.")

    # TABLA DE ENTRADAS
    (x, y, width, height, rows) = (25, 10, 100, 25, 12)
    headers, entries = ["Temp media", "Temp mínima", "Temp máxima", "Precipitaciones"], []
    make_label(window, "Mes", x, y)
    for i in range(12):
        make_label(window, MESES[i], x, y+height*(i+1))
    for i, h in enumerate(headers):
        column = []
        l = tk.Label(window, text=h)
        l.place(x=x+width*(i+1), y=y)
        for r in range(rows):
            e = make_field(window, x+width*(i+1), y+height*(r+1), 4, hint="0")
            column.append(e)
        entries.append(column)

    # INTERFAZ
    make_label(window, "Por Marcos Strauss", 10, 370)
    nf = make_field(window, 640, 10, 20, hint="Climatograma", label=("Nombre:", 575, 10))
    af = make_field(window, 640, 35, 20, hint="Anónimo", label=("Autor:", 575, 35))
    tmlf = make_field(window, 520, 335, 4, hint="0", label=("Lím. mín. temp (°C):", 400, 335))
    tMlf = make_field(window, 520, 365, 4, hint="150", label=("Lím. máx. temp (°C):", 400, 365))
    plf = make_field(window, 670, 365, 4, hint="300", label=("Lím. prec. (mm):", 570, 365))
    cbv = make_switch(window, 355, 335, ("Cuadro:", 300, 335))
    tbv = make_switch(window, 355, 365, ("Temp máx y mín:", 245, 365))
    make_button(window, 160, 365, "Graficar", run)
    ant = tk.StringVar(value="Análisis")
    make_varlabel(window, ant, 500, 70)
    
    dict = {
        "nf": nf, "af": af,
        "tf": entries[0], "mintf": entries[1], "maxtf": entries[2], "pf": entries[3],
        "tmlf": tmlf, "tMlf": tMlf, "plf": plf,
        "cbv": cbv, "tbv": tbv, "ant": ant}
    for k, v in dict.items():
        ENTRIES[k] = v

    window.mainloop()


def analyse():
    temp_prom = sum(VALUES["temps"]) / 12
    prec_anual = sum(VALUES["precs"])
    amp_term_anual = max(VALUES["temps"]) - min(VALUES["temps"])

    temp_class = ""
    if temp_prom <= 9:
        temp_class = "FRÍO"
    elif temp_prom <= 20:
        temp_class = "TEMPLADO"
    else:
        temp_class = "CÁLIDO"

    prec_class = ""
    if prec_anual <= 200:
        prec_class = "ÁRIDO"
    elif prec_anual <= 500:
        prec_class = "SEMIÁRIDO"
    elif prec_anual <= 1000:
        prec_class = "SEMIHÚMEDO"
    else:
        prec_class = "HÚMEDO"

    ENTRIES["ant"].set("El clima es " + str(temp_class) + " - " + str(prec_class) + "\n" +
        "así podés poner varias líneas sin tener que usar muchas labels\n\n" +
        "iupiiiii - amp term anual es " + str(amp_term_anual))

    # ESTO HABRÍA QUE CONTINUARLO


def graph(title, author, temps, min_temps, max_temps, precs, tml, tMl, pl, mym=True):
    months = range(1, 13)
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.set_xticks(months)
    ax1.set_ylim(0, pl)
    ax2.set_ylim(tml, tMl)
    ax1.yaxis.set_label_position("right")
    ax1.yaxis.tick_right()
    ax2.yaxis.set_label_position("left")
    ax2.yaxis.tick_left()
    ax1.spines["top"].set_visible(False)
    ax2.spines["top"].set_visible(False)
    ax2.plot(months, temps, label="Media", color="g")
    plt.scatter(months, temps, color="g")
    if ENTRIES["tbv"].get():
        ax2.plot(months, min_temps, label="Mínima", color="b")
        plt.scatter(months, min_temps, color="b")
        ax2.plot(months, max_temps, label="Máxima", color="r")
        plt.scatter(months, max_temps, color="r")
    ax1.bar(months, precs, label="Prec", color="pink", width=0.9)
    ax1.set_ylabel("Precipitación (mm)")
    ax2.set_ylabel("Temperatura (°C)")
    ax2.legend(loc = "upper left")
    plt.suptitle(title)
    plt.title("por " + author)
    plt.show()


def make_chart():
    chart_window = tk.Tk()
    chart_window.title("Cuadro de " + VALUES["title"])
    chart_window.geometry("960x200")

    chart = ttk.Treeview(chart_window)
    chart["columns"] = MESES
    chart.column("#0", width=150, minwidth=25)
    for m in MESES:
        chart.column(m, anchor=W, width=80)
    chart.heading("#0", text=" ", anchor=W)
    for m in MESES:
        chart.heading(m, text=m, anchor=W)
    chart.insert(parent="", index="end", iid="0",
        text="Temp promedio (°C)", values=VALUES["temps"])
    if ENTRIES["tbv"].get():
        chart.insert(parent="", index="end", iid="1",
            text="Temp mínima (°C)", values=VALUES["min_temps"])
        chart.insert(parent="", index="end", iid="2",
            text="Temp máxima (°C)", values=VALUES["max_temps"])
        amp_term = list(np.array(VALUES["max_temps"]) - np.array(VALUES["min_temps"]))
        chart.insert(parent="", index="end", iid="3",
            text="Amp térmica mensual (°C)", values=amp_term)
    chart.insert(parent="", index="end", iid="4", text="Precipitaciones (mm)", values=VALUES["precs"])
    chart.pack(pady=20)

    return chart


def run():
    dict = {
        "title": ENTRIES["nf"].get(), "author": ENTRIES["af"].get(),
        "temps": [float(f.get()) for f in ENTRIES["tf"]],
        "min_temps": [float(f.get()) for f in ENTRIES["mintf"]],
        "max_temps": [float(f.get()) for f in ENTRIES["maxtf"]],
        "precs": [float(f.get()) for f in ENTRIES["pf"]],
        "tml": float(ENTRIES["tmlf"].get()),
        "tMl": float(ENTRIES["tMlf"].get()),
        "pl": float(ENTRIES["plf"].get()) }
    for k, v in dict.items():
        VALUES[k] = v

    analyse()
    if ENTRIES["cbv"].get():
       aux = make_chart()
    graph(dict["title"], dict["author"], dict["temps"], dict["min_temps"], dict["max_temps"], dict["precs"], dict["tml"], dict["tMl"], dict["pl"])
    if ENTRIES["cbv"].get():
        aux.mainloop()


make_window()