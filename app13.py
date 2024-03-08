import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# Simulant le chargement des données à partir d'un DataFrame directement pour cet exemple
data = {
    "ID_Apprenti": [890, 891, 892],
    "Age_Jeune_Decembre": [22, 22, 25],
    "Sexe": ['M', 'F', 'M'],
    "Handicap_Oui_Non_Vide": ['Non', 'Oui', 'Oui'],
    "Code_Postal_Jeune": [94228, 86507, 24247],
    "Libelle_Ville_Jeune": ['Le Goff-les-Bains', 'Verdier-les-Bains', 'Neveu'],
    "ID_Entreprise": [938, 921, 917]
}

df = pd.DataFrame(data)

# Calculer la moyenne d'âge par département
average_age_by_department = df.groupby('Code_Postal_Jeune')['Age_Jeune_Decembre'].mean().reset_index()

# Création du graphique à barres avec Plotly Express
fig = px.bar(
    average_age_by_department, 
    x='Code_Postal_Jeune', 
    y='Age_Jeune_Decembre', 
    title="Moyenne d'âge par département",
    labels={'Code_Postal_Jeune': 'Code Postal', 'Age_Jeune_Decembre': "Âge moyen"}
)

# Initialisation de l'app Dash
app = Dash(__name__)

# Définition de la mise en page de l'app
app.layout = html.Div([
    html.H1("Analyse de l'âge moyen des apprentis par département"),
    dcc.Graph(
        id='age-department-graph',
        figure=fig
    )
])

# Lancement de l'application Dash
if __name__ == '__main__':
    app.run_server(debug=True)
