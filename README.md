# Restaurant Finder [![Build Status](https://travis-ci.org/dawidbudzynski/restaurant_finder_python_django.svg?branch=master)](https://travis-ci.org/dawidbudzynski/restaurant_finder_python_django)

## General info
A web application made using Python 3, Django 2, Bootstrap and REST API.
Application converts address provided by user to coordinates using Google Geocoding API.
Then taking coordinates application displays information about nearby restaurants using Zomato API. 

## Main functions
* displaying details about nearby restaurants
* displaying maps using Google API

## Technologies
* Python 3
* Django 2.0
* REST API
* Bootstrap 4

## Setup
To run this project:
1. Rename settings.ini.example to settings.ini and fill required fields. 
2. Install required libraries using pip:
    ```
    $ pip install -r requirements.txt
    ```
3. Apply migrations: 
    ```
    $ python manage.py migrate
    ```
4. To run your local server use command: 
    ```
    $ python manage.py runserver
    ```

## Demo
## https://restaurantfinderdjango.herokuapp.com

![alt text](https://raw.githubusercontent.com/dawidbudzynski/restaurant_finder_python_django/master/examples/example_1.png)
![alt text](https://raw.githubusercontent.com/dawidbudzynski/restaurant_finder_python_django/master/examples/example_2.png)
![alt text](https://raw.githubusercontent.com/dawidbudzynski/restaurant_finder_python_django/master/examples/example_3.png)
