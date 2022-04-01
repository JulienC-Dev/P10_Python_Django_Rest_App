# Développement d'une API via Django REST

## Overview

Création d'une API pour une société d'édition de logiciels permettant notamment de remonter et de suivre des problèmes
techniques(tracking system)

**API permet notamment de :**
* Créer divers projets
* D'ajouter des utilisateurs à des projets spécifiques,
* de créer des problèmes au sein des projets et d'attribuer des libellés à ces problèmes en
fonction de leurs priorités, de balises ..
* de permettre la création de commentaires sur différents problèmes en respectant des critères d'autorisations et de
contraintes sur les objects. L'accès à certaines ressources nécessitent des autorisations spéciales.

L'Authentification de l'utilisateur est réalisée via JWT (JSON Web Token) sur chacune des requêtes via le ```Header```

Une documentation de l'API a été réalisée via Postman
La documentation est publiée à l'adresse suivante :  https://documenter.getpostman.com/view/18264679/UVyrUbtQ

Les requêtes sont sous format JSON


## Test et developpement

1. Pré-requis pour l'utilisation de API:

    * Installer la dernière version de Python sur le site - https://www.python.org
    * Ouvrir l'interpréteur de commandes de Python
    * Créer un nouveau repertoire via la commande : ```cd mkdir projet10```
    * Initialiser un environnement virtuel via la commande : ```python -m venv env```
    * Taper dans la console et au niveau du dossier racine : ```git init```
    * Cloner le dépo via la console : ```git clone https://github.com/JulienC-Dev/P10_application_API_Django_Rest/tree/dev```
    * Puis installer les dépendances: ```pip install -r requirements.txt```
    * Télécharger Postman en local à l'adresse suivante pour la gestion des requêtes: ```https://www.postman.com/downloads/```

2. Connection au serveur local http://127.0.0.1:8000/
   * Aller sur le sous-dossier - Projet10 via la commande  : ```cd Projet10```
   * Créer un superuser via la ligne de commande ou utiliser les dataset de connection : ```python manage.py createsuperuser```
   * Lancer le serveur local via la commande : ```python manage.py runserver```
   * Ouvrir le naviguateur web puis taper dans la barre de recherche : ```http://127.0.0.1:8000/admin/```

## Dataset de connection

La base de données est en db.sqlite3.

1. Connection au site admin local http://127.0.0.1:8000/admin

| Nom Admin          | Mots de passe |
| -------------      |:-------------:|
| julien             | j             |


## Ressources

Vous pouvez trouver ces ressources utiles:

* Overview Django : https://www.djangoproject.com/start/overview/
* Overview Django REST : https://www.django-rest-framework.org
* Overview Postman : https://learning.postman.com/docs/getting-started/introduction/

## Version 0.1

Auteur JulienC-Dev - github : https://github.com/JulienC-Dev/P10_application_API_Django_Rest/tree/dev


