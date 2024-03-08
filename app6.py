# Import necessary libraries
from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import os

# Correct the file path and ensure the file exists
file_path = '/Users/bricelewis/Desktop/DataBase.csv'  # Replace with your actual path
if not os.path.exists(file_path):
    print(f"Error: The file at {file_path} does not exist.")
    exit()

# Read the CSV file with the correct delimiter
df = pd.read_csv(file_path, sep=';')  # Assuming semicolon delimiter

# Initialize the Dash app
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("My Dashboard with Data Visualization"),
    dcc.Graph(id='graph-output'),
    dash_table.DataTable(
        id='datatable-output',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        page_size=10
    )
])

# Define callback to update graph
@app.callback(
    Output('graph-output', 'figure'),
    [Input('datatable-output', 'data')]
)
def update_graph(data):
    # Use the DataFrame directly, no need to filter since we want all types of diplomas
    fig = px.pie(df, names='type_diplome', title="Répartition des types de diplômes")
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
