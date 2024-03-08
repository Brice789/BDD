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

# Ajout d'une nouvelle colonne pour différencier les individus avec et sans handicap
df['Groupe'] = df['Sexe'] + ' - ' + df['Handicap_Oui_Non_Vide']

# Calculer la moyenne d'âge par sexe et par handicap
average_age_by_group = df.groupby('Groupe')['Age_Jeune_Decembre'].mean().reset_index()

# Filtrage pour n'inclure que les deux premiers groupes (M - Non et F - Oui)
average_age_by_group = average_age_by_group.iloc[:2, :]

# Création du graphique à barres avec Plotly Express
fig = px.bar(
    average_age_by_group, 
    x='Groupe', 
    y='Age_Jeune_Decembre', 
    title="Moyenne d'âge par sexe et par présence de handicap",
    labels={'Groupe': 'Groupe (Sexe - Handicap)', 'Age_Jeune_Decembre': "Âge moyen"}
)

# Initialisation de l'app Dash
app = Dash(__name__)

# Définition de la mise en page de l'app
app.layout = html.Div([
    html.H1("Analyse de l'âge moyen des apprentis par sexe et handicap"),
    dcc.Graph(
        id='age-sex-handicap-graph',
        figure=fig
    )
])

# Lancement de l'application Dash
if __name__ == '__main__':
    app.run_server(debug=True)
