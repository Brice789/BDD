from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# Chargement des données
df = pd.read_csv('/Users/bricelewis/Desktop/DataBase.csv', sep=';')

# Comptage du nombre d'apprentis par entreprise
nombre_apprentis_par_entreprise = df['nom_complet_cfa'].value_counts().reset_index()
nombre_apprentis_par_entreprise.columns = ['Entreprise', 'Nombre d\'Apprentis']

# Création d'un graphique à barres avec Plotly Express
fig = px.bar(nombre_apprentis_par_entreprise.head(10),  # Seulement le top 10 pour une meilleure lisibilité
             x='Nombre d\'Apprentis', 
             y='Entreprise',
             orientation='h',
             title="Entreprises avec le plus grand nombre d'apprentis")

# Initialisation de l'app Dash
app = Dash(__name__)

# Définition de la mise en page de l'app
app.layout = html.Div(children=[
    html.H1(children='Analyse des Apprentis par Entreprise'),

    dcc.Graph(
        id='entreprises-apprentis-graph',
        figure=fig
    )
])

# Lancement de l'application Dash
if __name__ == '__main__':
    app.run_server(debug=True)
