#scrapping de données tennis



import requests
from bs4 import BeautifulSoup
import pandas as pd 
import pymongo

url = "https://fr.tennisstats247.com/classements/"


#----------------------------Scrapping------------------------------------------
def scrapPlayer(urll):

    #Instanciation des listes 
    nameColumnWinrateTable = []
    winrateTable = []
    nameColumnTable = []
    scoreTable = []

    #Récupère et parse la nouvelle page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #Récupère le nom des joueurs
    namePlayer = soup.find('h1').text   
    
    #Ici nous crééons une dataframe dans laquelle nous auront le nombre de victoires/défaites par rapport à la surface du terrain
    Table1 = soup.find(class_ = 'gridAlternate winLoss')
    if type(Table1) == type(None):
        winrate = 'pas de stat de winrate' #Dans le cas où il n'y a pas de données, cela empêchait de faire fonctionner la fonction str(winrate)
        winrateTable.append(winrate)
    else :
        for nameColumnWinrate in Table1.find_all('th'):
            nameColumnWinrate = nameColumnWinrate.text
            nameColumnWinrateTable.append(nameColumnWinrate)
        df1 = pd.DataFrame(columns = nameColumnWinrateTable)
        winrate = Table1.find_all('td')
        winrate = str(winrate).replace('<td>','').replace('</td>','').split(',')
        winrate = list(winrate)
        length = len(df1)
        df1.loc[length] = winrate[:3]   
        if len(winrate) == 6:
            df2 = pd.DataFrame(columns = nameColumnWinrateTable)    #Obligation de créer une dataframe par surface afin de pouvoir les remplir correctement
            df2.loc[length] = winrate[3:]
        df1 = pd.concat([df1,df2])  

    #Nous récupérons le tableau de victoires/défaites dans l'année au total et sur toutes les surfaces (dur, terre battue, gazon) et également les titres
    nameColumnTable.append('Player')
    Table2 = soup.find(class_ = 'gridAlternate careerStats')
    for nameColumn in Table2.find_all('span'):
        nameColumn = nameColumn.text
        nameColumnTable.append(nameColumn)          #Création des colonnes de la dataframe
    df3 = pd.DataFrame(columns = nameColumnTable)
    df4 = pd.DataFrame(columns = nameColumnTable)
    df5 = pd.DataFrame(columns = nameColumnTable)
    length = len(df3)

    scoreTable.append(namePlayer)
    for score in Table2.find_all('td'):
        score = score.text
        scoreTable.append(str(score).replace('\n',''))
        if len(scoreTable) == 12:                       #Récupération des données de la dataframe, petit problème observé quant à la mise en forme
            df3.loc[length] = scoreTable 
            scoreTable.append(namePlayer)                                #des données récupérés donc seulement sur l'année en cours
        if len(scoreTable) == 24:
            df4.loc[length] = scoreTable[12:]
            scoreTable.append(namePlayer)
        if len(scoreTable) == 36:
            df5.loc[length] = scoreTable[24:]
        else :
            continue
    df3 = pd.concat([df3,df4,df5])





def main():
    # Connexion avec Mongodb
    client = pymongo.MongoClient('tennis_mongo:27017')
    database = client['Tennis']
    collection = database['Player']
    collection.delete_many({}) # suppression des éléments déjà présent

    playerLinkTable = []

    # Récupère et parse la page
    url = "https://fr.tennisstats247.com/classements/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Récupère l'ensemble des liens allant sur la page de stats de chaque joueur
    result = soup.find(class_='gridAlternate rankings').find_all('a')
    for playerLink in result:
        playerLinkTable.append(playerLink.get('href'))
    
        # Récupère dataframes pour tous les joueurs de la listes et les ajoutes dans la collection
    list_player = []
    for urls in playerLinkTable:
        player = scrapPlayer(urls)
        list_player.append(player)
        dic_player = player.to_dict(orient='records')
        collection.insert_many(dic_player)

if __name__ == '__main__':
    main()
        
    



    



        

    
        



    



    


