# Proyecto de Mantenimiento Predictivo para Camiones CAEX

## Descripción

Este proyecto implementa un modelo de mantenimiento predictivo para camiones CAEX en operaciones mineras. Utiliza datos históricos y en tiempo real para predecir fallos y generar alertas automáticas de mantenimiento. El objetivo es optimizar los tiempos de operación y reducir los costos asociados a fallos imprevistos.

## Instrucciones de Uso

### Requisitos
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/cristianantilao/project-repo.git
   cd project-repo
2. Instalar dependencias:
   ```bash
   !pip install -r requirements.txt

### Cómo Ejecutarlo
1. Preprocesamiento de Datos: Ejecutar el script de preprocesamiento para transformar los datos crudos en formato utilizable:
   ```bash
   !python3 scripts/preprocessing.py

3. Entrenamiento del Modelo: Entrenar el modelo de mantenimiento predictivo:
   ```bash
   !python3 scripts/train_model.py

5. Generación del Dashboard: Una vez entrenado el modelo, ejecutar el dashboard:
   ```bash
   !python3 scripts/generate_dashboard.py

### Ejemplo de Caso de Uso
Se proporciona un notebook en `notebooks/example_usage.ipynb` que muestra cómo replicar los resultados con datos de muestra.

### Datos de Muestra
En la carpeta `data/processed/` se encuentran los datos de muestra para fines de prueba. El archivo `camiones_caex_data.csv` contiene características de los vehículos y una variable objetivo que indica si el vehículo necesita mantenimiento.

Estructura del Dataset

- `Vehicle_Model`: Tipo de vehículo (Car, SUV, Van, Truck, Bus, Motorcycle).
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
- `Owner_Type`: Tipo de propietario del vehículo.
- `Insurance_Premium`: Monto del seguro.
- `Service_History`: Número de servicios realizados.
- `Accident_History`: Número de accidentes.
- `Fuel_Efficiency`: Eficiencia de combustible en km/l.
- `Tire_Condition`: Estado de los neumáticos.
- `Brake_Condition`: Estado de los frenos.
- `Battery_Status`: Estado de la batería.
- `Need_Maintenance`: Indicador de si el vehículo necesita mantenimiento (1 = Sí, 0 = No).

## Requisitos del Sistema
- **Python:** 3.8 o superior
- **Librerías:**
  - **pandas:**
  - **scikit-learn:**
  - **dash:**
  - **(Más detalles en `requirements.txt`):**


## Licencia
Este proyecto está bajo la licencia [Nombre de la Licencia] - ver el archivo `LICENSE` para más detalles.

## Restricciones de Uso
El proyecto es de uso libre para replicación y análisis en contextos no comerciales. No se permite el uso del código en implementaciones comerciales sin autorización previa.

## Autor
Cristian Antilao

### 3. Recomendaciones adicionales

- **Datos de Muestra:** Incluye solo datos de muestra en el repositorio, evitando cualquier información sensible o confidencial.
- **Dependencias:** Usa `requirements.txt` o un `environment.yml` para listar las dependencias exactas que el proyecto necesita.
- **Documentación Técnica:** Proporciona links a la documentación de las librerías si se usan herramientas avanzadas.
- **Licencia:** Escoge una licencia adecuada para la liberación del código (MIT, Apache, etc.).

### 4. Validación Externa
Para facilitar la validación externa, asegúrate de probar el repositorio en diferentes entornos, y que cualquier persona pueda replicar los resultados con las instrucciones proporcionadas.

Esto asegurará la reproducibilidad del proyecto y que esté listo para la validación externa. ¿Te gustaría que te ayude con alguna parte en particular de esta configuración?
