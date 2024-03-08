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

# Define the callback for the Graph component
@app.callback(
    Output('graph-output', 'figure'),
    [Input('datatable-output', 'data')]
)
def update_graph(data):
    # Calculate counts of apprentices per city and get the top 5
    top_cities = df['libelle_ville_jeune'].value_counts().head(5)
    top_cities = top_cities.reset_index()
    top_cities.columns = ['City', 'Number of Apprentices']

    # Create a bar chart
    fig = px.bar(
        top_cities,
        x='Number of Apprentices',
        y='City',
        orientation='h',
        title="Top 5 des villes avec le plus grand nombre d'apprentis",
        text='Number of Apprentices'
    )
    
    # Update layout for better readability
    fig.update_layout(
        yaxis=dict(autorange="reversed"),  # To show the highest value on top
        xaxis_title="Nombre d'apprentis",
        yaxis_title="Ville",
    )

    # Show the number of apprentices next to each bar for clarity
    fig.update_traces(textposition='outside')
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
