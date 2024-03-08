# Import necessary libraries
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import os  # Import the os module

# Correct the path and incorporate data safely
file_path = '/Users/bricelewis/Desktop/DataBase.csv'

# Check if the file exists
if os.path.exists(file_path):
    # Adjusting the file read operation to skip bad lines
    df = pd.read_csv(file_path, sep=';', on_bad_lines='skip')
else:
    print(f"Error: The file at {file_path} does not exist.")
    # Exit the script if file does not exist to avoid running the rest of the code
    exit()

# Initialize the app with external stylesheets for better appearance
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout with an enhanced visual appearance
app.layout = html.Div([
    html.H1('My Dashboard with Data Visualization',
            style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
    dcc.RadioItems(id='column-selector',
                   options=[{'label': col, 'value': col} for col in df.columns],
                   value=df.columns[0],  # default value to first column name
                   style={'textAlign': 'center'}),
    html.Div([
        dash_table.DataTable(data=df.to_dict('records'), 
                             page_size=10, 
                             style_table={'overflowX': 'auto'}),
        dcc.Graph(id='graph-output'),
    ], style={'display': 'flex', 'flexDirection': 'column'})
])

# Callback to update the graph based on radio item selection
@app.callback(
    Output('graph-output', 'figure'),
    [Input('column-selector', 'value')]
)
def update_graph(selected_column):
    # Check if selected column is numerical to plot histogram
    if selected_column in df.select_dtypes(include=[ 'float64', 'int64']).columns:
        return px.histogram(df, x=selected_column)
    # If column is non-numeric, return an empty figure
    return {}

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

