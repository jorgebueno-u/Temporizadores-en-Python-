import tkinter as tk
from tkinter import ttk

from documento import Documento
from cola_impresora import ColaImpresora
from tarea import Tarea
from pila_robot import PilaRobot

# Instancias de estructuras
cola = ColaImpresora()
pila = PilaRobot()

# Estado de ejecucion
imprimiendo = False
doc_actual = None
pag_actual = 0

ejecutando_robot = False
tarea_actual = None

# --- Metodos Cola (Impresora) ---
def agregar_doc():
    nom = entry_doc_nom.get()
    pag = entry_doc_pag.get()
    tmp = entry_doc_tmp.get()
    if nom and pag and tmp:
        doc = Documento(nom, pag, tmp)
        cola.encolar(doc)
        area_doc.insert("end", f"Encolado: {doc.nombre} ({doc.paginas} pag, {doc.tiempo}s/pag)\n")

def iniciar_impresion():
    global imprimiendo
    if not imprimiendo:
        imprimiendo = True
        area_doc.insert("end", "Inicio de impresion.\n")
        procesar_cola()

def detener_impresion():
    global imprimiendo
    imprimiendo = False
    lbl_estado_doc.config(text="Estado:\nDetenido", bg="pink")
    area_doc.insert("end", "Impresion detenida.\n")

def procesar_cola():
    global imprimiendo, doc_actual, pag_actual
    if not imprimiendo:
        return

    if doc_actual is None:
        if not cola.esta_vacia():
            doc_actual = cola.desencolar()
            pag_actual = 1
            area_doc.insert("end", f"Imprimiendo {doc_actual.nombre}...\n")
        else:
            lbl_estado_doc.config(text="Estado:\nSin documentos", bg="khaki")
            ventana.after(1000, procesar_cola)
            return

    if pag_actual <= doc_actual.paginas:
        lbl_estado_doc.config(
            text=f"Imprimiendo:\n{doc_actual.nombre}\nPag {pag_actual} de {doc_actual.paginas}",
            bg="LightGreen"
        )
        area_doc.insert("end", f"  -> {doc_actual.nombre}: Pagina {pag_actual}/{doc_actual.paginas}\n")
        pag_actual += 1
        ventana.after(int(doc_actual.tiempo * 1000), procesar_cola)
    else:
        area_doc.insert("end", f"Finalizado: {doc_actual.nombre}\n")
        doc_actual = None
        ventana.after(500, procesar_cola)

# --- Metodos Pila (Robot) ---
def agregar_tarea():
    nom = entry_tar_nom.get()
    tip = combo_tipo.get()
    tmp = entry_tar_tmp.get()
    if nom and tip and tmp:
        tar = Tarea(nom, tip, tmp)
        pila.apilar(tar)
        area_robot.insert("end", f"Apilado: [{tar.tipo}] {tar.nombre} ({tar.tiempo}s)\n")

def iniciar_robot():
    global ejecutando_robot
    if not ejecutando_robot:
        ejecutando_robot = True
        area_robot.insert("end", "Inicio procesador robot.\n")
        procesar_pila()

def detener_robot():
    global ejecutando_robot
    ejecutando_robot = False
    lbl_estado_robot.config(text="Estado:\nDetenido", bg="pink")
    area_robot.insert("end", "Robot detenido.\n")

def procesar_pila():
    global ejecutando_robot, tarea_actual
    if not ejecutando_robot:
        return

    if not pila.esta_vacia():
        tarea_actual = pila.desapilar()
        lbl_estado_robot.config(
            text=f"Ejecutando:\n{tarea_actual.nombre}\n[{tarea_actual.tipo}]",
            bg="LightGreen"
        )
        area_robot.insert("end", f"Procesando: {tarea_actual.nombre} ({tarea_actual.tiempo}s)...\n")
        ventana.after(int(tarea_actual.tiempo * 1000), finalizar_tarea)
    else:
        lbl_estado_robot.config(text="Estado:\nSin tareas", bg="khaki")
        ventana.after(1000, procesar_pila)

