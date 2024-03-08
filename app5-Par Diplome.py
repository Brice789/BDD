import pandas as pd
from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output
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
    # Assuming the column name is actually 'type_diplome', otherwise replace with the correct name
    dcc.Dropdown(
        id='type_diplome-dropdown',
        options=[{'label': i, 'value': i} for i in df['type_diplome'].unique()],
        value=df['type_diplome'].unique()[0]
    ),
    dcc.Graph(id='graph-output'),
    dash_table.DataTable(
        id='datatable-output',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        page_size=10
    )
])

# Define callback to update graph based on the dropdown selection
@app.callback(
    Output('graph-output', 'figure'),
    [Input('type_diplome-dropdown', 'value')]
)
def update_graph(value):
    filtered_df = df[df['type_diplome'] == value]
    fig = px.histogram(filtered_df, x='type_diplome')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
