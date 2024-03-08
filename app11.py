from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# Chargement du dataset
df = pd.read_csv('/Users/bricelewis/Desktop/DataBase.csv', sep=';')

# Comptage du nombre d'apprentis par code postal
nombre_apprentis_par_code_postal = df['code_postal_site'].value_counts().reset_index()
nombre_apprentis_par_code_postal.columns = ['Code Postal', 'Nombre d\'Apprentis']

# Initialisation de l'app Dash
app = Dash(__name__)

# Création du graphique à barres avec Plotly Express
fig = px.bar(
    nombre_apprentis_par_code_postal.head(10),  # Affichage du top 10 pour une meilleure lisibilité
    x='Code Postal', 
    y='Nombre d\'Apprentis',
    title="Nombre d'apprentis par code postal"
)

# Définition de la mise en page de l'app
app.layout = html.Div(children=[
    html.H1(children='Analyse des Apprentis par Code Postal'),

    dcc.Graph(
        id='apprentis-code-postal-graph',
        figure=fig
    )
])

# Lancement de l'application Dash
if __name__ == '__main__':
    app.run_server(debug=True)
