import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

def train_model(train_data):
    """Entrena un modelo Random Forest en los datos de entrenamiento."""
    X = train_data.drop(columns=['target'])  # Variables predictoras
    y = train_data['target']  # Variable objetivo

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    return model

def evaluate_model(model, test_data):
    """Evalúa el modelo en los datos de prueba."""
    X_test = test_data.drop(columns=['target'])
    y_test = test_data['target']
    
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Precisión del modelo: {accuracy:.2f}")
    
    return accuracy

if __name__ == "__main__":
    # Cargar los datos
    train_data = pd.read_csv('data/processed/train_data.csv')
    test_data = pd.read_csv('data/processed/test_data.csv')
    
    # Entrenar el modelo
    model = train_model(train_data)
    
    # Evaluar el modelo
    evaluate_model(model, test_data)
    
    # Guardar el modelo entrenado
    with open('models/trained_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("Modelo entrenado y guardado exitosamente.")
