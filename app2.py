# Importation des bibliothèques nécessaires
from dash import Dash, html, dcc, dash_table, Input, Output
import pandas as pd

# URL hypothétique de votre fichier CSV (remplacez par l'URL de vos données réelles)
url_donnees_cfa = '/Users/bricelewis/Desktop/DataBasecopie.csv'

# Charger les données depuis le CSV
df = pd.read_csv("/Users/bricelewis/Desktop/DataBasecopie.csv", on_bad_lines='skip')

# Filtrer les données pour obtenir uniquement les entreprises situées à Paris
df_paris = df[df['libelle_ville_jeune'].str.contains("Paris", case=False)]

# Initialisation de l'application Dash
app = Dash(__name__)

# Mise en place de la disposition de l'application
app.layout = html.Div([
    html.H1('Entreprises et apprentis situés à Paris', style={'textAlign': 'center'}),
    dash_table.DataTable(
        id='table-paris',
        columns=[{"name": i, "id": i} for i in df_paris.columns],
        data=df_paris.to_dict('records'),
        page_size=10,
        style_table={'overflowY': 'auto'}
    )
])

# Exécution de l'application
if __name__ == '__main__':
    app.run_server(debug=True)
