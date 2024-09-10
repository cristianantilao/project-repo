import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import pickle
import numpy as np

def train_model(X_train, y_train):
    """Entrena un modelo Random Forest en los datos de entrenamiento con validación cruzada."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Realizamos validación cruzada con 5 folds y calculamos métricas
    scoring = ['accuracy', 'precision', 'recall', 'f1']
    cv_results = cross_validate(model, X_train, y_train, cv=5, scoring=scoring)
    
    print("Resultados de la validación cruzada (5-fold):")
    print(f"Accuracy: {cv_results['test_accuracy'].mean():.2f}")
    print(f"Precision: {cv_results['test_precision'].mean():.2f}")
    print(f"Recall: {cv_results['test_recall'].mean():.2f}")
    print(f"F1-score: {cv_results['test_f1'].mean():.2f}")
    
    # Entrenamos el modelo en todo el conjunto de entrenamiento
    model.fit(X_train, y_train)
    
    return model

def evaluate_model(model, X_test, y_test):
    """Evalúa el modelo en los datos de prueba y calcula varias métricas."""
    predictions = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)
    
    print(f"\nResultados en los datos de prueba:")
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-score: {f1:.2f}")
    
    # Calcular la matriz de confusión
    conf_matrix = confusion_matrix(y_test, predictions)
    
    return accuracy, precision, recall, f1, conf_matrix

if __name__ == "__main__":
    # Cargar los datos
    train_data = pd.read_csv('../data/processed/train_data.csv')
    test_data = pd.read_csv('../data/processed/test_data.csv')
    
    # Preparar las variables predictoras y objetivo
    X_train = train_data.drop(columns=['Need_Maintenance', 'Last_Service_Date', "Warranty_Expiry_Date"])
    y_train = train_data['Need_Maintenance']
    
    X_test = test_data.drop(columns=['Need_Maintenance', 'Last_Service_Date', "Warranty_Expiry_Date"])
    y_test = test_data['Need_Maintenance']
    
    # Entrenar el modelo con validación cruzada
    model = train_model(X_train, y_train)
    
    # Evaluar el modelo en los datos de prueba
    accuracy, precision, recall, f1, conf_matrix = evaluate_model(model, X_test, y_test)
    
    # Guardar el modelo entrenado
    with open('../models/trained_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    # Guardar la matriz de confusión
    np.save('../models/confusion_matrix.npy', conf_matrix)
    
    print("\nModelo entrenado y guardado exitosamente.")
    print("Matriz de confusión guardada exitosamente.")