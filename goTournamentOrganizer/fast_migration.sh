#!/bin/bash

#use this script for applying new changes of the model to the database
python manage.py makemigrations
python manage.py migrate