# StoreChallange

Proyecto de análisis de datos de ventas de tienda utilizando Pandas y Matplotlib.

## Descripción

Este proyecto implementa un sistema completo de análisis de datos que:
- Carga y manipula datos CSV con la biblioteca **Pandas**
- Crea visualizaciones de datos con la biblioteca **Matplotlib**
- Analiza métricas como ingresos, reseñas y rendimiento de ventas

## Características

### Análisis de Datos con Pandas
- Carga de datos CSV
- Manipulación y transformación de datos
- Agrupación y agregación de métricas
- Cálculo de estadísticas clave

### Visualizaciones con Matplotlib
- **Tendencia de ingresos**: Gráfico de línea mostrando ingresos diarios
- **Análisis por categoría**: Gráficos de barras y pastel mostrando distribución de ingresos
- **Análisis de reseñas**: Calificaciones promedio y cantidad de reseñas por producto
- **Rendimiento de ventas**: Productos más vendidos y tendencias de unidades vendidas

### Métricas Analizadas
- Ingresos totales y por categoría
- Unidades vendidas totales y por categoría
- Calificación promedio de productos
- Total de reseñas de clientes
- Top 5 productos por ingresos

## Requisitos

- Python 3.8+
- Pandas 2.0.0+
- Matplotlib 3.7.0+

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/Ibarra1812/StoreChallange.git
cd StoreChallange
```

2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Ejecutar el script de análisis:
```bash
python store_analysis.py
```

El script:
1. Carga los datos desde `store_data.csv`
2. Calcula métricas clave
3. Muestra un resumen en la consola
4. Genera visualizaciones en la carpeta `visualizations/`

## Estructura del Proyecto

```
StoreChallange/
├── store_data.csv          # Datos de ventas de la tienda
├── store_analysis.py       # Script principal de análisis
├── requirements.txt        # Dependencias del proyecto
├── visualizations/         # Carpeta con gráficos generados
│   ├── revenue_trend.png
│   ├── category_analysis.png
│   ├── review_analysis.png
│   └── sales_performance.png
└── README.md              # Este archivo
```

## Datos de Ejemplo

El archivo `store_data.csv` contiene datos de ventas con las siguientes columnas:
- `date`: Fecha de la venta
- `product`: Nombre del producto
- `category`: Categoría del producto
- `units_sold`: Unidades vendidas
- `unit_price`: Precio unitario
- `revenue`: Ingresos generados
- `customer_reviews`: Número de reseñas
- `rating`: Calificación promedio

## Visualizaciones Generadas

1. **revenue_trend.png**: Tendencia de ingresos diarios
2. **category_analysis.png**: Análisis de ingresos por categoría (barras y pastel)
3. **review_analysis.png**: Análisis de calificaciones y reseñas
4. **sales_performance.png**: Rendimiento de ventas por producto y categoría

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.