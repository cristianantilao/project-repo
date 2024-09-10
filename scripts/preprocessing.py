import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Cargar datos desde un archivo CSV."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Limpieza de datos: manejo de valores nulos y formateo."""
    df = df.dropna()  # Elimina filas con valores nulos

    df['Last_Service_Date'] = pd.to_datetime(df['Last_Service_Date'])       # Convierte a datetime
    df["Warranty_Expiry_Date"] = pd.to_datetime(df["Warranty_Expiry_Date"]) # Convierte a datetime

    df['Days_Since_Last_Service'] = (pd.Timestamp.now() - df['Last_Service_Date']).dt.days
    df['Days_Until_Warranty_Expiry'] = (df['Warranty_Expiry_Date'] - pd.Timestamp.now()).dt.days

    #Convertir las columnas categóricas (como "Fuel_Type", "Transmission_Type", "Owner_Type") a variables numéricas mediante codificación (one-hot encoding o label encoding).
    df = pd.get_dummies(df, columns=["Fuel_Type", "Transmission_Type"]) 

    #Escalado de variables numéricas
    scaler = StandardScaler()
    columnas_numericas = ["Mileage", "Odometer_Reading", "Fuel_Efficiency"]
    df[columnas_numericas] = scaler.fit_transform(df[columnas_numericas])

    #Columnas de condiciones
    mapeo_condiciones = {'Poor': 0, 'Average': 1, 'Good': 2, 'New': 3, 'Worn Out': -1}
    df['Maintenance_History'] = df['Maintenance_History'].map(mapeo_condiciones)
    df["Tire_Condition"] = df["Tire_Condition"].map(mapeo_condiciones)
    df["Brake_Condition"] = df["Brake_Condition"].map(mapeo_condiciones)
    df["Battery_Status"] = df["Battery_Status"].map(mapeo_condiciones)

    return df

def split_data(df, test_size=0.2):
    """Divide los datos en conjuntos de entrenamiento y prueba."""
    train, test = train_test_split(df, test_size=test_size, random_state=42)
    return train, test

if __name__ == "__main__":
    # Cargar los datos
    data = load_data('../data/raw/caex_data.csv')
    
    # Limpiar los datos
    data_cleaned = clean_data(data)
    
    # Dividir en conjuntos de entrenamiento y prueba
    train_data, test_data = split_data(data_cleaned)
    
    # Guardar los datos procesados
    train_data.to_csv('../data/processed/train_data.csv', index=False)
    test_data.to_csv('../data/processed/test_data.csv', index=False)
    
    print("Datos procesados y guardados exitosamente.")