def finalizar_tarea():
    global tarea_actual
    if tarea_actual:
        area_robot.insert("end", f"Completado: {tarea_actual.nombre}\n")
        tarea_actual = None
    if ejecutando_robot:
        procesar_pila()

# --- Interfaz Grafica ---
ventana = tk.Tk()
ventana.title("Laboratorio 3")
ventana.geometry("600x380")
ventana.configure(bg="tan1")

notebook = ttk.Notebook(ventana)
notebook.place(x=10, y=10, width=580, height=360)

tab1 = tk.Frame(notebook, bg="bisque2")
tab2 = tk.Frame(notebook, bg="lightblue2")

notebook.add(tab1, text="7.1 Impresora (Cola)")
notebook.add(tab2, text="7.2 Robot (Pila)")

# Tab 1: Impresora
tk.Label(tab1, text="Nombre Doc:", bg="bisque2").place(x=10, y=10)
entry_doc_nom = tk.Entry(tab1)
entry_doc_nom.insert(0, "Doc1")
entry_doc_nom.place(x=10, y=30, width=90)

tk.Label(tab1, text="Nº Paginas:", bg="bisque2").place(x=10, y=60)
entry_doc_pag = tk.Entry(tab1)
entry_doc_pag.insert(0, "3")
entry_doc_pag.place(x=10, y=80, width=90)

tk.Label(tab1, text="Tiempo/Pag (s):", bg="bisque2").place(x=10, y=110)
entry_doc_tmp = tk.Entry(tab1)
entry_doc_tmp.insert(0, "1.0")
entry_doc_tmp.place(x=10, y=130, width=90)

btn_add_doc = tk.Button(tab1, text="Agregar Doc", command=agregar_doc)
btn_add_doc.place(x=10, y=170, width=90, height=30)

area_doc = tk.Text(tab1)
area_doc.place(x=110, y=20, width=290, height=230)

lbl_estado_doc = tk.Label(tab1, text="Estado:\nEsperando", bg="bisque4")
lbl_estado_doc.place(x=410, y=20, width=150, height=120)

btn_ini_doc = tk.Button(tab1, text="Iniciar", command=iniciar_impresion)
btn_ini_doc.place(x=110, y=260, width=130, height=30)

btn_det_doc = tk.Button(tab1, text="Detener", command=detener_impresion)
btn_det_doc.place(x=270, y=260, width=130, height=30)

# Tab 2: Robot
tk.Label(tab2, text="Nombre Tarea:", bg="lightblue2").place(x=10, y=10)
entry_tar_nom = tk.Entry(tab2)
entry_tar_nom.insert(0, "Sensor1")
entry_tar_nom.place(x=10, y=30, width=90)

tk.Label(tab2, text="Tipo Tarea:", bg="lightblue2").place(x=10, y=60)
combo_tipo = ttk.Combobox(tab2, values=["Sensores (ts)", "Movimiento (tm)"])
combo_tipo.current(0)
combo_tipo.place(x=10, y=80, width=90)

tk.Label(tab2, text="Tiempo (s):", bg="lightblue2").place(x=10, y=110)
entry_tar_tmp = tk.Entry(tab2)
entry_tar_tmp.insert(0, "2.0")
entry_tar_tmp.place(x=10, y=130, width=90)

btn_add_tar = tk.Button(tab2, text="Apilar Tarea", command=agregar_tarea)
btn_add_tar.place(x=10, y=170, width=90, height=30)

area_robot = tk.Text(tab2)
area_robot.place(x=110, y=20, width=290, height=230)

lbl_estado_robot = tk.Label(tab2, text="Estado:\nEsperando", bg="bisque4")
lbl_estado_robot.place(x=410, y=20, width=150, height=120)

btn_ini_tar = tk.Button(tab2, text="Iniciar", command=iniciar_robot)
btn_ini_tar.place(x=110, y=260, width=130, height=30)

btn_det_tar = tk.Button(tab2, text="Detener", command=detener_robot)
btn_det_tar.place(x=270, y=260, width=130, height=30)

ventana.mainloop()