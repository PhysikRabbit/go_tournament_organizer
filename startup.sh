#!/bin/bash

project_name=goTournamentOrganizer
app_name=organizer

#for first startup
if [! -d $project_name]; then
  django-admin startproject $project_name
fi

#always
python $project_name/manage.py runserver

#for first startup
if [! -d $project_name/$app_name]; then
  cd $project_name
  python manage.py startapp $app_name
fi