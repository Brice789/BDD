import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Supposons que le DataFrame est chargé à partir d'un fichier CSV.
# Remplacez le chemin par le chemin réel de votre fichier.
df = pd.read_csv('/Users/bricelewis/Desktop/DataBase.csv', sep=';')

# Remplacement des codes par des labels lisibles pour le sexe.
# Changez 'M' et 'F' selon ce que vous avez dans votre colonne `code_sexe`.
df['code_sexe'] = df['code_sexe'].replace({'M': 'Homme', 'F': 'Femme'})

# Calcul du nombre d'apprentis par sexe.
count_by_sex = df['code_sexe'].value_counts().reset_index()
count_by_sex.columns = ['Sexe', 'Nombre d\'apprentis']

# Création du graphique à barres.
fig = px.bar(
    count_by_sex,
    x='Sexe',
    y='Nombre d\'apprentis',
    title='Comparaison du nombre d\'apprentis hommes et femmes'
)

# Initialisation de l'app Dash.
app = Dash(__name__)

# Définition de la mise en page de l'app.
app.layout = html.Div(children=[
    html.H1(children='Analyse des Apprentis'),

    html.Div(children='''
        Comparaison du nombre d'apprentis hommes et femmes.
    '''),

    dcc.Graph(
        id='sex-comparison-graph',
        figure=fig
    )
])

# Lancement de l'application Dash.
if __name__ == '__main__':
    app.run_server(debug=True)
