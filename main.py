import pandas as pd
from matplotlib import pyplot as plt

# Grafica de ejemplo
eje_x = ["A", "B", "C", "D", "E"]
eje_y = [2, 3, 5, 7, 11]
fig, ax = plt.subplots()
ax.bar(eje_x, eje_y, color="blue", label="Datos de ejemplo")
fig.savefig("generados/grafica_ejemplo.png", bbox_inches="tight")
plt.close(fig)  # Cerrar la figura para liberar memoria

# Leer archivo Excel
archivo_excel = "datos/datos_base.xlsx"
contador = 1
while contador <= 5:
    # codigo para leer el archivo Excel
    data_hoja = pd.read_excel(
        archivo_excel, sheet_name=f"Hoja{contador}", engine="openpyxl"
    )
    print(f"Datos leidos de la Hoja{contador}")
    # Graficar datos de la hoja
    eje_x = data_hoja.iloc[:, 0]  # Asumiendo que la primera columna es el eje X
    eje_y_barras = data_hoja.iloc[:, 1]  # Asumiendo que la segunda columna es el eje Y
    # Asumiendo que la tercera columna es el eje Y para el pastel
    eje_y_pastel = data_hoja.iloc[:, 2]
    # Crear la gráfica de barras
    fig, ax = plt.subplots()
    ax.bar(eje_x, eje_y_barras, color="green", label=f"Datos de Hoja {contador}")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_xticklabels(eje_x, rotation=45)
    ax.set_title(f"Gráfica de la Hoja {contador}")
    fig.savefig(f"generados/grafica_barras_hoja_{contador}.png", bbox_inches="tight")
    plt.close(fig)  # Cerrar la figura para liberar memoria
    # Crear la gráfica de pastel
    fig, ax = plt.subplots()
    ax.pie(
        eje_y_pastel,
        labels=eje_x,
    )
    ax.set_title(f"Gráfica de Pastel de la Hoja {contador}")
    fig.savefig(f"generados/grafica_pastel_hoja_{contador}.png", bbox_inches="tight")
    plt.close(fig)  # Cerrar la figura para liberar memoria
    # Incrementar el contador
    contador = contador + 1

print("Gráficas generadas y guardadas en la carpeta 'generados'.")
