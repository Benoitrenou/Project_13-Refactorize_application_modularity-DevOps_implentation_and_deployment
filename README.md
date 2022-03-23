# projet_13

Ce projet est une application web développée pour Orange County Lettings

Cette application a été construite via Django Framework dans sa version 3.0

Afin de faire fonctionner cette application en local, veuillez suivres les indications suivantes

## Clônage du projet

Tout d'abord, clônez en local le dépôt distant via la commande suivante dans votre terminal :

    git clone https://github.com/Benoitrenou/projet_13.git

## Création de l'environnement virtuel

Pour créer un environnement virtuel, depuis votre terminal de commande, effectuez les commandes suivantes :

### Sous Linux/ MAC OS

    $ python -m venv <environment_name>
    exemple : python -m venv venv
    
### Sous Windows:
    
    $ virtualenv <environment_name>
    exemple : virtualenv venv 
    
## Activation de l'environnement virtuel 

### Sous Linux / MAC OS:

    $ source <environment_name>/bin/activate
    exemple : source venv/bin/activate
   
### Sous Windows:

    $ source <environment_name>/Scripts/activate
    exemple : source venv/Scripts/activate
    
## Installation des packages : 

Afin que les packages nécessaires au fonctionnement de l'application soient installés sur l'environnement virtuel, entrez la commande suivante :

    $ pip install -r requirements.txt

## Lancement de l'application

Enfin pour lancer l'application, dans le terminal depuis le répertoire du projet :

    $ python manage.py runserver
    
Le site sera ensuite disponible à l'adresse suivante : http://localhost:8000/

## Lancer les tests et linting

Pour générer un rapport Flake8, placez vous dans le dossier racine du projet et utilisez la commande :

    $ flake8

Les conditions de linting sont précisées dans le fichier `setup.cfg`

Pour lancer les tests unitaires, placez vous dans le dossier racine du projet et utilisez la commande :

    $ pytest

Les paramètres de pytest sont précisés dans le fichier `setup.cfg`

Les paramètres de couverture de tests sont précisés dans le fichier `.coveragerc`

# Déploiement

Pour le déploiement de cette application, nous allons mettre en place un pipeline de développement et intégration continus via CircleCi

Ce pipeline permettra, à chaque mise à jour, de :
- Mettre à jour automatiquement le projet à chaque push sur GitHub
- Analyser le projet an automatisant les tests unitaires et de linting
- Dockeriser l'environnement de déploiement de l'application
- Déployer l'application sur Heroku
- Suivre les erreurs et la performance via Sentry

Pour mettre en place ce pipeline, vous devez disposer de compte sur les applications suivantes :
- GitHb
- CircleCi
- Docker Hub
- Heroku
- Sentry

## CircleCi

Pour lier le projet à CircleCi, vous devez avoir préalablement lié votre compte GitHub à votre compte CircleCi lors de sa création

Ensuite, allez dans l'onglet `Projects` de CircleCi et cliquez sur `Set Up Project` correspondant au repository de votre choix

En cas de difficultés, suivez les indications données sur https://circleci.com/docs/2.0/getting-started/

### Variables d'environnement

Depuis le `Dashboard` de CircleCi, accédez aux `Project Settings` de votre project puis à l'onglet `Environment Variables`

Sur cette page, vous devez ajouter les variables suivantes :

|   Nom des Variable à ajouter  |   Obtention   |
|---    |---    |
|   DOCKERHUB_TOKEN   |   https://hub.docker.com/settings/security -> `New Access Token`   |
|   DOCKERHUB_USERNAME   |   Votre username sur Docker  |
|   HEROKU_TOKEN   |   Via cmd `heroku auth:token`   |
|   SECRET_KEY   |   Secret Key Django   |
|   SENTRY_TOKEN   |   https://sentry.io/settings/ -> `Projects` -> Sélectionnez le projet correspondant -> `Client Keys (DSN)`   |

Une fois le pipeline mis en place, chaque push GitHub lancera le job `build_test`

Seuls les push sur la brance `main` lanceront les jobs `deploy_docker` et ensuite `deploy_heroku`

Vous pourrez une fois les jobs validés, accéder à l'application sur https://oc-lettings2022.herokuapp.com/


