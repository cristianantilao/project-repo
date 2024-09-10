# Proyecto de Mantenimiento Predictivo para Camiones CAEX

## Descripción

Este proyecto implementa un modelo de mantenimiento predictivo para camiones CAEX en operaciones mineras. Utiliza datos históricos y en tiempo real para predecir fallos y generar alertas automáticas de mantenimiento. El objetivo es optimizar los tiempos de operación y reducir los costos asociados a fallos imprevistos.

## Instrucciones de Uso

### 1. Preprocesamiento de Datos

Primero, asegúrate de que tienes los datos crudos en el directorio `data/raw`. Luego, ejecuta el script de preprocesamiento:

```bash
python scripts/preprocessing.py

Este script cargará, limpiará y dividirá los datos en conjuntos de entrenamiento y prueba, guardándolos en data/processed/.

Entrenamiento del Modelo
Una vez procesados los datos, puedes entrenar el modelo ejecutando el siguiente comando:

python scripts/train_model.py
Este script entrenará un modelo de Random Forest basado en los datos procesados y lo guardará en models/trained_model.pkl.

Generación del Dashboard
Finalmente, para generar un dashboard interactivo que visualice los datos y alertas de mantenimiento, ejecuta el siguiente script:
python scripts/generate_dashboard.py
Esto iniciará un servidor local y podrás visualizar el dashboard en tu navegador.

Requisitos
Python 3.8 o superior
Librerías necesarias (puedes instalarlas con pip install -r requirements.txt):
pandas
scikit-learn
dash
plotly

Reproducción y Configuración Local
Clona este repositorio:
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio

Instala las dependencias necesarias:
pip install -r requirements.txt
Sigue los pasos anteriores para preprocesar los datos, entrenar el modelo y generar el dashboard.

Licencia
Este proyecto está bajo la licencia [Nombre de la Licencia] - ver el archivo LICENSE para más detalles.

Restricciones de Uso
El proyecto es de uso libre para replicación y análisis en contextos no comerciales. No se permite el uso del código en implementaciones comerciales sin autorización previa.


### 3. Recomendaciones adicionales

- **Datos de Muestra:** Incluye solo datos de muestra en el repositorio, evitando cualquier información sensible o confidencial.
- **Dependencias:** Usa `requirements.txt` o un `environment.yml` para listar las dependencias exactas que el proyecto necesita.
- **Documentación Técnica:** Proporciona links a la documentación de las librerías si se usan herramientas avanzadas.
- **Licencia:** Escoge una licencia adecuada para la liberación del código (MIT, Apache, etc.).

### 4. Validación Externa
Para facilitar la validación externa, asegúrate de probar el repositorio en diferentes entornos, y que cualquier persona pueda replicar los resultados con las instrucciones proporcionadas.

Esto asegurará la reproducibilidad del proyecto y que esté listo para la validación externa. ¿Te gustaría que te ayude con alguna parte en particular de esta configuración?
