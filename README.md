# Temporizadores en Python - Carrera Automovilística con GUI 🏎️⚡

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![UMNG](https://img.shields.io/badge/Universidad-UMNG-red.svg)](https://www.unimilitar.edu.co/)

Este repositorio contiene la solución desarrollada para la **Práctica de Laboratorio 4: Temporizadores en Python** de la asignatura **Programación 3** de la Universidad Militar Nueva Granada.

El objetivo principal es explorar el funcionamiento de los temporizadores en Python (tanto bloqueantes como no bloqueantes) e implementar una simulación gráfica e interactiva de una competencia automovilística.

---

## 🚀 Características Principales

- **Simulación Gráfica Interactiva:** Desarrollada con `tkinter` / `PyQt`.
- **10 Temporizadores Independientes:** Cada vehículo cuenta con su propio `Timer` o subproceso independiente para controlar su desplazamiento.
- **Velocidad Dinámica y Aleatoria:** Cada vehículo cambia su velocidad aleatoriamente al rebotar en los extremos de la pista (idas y vueltas).
- **Sistema de Apuestas:** El usuario puede seleccionar su vehículo favorito antes de iniciar la carrera y recibir un anuncio del resultado.
- **Configuración de Rondas:** Permite definir el número de idas y vueltas (laps/rondas) a ejecutar.
- **Control Global de Tiempo (Slider):** Ajuste en tiempo real de la velocidad general de la simulación mediante un control deslizante.
- **Tabla de Resultados:** Al finalizar, se muestra una tabla ordenada del menor al mayor tiempo registrado (ganador en primer lugar).
- **Reinicios Sin Cierre:** Posibilidad de reiniciar la competencia con un clic sin necesidad de cerrar la ventana principal.

---

## 🛠️ Tecnologías y Requisitos

- **Lenguaje:** Python 3.13.5 (o superior).
- **IDE Recomendado:** Microsoft Visual Studio Code.
- **Librerías Utilizadas:**
  - `tkinter` / `PyQt` (Interfaz Gráfica)
  - `threading` / `time` (Manejo de tiempos y subprocesos)
  - `random` (Ajustes aleatorios de velocidad)
  - `Pillow` (Opcional para carga y redimensión de imágenes de vehículos)

---

## 📂 Estructura del Repositorio

```text
.
├── assets/                  # Imágenes de los vehículos y elementos gráficos
├── src/
│   ├── cronometro.py        # Clase Cronometro basada en time.time()
│   ├── temporizadores.py    # Ejemplos con time.sleep() y threading.Timer
│   └── carrera_gui.py       # Aplicación principal de la carrera automovilística
├── README.md                # Descripción del proyecto
└── LICENSE                  # Licencia de uso
