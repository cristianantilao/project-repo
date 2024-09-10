# preprocessing.py
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    """Cargar datos desde un archivo CSV."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Limpieza de datos: manejo de valores nulos y formateo."""
    df = df.dropna()  # Elimina filas con valores nulos
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # Convierte a datetime
    return df

def split_data(df, test_size=0.2):
    """Divide los datos en conjuntos de entrenamiento y prueba."""
    train, test = train_test_split(df, test_size=test_size, random_state=42)
    return train, test

if __name__ == "__main__":
    # Cargar los datos
    data = load_data('data/raw/caex_data.csv')
    
    # Limpiar los datos
    data_cleaned = clean_data(data)
    
    # Dividir en conjuntos de entrenamiento y prueba
    train_data, test_data = split_data(data_cleaned)
    
    # Guardar los datos procesados
    train_data.to_csv('data/processed/train_data.csv', index=False)
    test_data.to_csv('data/processed/test_data.csv', index=False)
    
    print("Datos procesados y guardados exitosamente.")
