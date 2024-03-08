# Import necessary libraries
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import os  # Correctly import os

# Correct the path and incorporate data safely
file_path = '/Users/bricelewis/Desktop/DataBase.csv'

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
    html.Div(className='row', children=[
        html.H1('My Dashboard with Data Visualization',
                style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
        dcc.RadioItems(options=[{'label': i, 'value': i} for i in ['pop', 'lifeExp', 'gdpPercap']],
                       value='lifeExp',
                       inline=True,
                       id='my-radio-buttons-final',
                       style={'textAlign': 'center', 'margin': 'auto'}),
    ]),
    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dash_table.DataTable(data=df.to_dict('records'), 
                                 page_size=10, 
                                 style_table={'overflowX': 'auto'}),
        ]),
        html.Div(className='six columns', children=[
            dcc.Graph(id='histo-chart-final'),
        ])
    ])
])

# Callback to update the graph based on radio item selection
@app.callback(
    Output('histo-chart-final', 'figure'),
    Input('my-radio-buttons-final', 'value')
)
def update_graph(selected_column):
    if selected_column in df.columns:
        return px.histogram(df, x='continent', y=selected_column, histfunc='avg')
    # Default case if column not in df, providing an empty figure
    return {'data': []}

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
