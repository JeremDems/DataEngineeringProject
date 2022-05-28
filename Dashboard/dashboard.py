import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_table
from dash import callback_context
import dash_bootstrap_components as dbc
import pymongo
import plotly.express as px
import pandas as pd

# Connexion avec Mongodb
client = pymongo.MongoClient('tennis_mongo:27017')
database = client['Tennis']
collection = database['Player']

def generate_page():
    # Création de df pour l'affichage des données

    data1 = pd.DataFrame(list(collection.find({"Classement":{'$gte':10}})))[["Player","Titres", "V", "D", "Année"]]
    data2 = pd.DataFrame(list(collection.find({"Victoire":{'$gt':15}})))[["Surface", "Victoires","Défaites"]]
    data3 = pd.DataFrame(list(collection.find({})))[["VD", "DD", "VTB","DTB"]]
    data4 = pd.DataFrame(list(collection.find({})))[["Classement", "V", "D"]]


    # Création de graphique pour l'affichage des données
    bar1 = px.bar(data1, x = "player", y = "V", barmode="group") 
    bar2 = px.bar(data1, x = "player", y = "D", barmode="group") 
    bar3 = px.bar(data2, x = "player", y = "VD", barmode="group", facet_col="Season") 
    bar4 = px.bar(data2, x = "player", y = "DD", barmode="group", facet_col="Season") 
    bar5 = px.bar(data2, x = "player", y = "VTB", barmode="group", facet_col="Season") 
    bar6 = px.bar(data2, x = "player", y = "DTB", barmode="group", facet_col="Season") 

    return html.Div(style={'font-family' : 'Trebuchet MS, sans-serif'}, children=[
        html.Div( id="header", children=[
            html.H2(id = "titre", children=f'Tennis Scraping',
                            style={'textAlign': 'center', 'color': '#FFFFFF', 'fontSize': 70}),
            
            html.H4(id = "name", children=f'Demay Jérémy', 
                            style={'textAlign': 'center', 'color': '#FFFFFF', 'marginBottom': '85px'}),

            html.H3(id = "Description", 
                        children=f"Ce projet permet de récupérer les statistiques des joueurs de tennis lors de l'année 2022.",
                        style={'textAlign': 'center', 'color': '#FFFFFF', 'marginBottom': "100px"}),
        ]),

        dcc.Tabs([
            dcc.Tab(label='Statistiques générales', children=[
                html.Div(children=[
                #html.Button('Refresh', id='Refresh', n_clicks=0),
                html.H5('Joueurs ayant le plus de victoires cette année', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px'},
                    id = 'graph1',
                    figure = bar1
                ),
                html.H5('Nombre de défaites cette année', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph2',
                    figure = bar2
                ),
                html.H5('Nombre de victoires sur une surface dur', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph3',
                    figure = bar3
                ),
                html.H5('Nombre de défaites sur une surface dur', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph4',
                    figure = bar4
                ),
                html.H5('Nombre de victoires sur terre battue', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph5',
                    figure = bar5
                ),
                html.H5('Nombre de défaites sur terre battue', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph6',
                    figure = bar6
                ),
                ]),
            ], style={'fontSize': 20, 'color' : 'black'}),
        ]),    
    ]
    )




if __name__ == '__main__':

    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY]) 

    app.layout = generate_page # démarrer la page

    #
    # RUN APP
    #

    app.run_server(debug=True, host = '0.0.0.0') # (8)