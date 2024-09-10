# Proyecto de Mantenimiento Predictivo para Camiones CAEX

## Descripción

Este proyecto implementa un modelo de mantenimiento predictivo para camiones CAEX en operaciones mineras, utilizando técnicas de machine learning. Utiliza datos históricos y en tiempo real para predecir fallos y generar alertas automáticas de mantenimiento. El objetivo es optimizar los tiempos de operación y reducir los costos asociados a fallos imprevistos.

### Contexto del Problema

En la operación minera, los camiones CAEX enfrentan condiciones extremas que pueden provocar fallos inesperados, lo que resulta en paradas no planificadas y aumento de costos. El mantenimiento actual es reactivo, lo que puede llevar a intervenciones innecesarias o reparaciones urgentes. Este proyecto propone una solución basada en machine learning para predecir la necesidad de mantenimiento y evitar estos problemas.

## Propuesta de Solución

La solución propuesta consiste en construir un modelo predictivo que use datos históricos y en tiempo real para identificar si un camión requiere o no mantención. Se implementará un dashboard para visualizar las predicciones y generar alertas de mantenimiento preventivo.

## Estructura del Repositorio
- **data/:** Contiene el dataset utilizado para el análisis.
- **scripts/:** Scripts Python para el procesamiento de datos y entrenamiento del modelo.
- **notebooks/:** Jupyter Notebooks con ejemplos de uso y análisis.
- **requirements.txt:** Lista de dependencias del proyecto.
- **README.md:** Documentación del proyecto.

## Instrucciones de Uso

### Requisitos
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/cristianantilao/project-repo.git
   cd project-repo
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt

### Cómo Ejecutarlo
1. Preprocesamiento de Datos: Ejecutar el script de preprocesamiento para transformar los datos crudos en formato utilizable:
   ```bash
   python scripts/preprocessing.py

3. Entrenamiento del Modelo: Entrenar el modelo de mantenimiento predictivo:
   ```bash
   python scripts/train_model.py

5. Generación del Dashboard: Una vez entrenado el modelo, ejecutar el dashboard:
   ```bash
   python scripts/generate_dashboard.py

### Ejemplo de Caso de Uso
Se proporciona un notebook en `notebooks/example_usage.ipynb` que muestra cómo realizar el análisis y replicar los resultados con datos de muestra.

### Datos de Muestra
En la carpeta `data/processed/` se encuentran los datos de muestra para fines de prueba. El archivo `camiones_caex_data.csv` contiene características de los vehículos y una variable objetivo que indica si el vehículo necesita mantenimiento.

Estructura del Dataset

- `Mileage`: Total de kilómetros recorridos.
- `Maintenance_History`: Historia de mantenimiento del vehículo.
- `Reported_Issues`: Número de problemas reportados.
- `Vehicle_Age`: Edad del vehículo en años.
- `Fuel_Type`: Tipo de combustible utilizado.
- `Transmission_Type`: Tipo de transmisión.
- `Engine_Size`: Tamaño del motor en cc.
- `Odometer_Reading`: Lectura actual del odómetro.
- `Last_Service_Date`: Fecha del último servicio.
- `Warranty_Expiry_Date`: Fecha de expiración de la garantía.
- `Service_History`: Número de servicios realizados.
- `Accident_History`: Número de accidentes.
- `Fuel_Efficiency`: Eficiencia de combustible en km/l.
- `Tire_Condition`: Estado de los neumáticos.
- `Brake_Condition`: Estado de los frenos.
- `Battery_Status`: Estado de la batería.
- `Need_Maintenance`: Indicador de si el vehículo necesita mantenimiento (1 = Sí, 0 = No).

## Requisitos del Sistema
- **Python:** 3.11 o superior
- **Librerías:**
  - **pandas:**
  - **scikit-learn:**
  - **dash:**
  - **(Más detalles en `requirements.txt`):**

## Recursos Adicionales
- **Documentación de Scikit-learn:** https://scikit-learn.org/stable/
- **Documentación de Pandas:** https://pandas.pydata.org/
- **Documentación de Dash:** https://dash.plotly.com/

## Restricciones de Uso
El proyecto es de uso libre para replicación y análisis en contextos no comerciales. No se permite el uso del código en implementaciones comerciales sin autorización previa.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Autor
Cristian Antilao
