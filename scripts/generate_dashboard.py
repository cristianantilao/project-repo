import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Cargar datos procesados
data = pd.read_csv('data/processed/train_data.csv')

# Crear la app de Dash
app = dash.Dash(__name__)

# Layout de la app
app.layout = html.Div([
    html.H1("Dashboard de Mantenimiento Predictivo"),
    
    dcc.Graph(
        id='example-graph',
        figure=px.scatter(data, x='timestamp', y='sensor_value', color='target')
    )
])

# Ejecutar el servidor
if __name__ == '__main__':
    app.run_server(debug=True)
