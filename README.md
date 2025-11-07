# Alura Store - Challenge de Data Science

## 📊 Descripción del Proyecto

Este proyecto es un challenge de Alura enfocado en Data Science. El objetivo principal es ayudar a decidir qué tienda de la cadena **Alura Store** debe recibir mayor inversión y enfoque estratégico mediante el análisis de datos de ventas, rendimiento y reseñas de las 4 tiendas que componen la cadena.

## 🎯 Objetivos del Challenge

1. **Cargar y manipular datos CSV** utilizando la biblioteca Pandas
2. **Crear visualizaciones de datos** utilizando la biblioteca Matplotlib
3. **Analizar métricas clave** como:
   - Ingresos por tienda
   - Reseñas y calificaciones de clientes
   - Rendimiento de ventas
   - Tendencias temporales

## 🛠️ Tecnologías y Librerías

- **Python 3.8+**
- **Pandas**: Para carga, limpieza y manipulación de datos
- **Matplotlib**: Para creación de gráficos y visualizaciones
- **NumPy**: Para cálculos numéricos
- **Jupyter Notebook**: Para análisis interactivo (opcional)

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

1. **Clona este repositorio:**
```bash
git clone https://github.com/Ibarra1812/StoreChallange.git
cd StoreChallange
```

2. **Crea un entorno virtual (recomendado):**
```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
```

3. **Instala las dependencias:**
```bash
pip install pandas matplotlib numpy jupyter
```

O utiliza el archivo de requirements (si existe):
```bash
pip install -r requirements.txt
```

## 📁 Estructura del Proyecto

```
StoreChallange/
│
├── data/                      # Carpeta para archivos CSV
│   ├── ventas_tienda1.csv
│   ├── ventas_tienda2.csv
│   ├── ventas_tienda3.csv
│   ├── ventas_tienda4.csv
│   └── resenas.csv
│
├── notebooks/                 # Jupyter Notebooks con análisis
│   ├── 01_carga_datos.ipynb
│   ├── 02_analisis_exploratorio.ipynb
│   ├── 03_visualizaciones.ipynb
│   └── 04_conclusiones.ipynb
│
├── src/                       # Scripts de Python
│   ├── load_data.py          # Funciones para cargar datos
│   ├── analysis.py           # Funciones de análisis
│   └── visualization.py      # Funciones de visualización
│
├── results/                   # Gráficos y resultados generados
│   └── graficos/
│
├── README.md
└── requirements.txt
```

## 📊 Análisis de Datos con Pandas

### 1. Carga de Datos

```python
import pandas as pd

# Cargar datos de ventas de cada tienda
tienda1 = pd.read_csv('data/ventas_tienda1.csv')
tienda2 = pd.read_csv('data/ventas_tienda2.csv')
tienda3 = pd.read_csv('data/ventas_tienda3.csv')
tienda4 = pd.read_csv('data/ventas_tienda4.csv')

# Visualizar primeras filas
print(tienda1.head())
```

### 2. Manipulación de Datos

```python
# Combinar datos de todas las tiendas
tienda1['tienda'] = 'Tienda 1'
tienda2['tienda'] = 'Tienda 2'
tienda3['tienda'] = 'Tienda 3'
tienda4['tienda'] = 'Tienda 4'

datos_completos = pd.concat([tienda1, tienda2, tienda3, tienda4], ignore_index=True)

# Limpieza de datos
datos_completos = datos_completos.dropna()  # Eliminar valores nulos
datos_completos['fecha'] = pd.to_datetime(datos_completos['fecha'])  # Convertir fechas

# Análisis estadístico básico
print(datos_completos.describe())
```

### 3. Análisis de Métricas

```python
# Ingresos totales por tienda
ingresos_por_tienda = datos_completos.groupby('tienda')['ingresos'].sum()

# Promedio de reseñas por tienda
promedio_resenas = datos_completos.groupby('tienda')['calificacion'].mean()

# Número de ventas por tienda
ventas_por_tienda = datos_completos.groupby('tienda').size()

print(f"Ingresos por tienda:\n{ingresos_por_tienda}\n")
print(f"Promedio de calificaciones:\n{promedio_resenas}\n")
print(f"Número de ventas:\n{ventas_por_tienda}")
```

