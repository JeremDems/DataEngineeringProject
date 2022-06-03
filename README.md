# **DataEngineeringProjet : Tennis scrapping**

## **Description**

Ce projet a pour but de récupérer des données sur internet afin de les afficher sur une autre page où d'une autre manière (générée à partir d'un environnement en particulier). J'ai donc utilisé une base de donnée sur le Tennis afin de récupérer les statistiques des joueurs les plus performants sur ce site(https://fr.tennisstats247.com/classements/).

<br>

## **User Guide**

### **Récupération et lancement du projet**

Le projet est à récupérer sur Git (https://github.com/JeremDems/DataEngineeringProject), il vous faudra le cloner sur votre ordinateur (par défaut dans les documents) afin de l'utiliser

Pour lancer le projet, ouvrez votre shell et rendez-vous sur le répertoire courant du projet (dans notre cas /DataEngineeringProject) via la commande 'cd'. Ensuite tapez "docker-compose up --build" (sur votre shell également), vérifiez que le répertoire "data" sur la racine du projet n'existe pas pour le faire tourner, sinon supprimez-le avant de lancer le docker-compose up. 
Pour se faire, vous aurez besoin d'installer docker (si cela n'est pas fait), qui nous permettra la création de l'image (packages, version de python) qui assurera le bon déroulement de l'application

Pour lancer le dashboard, il faut se rendre à l'adresse suivante `http://localhost:8050/`. 

<br>

### **Fonctionnement du dashboard**

Le Dashbaord sera ainsi composé d'un onglet `Statistiques générales` qui contiendra diverses données sur les meilleurs joueurs (nombre de victoires/défaites). Ne pas hésiter à zoomer sur les joueurs.

<br>

### **Composition du projet et liste des technologies utilisés**

Le projet est composé de 2 fichiers python :
* - scrapping de données tennis.py qui récupèrera les données puis enverront ces données dans les bases de données mongo afin de les traiters via un dashboard
* - dashboard.py pour le traitement et l'affichage des données

Pour le scraping de données, nous utiliserons:
* - requests afin de faire nos requetes html.
* - beautifulsoup (bs4) afin de parser le code que l'on a récupéré.

Pour le traîtement et le stockage des données :
* - pandas pour la création de Dataframe qui contiennent nos données.
* - mongodb afin de stocker nos données transformées.
  
Pour l'affichage des données :
* - Dash pour la création d'un dashboard intéractif.
* - Plotly express afin de faire de mettre les données sous forme de graphique (dans notre cas en diagramme barre).

 
<br>

*<div style="text-align: right"> Demay Jérémy</div>*


<br>
 
