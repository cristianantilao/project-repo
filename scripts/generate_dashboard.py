import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Cargar datos procesados
df = pd.read_csv('../data/processed/train_data.csv')
conf_matrix = np.load('../models/confusion_matrix.npy')

# Procesar datos
df['Last_Service_Date'] = pd.to_datetime(df['Last_Service_Date'])
df.set_index('Last_Service_Date', inplace=True)

# Crear la app de Dash
app = dash.Dash(__name__)

# Gráfico de línea (resample de Need_Maintenance por mes)
resample_fig = px.line(
    df['Need_Maintenance'].resample('M').sum().reset_index(), 
    x='Last_Service_Date', 
    y='Need_Maintenance',
    title='Frecuencia de Mantenimiento a lo Largo del Tiempo',
    labels={'Last_Service_Date': 'Fecha', 'Need_Maintenance': 'Mantenimientos requeridos'}
)

# Gráfico de pastel (Condición de los Neumáticos)
pie_fig = px.pie(
    df.reset_index(), 
    names='Tire_Condition', 
    title='Condición de los Neumáticos',
    hole=0.3,  # para hacerlo tipo dona
    color_discrete_sequence=['#ff9999','#66b3ff','#99ff99']
)

# Crear histograma apilado usando las columnas dummy de tipo de combustible
hist_fig = go.Figure()

# Añadir las barras para cada tipo de combustible
hist_fig.add_trace(go.Histogram(
    x=df.index, 
    y=df['Fuel_Type_Diesel'], 
    name='Diesel', 
    marker_color='blue',
    opacity=0.75
))

hist_fig.add_trace(go.Histogram(
    x=df.index, 
    y=df['Fuel_Type_Electric'], 
    name='Electric', 
    marker_color='green',
    opacity=0.75
))

hist_fig.add_trace(go.Histogram(
    x=df.index, 
    y=df['Fuel_Type_Petrol'], 
    name='Petrol', 
    marker_color='red',
    opacity=0.75
))

# Actualizar el layout del histograma
hist_fig.update_layout(
    barmode='stack',
    title='Distribución de Mantenimiento por Tipo de Combustible',
    xaxis_title='Fecha',
    yaxis_title='¿Requiere Mantenimiento?',
    legend_title='Tipo de Combustible',
    bargap=0.2
)

# Crear la matriz de confusión con anotaciones
conf_matrix_fig = go.Figure(data=go.Heatmap(
    z=conf_matrix,
    x=['Predicted No', 'Predicted Yes'],
    y=['Actual No', 'Actual Yes'],
    colorscale='Viridis',
    colorbar=dict(title='Conteo'),
    text=conf_matrix,  # Añadir conteos a las celdas
    texttemplate="%{text}",  # Mostrar texto con el conteo
    textfont=dict(size=14),  # Tamaño de la fuente del texto
))

# Actualizar el layout del gráfico de la matriz de confusión
conf_matrix_fig.update_layout(
    title='Matriz de Confusión',
    xaxis_title='Predicciones',
    yaxis_title='Valores Reales',
    xaxis=dict(tickvals=[0, 1], ticktext=['No', 'Sí']),
    yaxis=dict(tickvals=[0, 1], ticktext=['No', 'Sí']),
    height=400,
    width=400
)

# Layout de la app
app.layout = html.Div([
    html.H1("Dashboard de Mantenimiento Predictivo"),
    
    dcc.Graph(id='maintenance-line', figure=resample_fig),
    
    dcc.Graph(id='tire-condition-pie', figure=pie_fig),
    
    dcc.Graph(id='fuel-maintenance-hist', figure=hist_fig),
    
    dcc.Graph(id='confusion-matrix', figure=conf_matrix_fig)
])

# Ejecutar el servidor
if __name__ == '__main__':
    app.run_server(debug=True)
