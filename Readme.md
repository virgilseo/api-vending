# Vending Machine API

Vending machine API, MPV code challenge.

## Table of Contents
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Authorization](#authorization)
* [Django_Rest](#django_rest)

## Prerequisites

 - Anaconda: https://www.anaconda.com/
   - manage your virtual environments and packages

## Installation

1. Open the Anaconda terminal and run this command to create a virtual environment:
```
conda create -n api_vending python=3.10
```
Next, you need to activate your virtual env:
```
conda activate api_vending
```
After the env is activatedrun this command:
```
git clone https://github.com/virgilseo/api-vending.git
```
Next, cd into the folder and run this command to install the required packages:
```
pip install -r requirements.txt
```
After this you need to migrate your tables:
```
python manage.py migrate
```
Create admin user:
```
python manage.py createsuperuser
```
Create a local_settings.py file @ root and add these values:
```
ALLOWED_HOSTS = ['localhost']

DEBUG = True
SECURE_SSL_REDIRECT = False

```

Set the SECRET_KEY env variable for django.

Run the app:
```
python manage.py runserver
```
App available @ localhost:8000

## Authorization
JWt authorization is implemented for this app's users.

Using the SIMPLE JWT package: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

The token claim has been updated to include user details: username , role and deposit were added.

## Django_Rest

Django Rest Framework is used to build the Web Rest API.

 - https://www.django-rest-framework.org/


