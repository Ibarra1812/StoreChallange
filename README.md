# Análisis de Tiendas - Challenge Data Science Alura Latam

Este repositorio contiene el análisis de datos de ventas de cuatro tiendas, realizado como parte del Challenge 1 de Data Science de Alura Latam. El objetivo principal es analizar y comparar el rendimiento de cada tienda para proveer una recomendación de negocio sobre cuál plataforma es la mejor para vender productos.

El análisis se centra en métricas clave como ingresos, popularidad de categorías, satisfacción del cliente y costos de envío.

## Dependencias y Bibliotecas

Este proyecto fue desarrollado en un entorno de Google Colab. Las bibliotecas esenciales para ejecutar el análisis son:

* **pandas:** Para la carga, manipulación y análisis de los datos.
* **matplotlib:** Utilizada (a través de la función `.plot()` de pandas) para la generación de todas las visualizaciones.

## Cómo Ejecutar el Proyecto

El archivo `storealuraentrega.py` es una exportación directa de un notebook de Google Colab (`.ipynb`).

La forma recomendada de replicar este análisis es en un entorno de notebook (como Google Colab o Jupyter Notebook):

1.  Abra un nuevo notebook.
2.  Asegúrese de tener instaladas las bibliotecas `pandas` y `matplotlib`.
3.  Ejecute el código en el orden presentado en el archivo, celda por celda, ya que los análisis posteriores dependen de las variables creadas en los pasos anteriores (especialmente el DataFrame `df_total`).

## Fuente de Datos

Los datos no están incluidos en este repositorio. Se cargan directamente desde el repositorio de GitHub de Alura Latam en tiempo de ejecución.

* **Tienda 1:** `https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv`
* **Tienda 2:** `https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv`
* **Tienda 3:** `https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv`
* **Tienda 4:** `https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv`

## Metodología y Análisis Realizados

El análisis sigue una estructura secuencial para construir una recomendación final.

### 1. Preparación de Datos
Carga de los cuatro archivos CSV en DataFrames de Pandas. Se consolidan en un único DataFrame (`df_total`) y se añade una columna `Tienda` para permitir la segmentación y agrupación.

### 2. Análisis de Rendimiento
Se calculan y visualizan las siguientes métricas para cada tienda:

* **Ingresos Totales:** (Ejercicio 1) Suma de la columna `Precio` para determinar qué tienda tiene el mayor volumen de mercado.
* **Ventas por Categoría:** (Ejercicio 2) Conteo de ventas por `Categoría del Producto` y `Tienda`.
* **Valoración Media:** (Ejercicio 3) Promedio de la columna `Calificación` para medir la satisfacción del cliente.
* **Productos Más y Menos Vendidos:** (Ejercicio 4) Conteo de ventas por `Producto` y `Tienda` para identificar productos estrella y de baja rotación.
* **Costo de Envío Promedio:** (Ejercicio 5) Promedio de la columna `Costo de envío` para evaluar el costo logístico para el cliente.

### 3. Visualización de Datos
Se generan tres gráficos principales para resumir los hallazgos:
1.  **Gráfico de Barras (Ingresos Totales):** Comparación directa de la facturación.
2.  **Gráfico Circular (Top 5 Categorías):** Proporción del mercado de las categorías más vendidas.
3.  **Gráfico de Dispersión (Precio vs. Envío):** Análisis de la correlación entre el precio del producto y el costo de envío.

### 4. Análisis Geográfico (Extra)
Se utiliza un gráfico de dispersión (scatterplot) con las columnas `lat` y `lon` para visualizar la concentración de ventas geográficamente. Se combina con un análisis de la columna `Lugar de Compra` para identificar las ciudades con mayor volumen de ventas (Bogotá y Medellín).

## Conclusión del Análisis (Recomendación)

Basado en el análisis de los datos, la recomendación es **vender en la Tienda 1**.

**Justificación:**
* **Ingresos:** La Tienda 1 es la líder indiscutible en ingresos totales ($1,150,880,000), lo que indica que posee el mayor volumen de mercado y la base de clientes más grande.
* **Métricas Secundarias:** Aunque la Tienda 1 tiene el costo de envío promedio más alto y su valoración media no es la mejor (todas las tiendas están virtualmente empatadas cerca de 4.0 estrellas), su dominancia en el volumen de mercado sugiere que los clientes están dispuestos a pagar el costo de envío más alto.
* **Geografía:** El análisis geográfico demostró que las cuatro tiendas compiten exactamente en las mismas regiones (principalmente Bogotá y Medellín). Dado que todas operan en el mismo mercado, la mejor opción es la que ha logrado capturar la mayor parte de ese mercado.
