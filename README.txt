Virtual Env
--------------------------------
pip install pipenv

Django Project
-------------------------------
cd desktop
mkdir myproject
cd myproject
pipenv install Django

activating virtual environment
---------------------------------
pipenv shell

starting new project 
---------------------------------
django-admin startproject storefront .

server
---------------------------------
python manage.py runserver

setting terminal
---------------------------------
Ctrl + C
pipenv --venv
#paste the path of the python version of your venv into the python: interpretor from the view->command palette
#and run the server again from the vscode terminal cmd not PS

creating and registrating an app
--------------------------------
python manage.py startapp playground
#type 'playground' into the INSTALLED_APPS in settings.py

making a request (views.py)
----------------------------
from django.http import HttpResponse
#create say_hello function that displays hello world

mapping URL to views
-------------------------------
#create 'urls.py' inside the app, 'playground' and open it
from django.urls import path
from . import views
#create an array called 'urlpatterns' and pass in its views arguments
#move inside urls.py of storefront
from django.urls import path, include
#specify the path and url in the URLConf

Run HTML in browser
-------------------------
http://127.0.0.1:8000/playground/hello/

templates
-------------------------------
#create a folder inside app called 'templates' 
#create 'hello.html' within the folder
#create a function that returns render in the views.py to display html content from the template

Debugging
-----------------------
#launch.json
#under the runserver, append '9000' as a new port number
#add a breakpoint and run debug
#access url .../playground/htmlhello/ to navigate through debug

addding a debugging tool
--------------------------------
pipenv install django-debug-toolbar
#include 'debug_toolbar' in INSTALLED_APPS, settings.py
path ('__debug__/', include('debug_toolbar.urls')) #into urls.py of storefront
'debug_toolbar.middleware.DebugToolbarMiddleware' #type into MIDDLEWARE of settings.py
#paste code below into the settings.py
INTERNAL_IPS = [
    #...
    '127.0.0.1',
    #...
]
#the toolbar can be accessed with an official html file