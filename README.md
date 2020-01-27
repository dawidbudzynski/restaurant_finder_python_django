# Restaurant Finder [![Build Status](https://travis-ci.org/dawidbudzynski/restaurant_finder_python_django.svg?branch=v1.0)](https://travis-ci.org/dawidbudzynski/restaurant_finder_python_django)

## General info
A web application made using Python 3, Django 2, React, Redux, REST API and Semantic UI.
Application converts address provided by user to coordinates using Google Geocoding API.
Then taking coordinates application displays information about nearby restaurants using Zomato API. 

## Main functions
* displaying details about nearby restaurants
* displaying maps using Google API

## Technologies
* Python 3
* Django 2.0
* React
* Redux
* REST API
* Semantic UI

## Setup
To run this project:
1. Rename settings.ini.example to settings.ini and fill required fields. 
2. Start docker containers with command:
    ```
    $ docker-compose up
    ```
 3. Application is available on port 3000
     ```
     http://localhost:3000/
     ```

## Demo
## https://restaurantfinderdjango.herokuapp.com

![alt text](https://raw.githubusercontent.com/dawidbudzynski/restaurant_finder_python_django/master/backend/examples/example_1.png)
![alt text](https://raw.githubusercontent.com/dawidbudzynski/restaurant_finder_python_django/master/backend/examples/example_2.png)
![alt text](https://raw.githubusercontent.com/dawidbudzynski/restaurant_finder_python_django/master/backend/examples/example_3.png)
