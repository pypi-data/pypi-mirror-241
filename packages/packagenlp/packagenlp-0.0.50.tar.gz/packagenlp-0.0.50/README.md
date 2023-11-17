# Package NLP

## Informations

> Initié le : 02/03/2023

> Interlocuteurs : Marine CERCLIER, Grégory GAUTHIER, Tangi LE TALLEC, Alan BIGNON, Islem EZZINE

> Dans le cadre du projet interne DataScience de package NLP

## Description

L'objectif de ce projet est d'avoir un package NLP permettant d'effectuer différentes tâches de traitement du langage naturel de manière simple et configurable.
Vous pouvez y retrouver différents dossiers et eléments dont chacun répond à des objectifs précis :

* dossier packagenlp : Les différents scripts Python nécessaires au fonctionnement du projet sont enregistrés dans ce dossier.
* fichier requirements.txt : Il contient les packages présents sur l'environnement de travail du développeur et qui sont donc nécessaires au bon fonctionnement du code.
* fichier LICENSE : Spécifie par quelle license juridique est couvert notre projet.
* fichier README.md : C'est le présent fichier. Il constitue la documentation principale du projet, c'est-à-dire celle qui doit être lue en premier par un utilisateur qui veut comprendre de quoi le projet traite.

## Présentation de la Class NLP

La permet de choisirs entre deux bibliothèques populaires pour le NLP, nltk et spacy.
Les principales fonctionnalités de cette classe sont :

* Initialisation avec le choix du package NLP à utiliser (nltk ou spacy)
* Nettoyage des mots vides (stop words) en français en ajoutant ou supprimant des mots vides spécifiques
* Conversion du texte en minuscules
* Nettoyage du texte en supprimant tous les caractères spéciaux, sauf ceux spécifiés dans l'argument exception, et en option, en conservant les chiffres
* Suppression des accents d'un texte en les remplaçant par les lettres correspondantes sans accent
* Lemmatisation du texte en tenant compte des exceptions de lemmatisation, en conservant ou non les chiffres, et en excluant certains types de mots


## Utilisation de la class analyse (streamlit)

* La classe analyse que nous avons créée est intégrée dans une application Streamlit, facilitant ainsi l'analyse interactive de données en utilisant des techniques de NLP (Natural Language Processing ou Traitement Automatique du Langage Naturel en français). Voici les étapes principales et les fonctionnalités offertes :

* Chargement du fichier CSV : l'utilisateur peut charger un fichier CSV dans l'application. Les données du fichier sont ensuite stockées et prêtes pour l'analyse.

* Application des fonctions de NLP : une fois le fichier CSV chargé, les différentes fonctions de NLP créées précédemment peuvent être appliquées sur les données textuelles présentes dans le fichier.

* Visualisation des informations : après avoir traité les données avec les fonctions de NLP, l'application permet de visualiser des informations pertinentes sous forme graphique. Cela peut inclure des histogrammes, des nuages de mots, des diagrammes de dispersion, etc., facilitant ainsi l'interprétation des résultats.

* Interactivité et personnalisation : L'utilisateur a la possibilité de personnaliser les analyses en choisissant les paramètres des fonctions de NLP à appliquer, ainsi que les types de visualisations à générer.

Afin de lancé l'application, il suffit après import du package, créer un fichier python (.py) en y rajoutant les lignes suivante :

```
from packagenlp.analyse import ClassAnalyse

if __name__ == "__main__":
    app = ClassAnalyse()
    app.main()
```
Après enregistrement, il suffira d'ouvrir un terminal et ce placer dans l'emplacement de votre fichié et lancé la commande suivante :

`streamlit run "nom_du_fichier.py"`


