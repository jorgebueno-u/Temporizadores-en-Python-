Simulador de Estructuras de Datos Dinámicas (Pilas y Colas)
Este proyecto es una aplicación de escritorio desarrollada en Python con Tkinter que simula el comportamiento de dos estructuras de datos dinámicas fundamentales: Colas (FIFO) y Pilas (LIFO).
La aplicación fue desarrollada como parte de la práctica de laboratorio de la asignatura Programación 3 de la Universidad Militar Nueva Granada.
📸 Módulos del Proyecto
La aplicación se compone de dos herramientas interactivas integradas en una interfaz con pestañas (ttk.Notebook):
1. Simulador de Controlador de Impresión (Cola / FIFO)
Concepto: First-In, First-Out (El primero en entrar es el primero en salir).
Descripción: Simula la cola de spooler de una impresora. Los documentos ingresados se agregan al final de la cola. Al iniciar el proceso, se atienden e imprimen estrictamente en el orden en que llegaron, procesando página por página en tiempo real.
Atributos del Documento: Nombre, número de páginas y tiempo de impresión por página.
2. Simulador de Procesador de Robot Explorador (Pila / LIFO)
Concepto: Last-In, First-Out (El último en entrar es el primero en salir).
Descripción: Simula el procesador de tareas de un robot explorador (tareas de sensores y movimiento). A medida que se agregan tareas, se apilan. Al iniciar la ejecución, el procesador desapila y ejecuta siempre la última tarea ingresada (la cima de la pila).
Atributos de la Tarea: Nombre de la tarea, tipo (Sensores o Movimiento) y tiempo de ejecución.
🛠️ Estructura del Código
El proyecto sigue los principios de la Programación Orientada a Objetos (POO) y la separación de responsabilidades en módulos independientes:
├── cola_impresora.py    # Clase ColaImpresora (Estructura de datos FIFO)
├── documento.py         # Clase Documento (Modelo de datos para la cola)
├── pila_robot.py        # Clase PilaRobot (Estructura de datos LIFO)
├── tarea.py             # Clase Tarea (Modelo de datos para la pila)
├── main.py              # Interfaz Gráfica de Usuario (Tkinter) y lógica de eventos
└── README.md            # Documentación del proyecto

🚀 Requisitos e InstalaciónRequisitos previos
Python 3.8 o superior instalado en el sistema.
Tkinter (incluido por defecto en las instalaciones estándar de Python para Windows y macOS).
Pasos para ejecutar
Clonar el repositorio:
git clone https://github.com/tu-usuario/simulador-estructuras-datos.git
cd simulador-estructuras-datos

Ejecutar la aplicación:
python main.py

🧪 Demostración de Uso
Prueba de Cola (Impresora):
Agrega varios documentos (ej. Doc1 con 3 páginas, Doc2 con 2 páginas).
Oprime el botón Iniciar. Verás cómo procesa Doc1 página por página antes de continuar con Doc2.
Prueba de Pila (Robot):
Apila múltiples tareas (ej. Sensor1, Movimiento1, Sensor2).
Oprime Iniciar. Observa cómo la primera tarea en ejecutarse es la última que agregaste (Sensor2).
Si apilas una nueva tarea mientras el robot trabaja, esta se ejecutará inmediatamente después de finalizar la tarea actual.
📜 Licencia
Este proyecto fue desarrollado con fines educativos para la práctica universitaria de Programación 3 (Ingeniería Mecatrónica - UMNG).
