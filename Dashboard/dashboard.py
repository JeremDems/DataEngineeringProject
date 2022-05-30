import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table
from dash import callback_context
from dash.dash_table.Format import Group
import dash_bootstrap_components as dbc
import pymongo
import plotly.express as px
import pandas as pd

# Connexion avec Mongodb
client = pymongo.MongoClient('tennis_mongo:27017')
database = client['Tennis']
collection1 = database['Player1']
# collection2 = database['Player2']

def generate_page():
    # Création de df pour l'affichage des données

    data1 = pd.DataFrame(list(collection1.find({'Classement':{'$gte':5}})))[['Player', 'Année', 'VTB', 'DTB']]
    data2 = pd.DataFrame(list(collection1.find({'Classement':{'$gte':5}})))[['Player', 'Année', 'VD', 'DD']]
    data3 = pd.DataFrame(list(collection1.find({'Classement':{'$gte':5}})))[['Player', 'Année', 'Titres', 'V']]
    # data4 = pd.DataFrame(list(collection2.find({"Victoires":{'$gt':15}})))[["Surface", "Victoires","Défaites"]]


    # Création de graphique pour l'affichage des données
    # bar1 = px.bar(data4, x = "Player", y = "Victoires", barmode="group") 
    # bar2 = px.bar(data4, x = "Player", y = "Défaites", barmode="group") 
    bar3 = px.bar(data2, x = "Player", y = "VD", barmode="group", facet_col="Année") 
    bar4 = px.bar(data2, x = "Player", y = "DD", barmode="group", facet_col="Année") 
    bar5 = px.bar(data1, x = "Player", y = "VTB", barmode="group", facet_col="Année") 
    bar6 = px.bar(data1, x = "Player", y = "DTB", barmode="group", facet_col="Année") 
    bar7 = px.bar(data3, x = "Player", y = "Titres", barmode="group", facet_col="Année") 
    bar8 = px.bar(data3, x = "Player", y = "V", barmode="group", facet_col="Année")

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
                # html.H5('Joueurs ayant le plus de victoires cette année', style={'textAlign': 'center', 'marginTop': '40px'}),
                # dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px'},
                #     id = 'graph1',
                #     figure = bar1
                # ),
                # html.H5('Nombre de défaites cette année', style={'textAlign': 'center', 'marginTop': '40px'}),
                # dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                #     id = 'graph2',
                #     figure = bar2
                # ),
                html.H5('Nombre de victoires sur une surface dur', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph1',
                    figure = bar3
                ),
                html.H5('Nombre de défaites sur une surface dur', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph2',
                    figure = bar4
                ),
                html.H5('Nombre de victoires sur terre battue', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph3',
                    figure = bar5
                ),
                html.H5('Nombre de défaites sur terre battue', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph4',
                    figure = bar6
                ),
                html.H5('Nombre de titres gagnés cette année', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph5',
                    figure = bar7
                ),
                html.H5('Nombre de victoires au total cette année', style={'textAlign': 'center', 'marginTop': '40px'}),
                dcc.Graph(style={'backgroundColor' : '#EFDDBC', 'width' : '80%', 'margin' : 'auto', 'marginTop' : '20px', 'marginBottom' : '20px'},
                    id = 'graph6',
                    figure = bar8
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

    app.run_server(debug=True, host = '0.0.0.0', port = 8050) # (8)