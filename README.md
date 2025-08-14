# Procesamiento avanzado de datos con Python

## Descripción

EL OBJETIVO DE LA PRÁCTICA ES QUE EL ESTUDIANTE ADQUIERA HABILIDADES AVANZADAS
DE PROCESAMIENTO DE DATOS DE HOJAS DE CÁLCULO, MEDIANTE LA PROGRAMACIÓN DE
SCRIPTS AUTOMATIZADOS ESCRITOS EN LENGUAJE DE PROGRAMACIÓN PYTHON.

## Pasos

1. Configurar repositorio y dependencias:

   - Crear un archivo `.gitignore` para excluir archivos innecesarios.
   - Crear un archivo `requirements.txt` y agregar las dependencias del
     proyecto.
   - Crear un archivo `README.md` para documentar el proyecto.
   - Crear un archivo `main.py` como punto de entrada del script.
   - Crear una carpeta `datos` y copiar el archivo `datos_base.xlsx`
     proporcionado en la práctica.

2. Crear un entorno virtual:

   - Crear un entorno virtual con `python -m venv venv`.
   - Activar el entorno virtual:
     - En Windows: `venv\Scripts\activate`
     - En macOS/Linux: `source venv/bin/activate`
   - Instalar las dependencias del proyecto con
     `pip install -r requirements.txt`.

3. Desarrollar el script `main.py`:

   - Importar las librerías necesarias: `pandas`, `matplotlib`.
   - Cargar el archivo `datos_base.xlsx` utilizando `pandas` iterando sobre las
     hojas de cálculo.
   - Generar un gráfico de barras utilizando `matplotlib` para visualizar los
     datos con las columnas de `Detalle` y `Valor`.
   - Generar un gráfico de pastel utilizando `matplotlib` para visualizar los
     datos con las columnas de `Detalle` y `Porcentaje`.
   - Guardar los gráficos generados en la carpeta `generados` con nombres
     descriptivos.

4. Ejecutar el script:
   - Ejecutar el script `main.py` para procesar los datos y generar los
     gráficos.
   - Verificar que los gráficos se hayan guardado correctamente en la carpeta
     `generados`.
