# PIA_CE-IABD_Practice

![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)&nbsp;![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-d00000?style=for-the-badge&logo=keras&logoColor=white)&nbsp;![TensorFlow](https://img.shields.io/badge/TensorFlow-TensorBoard-ff6f00?style=for-the-badge&logo=tensorflow&logoColor=white)&nbsp;![Pandas](https://img.shields.io/badge/Pandas%20%7C%20NumPy%20%7C%20Plotly-Análisis-150458?style=for-the-badge&logo=pandas&logoColor=white)&nbsp;![OOP](https://img.shields.io/badge/POO-Python-22c55e?style=for-the-badge)&nbsp;![IES Augustobriga](https://img.shields.io/badge/IES%20Augustobriga-CE%20IABD-6366f1?style=for-the-badge)

> **PIA_CE-IABD_Practice** recoge los ejercicios y proyectos de la asignatura **Programación de Inteligencia Artificial** del _Curso de Especialización en Inteligencia Artificial y Big Data_ del **IES Augustóbriga**. Se trabaja desde los fundamentos de **Python** hasta la programación de **redes neuronales profundas** con Keras y TensorBoard, pasando por POO, librerías de análisis de datos y manejo de ficheros.

---

## 📚 Asignatura

| | |
|---|---|
| **Centro** | IES Augustóbriga |
| **Curso** | C.E. Inteligencia Artificial y Big Data |
| **Asignatura** | Programación de Inteligencia Artificial |
| **Lenguaje principal** | Python 3.10+ |
| **Tecnologías** | Keras, TensorFlow, TensorBoard, Pandas, NumPy, Matplotlib, Plotly, SQLite |

---

## 🗂️ Temario

### 🐍 Tema 01 · Introducción a Python

Primeros pasos con Python: sintaxis básica, entrada/salida, funciones numéricas, operaciones con strings y estructuras de control de flujo.

- Tipos de datos primitivos: `int`, `float`, `bool`, `str`.
- Funciones numéricas integradas: `abs()`, `round()`, `pow()`, `divmod()`.
- Manipulación de cadenas: slicing, métodos, f-strings.
- Control de flujo: `if/elif/else`, `while`, `for`, `break`, `continue`.
- Bucles `for` especiales: `enumerate()`, `zip()`, `range()`.

### 💾 Tema 02 · Estructuras de Datos

Estudio profundo de las estructuras de datos nativas de Python y sus operaciones.

- **Listas** — indexación, slicing, métodos de lista.
- **Tuplas** — inmutabilidad, desempaquetado, uso como claves.
- **Diccionarios** — pares clave-valor, recorrido y métodos.
- **Sets** — conjuntos, operaciones de unión, intersección y diferencia.
- **Arrays** — módulo `array` y comparativa con listas.
- **Comprensiones** — list, dict y set comprehensions para código conciso.

### ⚙️ Tema 03 · Funciones Avanzadas, Ficheros y SQLite

Programación funcional avanzada y persistencia de datos.

- **Funciones** — argumentos por defecto, `*args`, `**kwargs`, funciones lambda.
- **Funciones decoradoras** — patrón decorador, `@wraps`, casos de uso reales.
- **Ficheros** — lectura y escritura de ficheros de texto, CSV y JSON.
- **SQLite** — creación de bases de datos, consultas SQL desde Python con `sqlite3`.

### 📊 Tema 04 · Librerías de Análisis de Datos

Herramientas esenciales del ecosistema científico de Python.

- **NumPy** — arrays multidimensionales, álgebra lineal y operaciones vectorizadas.
- **Pandas** — DataFrames, series, limpieza, agrupación y análisis de datasets.
- **Matplotlib** — visualización estática: gráficos de línea, barras, histogramas.
- **Plotly** — gráficos interactivos y dashboards dinámicos.

### 🧩 Tema 05 · POO en Python

Programación Orientada a Objetos aplicada a Python.

- Clases, objetos, atributos y métodos.
- Constructores `__init__` y métodos mágicos (`__str__`, `__repr__`, `__len__`).
- Herencia simple y múltiple, polimorfismo y encapsulación.
- Clases abstractas con `ABC` y el módulo `dataclasses`.

### 🧠 Tema 06 · Redes Neuronales Profundas

Programación de Deep Learning con Keras y seguimiento con TensorBoard.

- Construcción de redes neuronales con la API secuencial de **Keras**.
- Capas densas, funciones de activación (`ReLU`, `Sigmoid`, `Softmax`).
- Compilación del modelo: optimizadores (`Adam`, `SGD`), funciones de pérdida y métricas.
- Entrenamiento, validación y evaluación del modelo.
- Visualización del entrenamiento con **TensorBoard**: curvas de pérdida y precisión.

---

## 🏗️ Estructura del Proyecto

```txt
PIA_CE-IABD_Practice/
├── Tema_01/
│   └── Tareas/        # Introducción a Python
├── Tema_02/
│   └── Tareas/        # Estructuras de datos
├── Tema_03/
│   └── Tareas/        # Funciones avanzadas, ficheros y SQLite
├── Tema_04/
│   └── Tareas/        # Librerías: Pandas, NumPy, Matplotlib, Plotly
├── Tema_05/
│   └── Tareas/        # POO en Python
├── Tema_06/
│   └── Tareas/        # Redes neuronales profundas con Keras y TensorBoard
└── README.md
```

---

## ⚙️ Requisitos y Ejecución

Clonar el repositorio:
```bash
git clone https://github.com/sorgazb/PIA_CE-IABD_Practice.git
cd PIA_CE-IABD_Practice
```

Instalar dependencias:
```bash
pip install numpy pandas matplotlib plotly keras tensorflow
```

Ejecutar cualquier script:
```bash
python Tema_01/Tareas/ejercicio.py
```

Lanzar TensorBoard (Tema 06):
```bash
tensorboard --logdir=Tema_06/logs
```

---

## 🤝 Contribución

Haz fork del repositorio.

Crea una rama de trabajo:
```bash
git checkout -b feature/mi-nueva-practica
```

Realiza tus cambios y haz commit.

Abre un Pull Request describiendo tus mejoras.

---

<p align="center">
  C.E. Inteligencia Artificial y Big Data &nbsp;·&nbsp; Programación de Inteligencia Artificial &nbsp;·&nbsp; IES Augustóbriga &nbsp;·&nbsp; Sergio Orgaz Bravo
</p>
