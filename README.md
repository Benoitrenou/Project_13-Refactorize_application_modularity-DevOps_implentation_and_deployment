In this scenario, the modularity of the application built via Django from OCL, a real estate agency, must first be reworked to go from one to three applications. 

The database migrations must be customized so as not to lose any data during this refactoring

This work can be studied in the migration files of the applications oc_lettings_site, lettings and profiles

The rest of the scenario deals with Dev Ops work with the implementation of a CI/CD pipeline, the containerization of the project, and the deployment of the application

Objectives of project:
  - Refactorize an application and its database
  - Implement Dev Ops tools CI/CD, Docker, deployment

## Create virtual environment

From your terminal, enter the following commands depending on your operating system

### With Linux/ MAC OS

    $ python -m venv <environment_name>
    example : python -m venv venvOCL
    
### With Windows:
    
    $ virtualenv <environment_name>
    example : virtualenv venvOCL 
    
## Activate virtual environment

### With Linux / MAC OS:

    $ source <environment_name>/bin/activate
    example : source venvOCL/bin/activate
   
### With Windows:

    $ source <environment_name>/Scripts/activate
    example : source venvOCL/Scripts/activate
    
## Installation of packages : 

    $ pip install -r requirements.txt

## Launch application

    $ python manage.py runserver

## Launch tests and linting

To generate a Flake8 report, go to the root folder of the project and use in the terminal the command :

    $ flake8

The linting conditions are specified in the `setup.cfg` file

To launch the unit tests, go to the root folder of the project and use the command :

    $ pytest

The pytest parameters are specified in the `setup.cfg` file

Test coverage parameters are specified in the `.coveragerc` file

# Deployment

For the deployment of this application, we will set up a continuous development and integration pipeline via CircleCi

This pipeline will, with each update, allow to:
  - Automatically update the project with each push on GitHub
  - Analyze the project by automatizing the unit tests and linting
  - Dockerize the application deployment environment
  - Deploy the application on Heroku
  - Monitor errors and performance via Sentry

To set up this pipeline, you must have accounts on the following applications:
  - GitHb
  - CircleCi
  - Docker Hub
  - Heroku
  - Sentry

## CircleCi

To link the project to CircleCi, you must have linked your GitHub account to your CircleCi account when you created it

Then go to the `Projects` tab in CircleCi and click on `Set Up Project` corresponding to the repository of your choice

In case of difficulties, follow the instructions given on https://circleci.com/docs/2.0/getting-started/

### Environment variables

From the CircleCi `Dashboard`, go to the `Project Settings` of your project and then to the `Environment Variables` tab

On this page you need to add the following variables:

|   Name of the Variable to add  |   Obtaining   |
|---    |---    |
|   DOCKERHUB_TOKEN   |   https://hub.docker.com/settings/security -> `New Access Token`   |
|   DOCKERHUB_USERNAME   |   Your username on Docker  |
|   HEROKU_TOKEN   |   Via cmd `heroku auth:token`   |
|   SECRET_KEY   |   Secret Key Django   |
|   SENTRY_TOKEN   |   https://sentry.io/settings/ -> `Projects` -> Select the corresponding project -> `Client Keys (DSN)`   |

Once the pipeline is set up, each GitHub push will launch the `build_test` job

Only the pushes on the `main` branch will launch the `deploy_docker` and then `deploy_heroku` jobs

Once the jobs are validated, you can access the application on https://oc-lettings2022.herokuapp.com/