## 📈 Visualizaciones con Matplotlib

### 1. Gráfico de Barras - Ingresos por Tienda

```python
import matplotlib.pyplot as plt

# Configurar el estilo
plt.style.use('seaborn-v0_8')
plt.figure(figsize=(10, 6))

# Crear gráfico de barras
ingresos_por_tienda.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Ingresos Totales por Tienda', fontsize=16, fontweight='bold')
plt.xlabel('Tienda', fontsize=12)
plt.ylabel('Ingresos ($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('results/graficos/ingresos_por_tienda.png')
plt.show()
```

### 2. Gráfico de Líneas - Tendencia de Ventas

```python
# Ventas por mes
datos_completos['mes'] = datos_completos['fecha'].dt.to_period('M')
ventas_mensuales = datos_completos.groupby(['mes', 'tienda'])['ingresos'].sum().unstack()

plt.figure(figsize=(12, 6))
for tienda in ventas_mensuales.columns:
    plt.plot(ventas_mensuales.index.astype(str), ventas_mensuales[tienda], 
             marker='o', label=tienda, linewidth=2)

plt.title('Tendencia de Ventas Mensuales por Tienda', fontsize=16, fontweight='bold')
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Ingresos ($)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/graficos/tendencia_ventas.png')
plt.show()
```

### 3. Gráfico Circular - Distribución de Ventas

```python
plt.figure(figsize=(8, 8))
plt.pie(ventas_por_tienda, labels=ventas_por_tienda.index, autopct='%1.1f%%',
        startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Distribución de Ventas por Tienda', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('results/graficos/distribucion_ventas.png')
plt.show()
```

### 4. Gráfico de Dispersión - Reseñas vs Ingresos

```python
plt.figure(figsize=(10, 6))
for tienda in datos_completos['tienda'].unique():
    datos_tienda = datos_completos[datos_completos['tienda'] == tienda]
    plt.scatter(datos_tienda['calificacion'], datos_tienda['ingresos'], 
                label=tienda, alpha=0.6, s=50)

plt.title('Relación entre Calificaciones e Ingresos', fontsize=16, fontweight='bold')
plt.xlabel('Calificación', fontsize=12)
plt.ylabel('Ingresos ($)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('results/graficos/resenas_vs_ingresos.png')
plt.show()
```

## 📊 Métricas de Análisis

### Métricas Clave a Evaluar:

1. **Ingresos Totales**: Suma de todas las ventas por tienda
2. **Ticket Promedio**: Ingreso promedio por transacción
3. **Número de Transacciones**: Cantidad de ventas realizadas
4. **Calificación Promedio**: Promedio de reseñas de clientes
5. **Tasa de Crecimiento**: Variación de ventas mes a mes
6. **Rendimiento por Categoría**: Productos más vendidos por tienda

### Ejemplo de Cálculo de Métricas:

```python
# Calcular métricas por tienda
metricas = datos_completos.groupby('tienda').agg({
    'ingresos': ['sum', 'mean', 'count'],
    'calificacion': 'mean'
}).round(2)

metricas.columns = ['Ingresos Totales', 'Ticket Promedio', 'Num. Transacciones', 'Calificación Promedio']
print(metricas)

# Identificar la tienda con mejor rendimiento
mejor_tienda = metricas['Ingresos Totales'].idxmax()
print(f"\nLa tienda con mejor rendimiento es: {mejor_tienda}")
```

## 💡 Conclusiones y Recomendaciones

Después del análisis, podrás responder preguntas como:

- ¿Qué tienda genera más ingresos?
- ¿Qué tienda tiene mejor satisfacción del cliente?
- ¿Hay correlación entre reseñas positivas y ventas?
- ¿Qué tienda merece mayor inversión?
- ¿Cuáles son las tendencias de crecimiento?

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agrega nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es parte del Challenge de Alura Latam.

## 👥 Autor

- **Tu Nombre** - [Ibarra1812](https://github.com/Ibarra1812)

## 🙏 Agradecimientos

- Alura Latam por proporcionar este challenge
- La comunidad de Data Science por sus recursos y apoyo

---

**¡Buena suerte con tu análisis! 🚀📊**