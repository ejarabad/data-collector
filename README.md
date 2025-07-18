# Proyecto ETL: Colector y Procesador de Datos de Redes Sociales (Simulado)

Este proyecto demuestra un pipeline básico de Extracción, Transformación y Carga (ETL) utilizando Python. Simula la recolección de datos de publicaciones de redes sociales, su limpieza y transformación, y finalmente su carga en una base de datos SQLite para su posterior análisis.

## 🚀 Habilidades Demostradas

* **Ingeniería de Datos:** Diseño e implementación de un pipeline ETL.
* **Python:** Uso de librerías clave para manipulación de datos y operaciones de sistema.
* **Extracción (Extract):** Obtención de datos de fuentes externas (simulado vía API REST).
* **Transformación (Transform):** Limpieza, normalización, renombrado de columnas y creación de nuevas características (Feature Engineering).
* **Carga (Load):** Persistencia de datos limpios en una base de datos relacional (SQLite).
* **Manejo de Archivos:** Lectura y escritura de formatos CSV y JSON.
* **Bases de Datos:** Interacción básica con bases de datos SQL.

## 🛠️ Tecnologías Utilizadas

* **Python 3.x**
* **Pandas:** Para manipulación y análisis de datos.
* **Requests:** Para realizar peticiones HTTP (extracción de datos).
* **SQLite3:** Base de datos ligera y embebida para la capa de carga.
* **Git & GitHub:** Control de versiones y alojamiento del repositorio.

## 📂 Estructura del Proyecto
data_collector/
├── collect_data.py       # Script para la Extracción de datos crudos.
├── transform_data.py     # Script para la Transformación y limpieza de datos.
├── load_data.py          # Script para la Carga de datos limpios a la base de datos.
├── requirements.txt      # Lista de dependencias de Python del proyecto.
├── .gitignore            # Archivo para ignorar archivos y carpetas en Git.
├── raw_data/             # Contiene los datos extraídos en su formato original.
│   └── social_media__data.csv
│   └── social_media_data.json
├── cleaned_data/         # Contiene los datos después de la fase de transformación.
│   └── clean_social_media_data.csv
└── database/             # Contiene el archivo de la base de datos SQLite.
└── social_media_data.db

## ⚙️ Cómo Ejecutar el Proyecto

Sigue estos pasos para ejecutar el pipeline ETL completo en tu máquina local:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TuUsuario/data_engineer_project_jr.git](https://github.com/TuUsuario/data_engineer_project_jr.git)
    cd data_engineer_project_jr
    ```
    *(Nota: Reemplaza `TuUsuario` y `data_engineer_project_jr` con tu información real de GitHub después de crear el repositorio.)*

2.  **Crear y activar el entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar el pipeline ETL en secuencia:**
    ```bash
    python collect_data.py
    python transform_data.py
    python load_data.py
    ```
    *(Opcional: Puedes ejecutar cada script individualmente para ver los resultados de cada fase.)*

## 📈 Resultados Esperados

Después de ejecutar los scripts, se generarán las siguientes carpetas y archivos:

* `raw_data/`: Contendrá `social_media_data.csv` y `social_media_data.json` con los datos tal como se extrajeron.
* `cleaned_data/`: Contendrá `clean_social_media_data.csv` con los datos limpios, renombrados y con la nueva columna `content_length`.
* `database/`: Contendrá `social_media_data.db`, el archivo de la base de datos SQLite con la tabla `posts` cargada con los datos limpios.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes sugerencias o mejoras, no dudes en abrir un *issue* o enviar un *pull request*.
