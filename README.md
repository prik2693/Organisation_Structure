# Organisation_Structure
Organisation Structure is a web application which shows the organisation hierarchy of the logged in user and on input of organisation id gives out a tree structure of the organisation.
Organisation 1

|________Team 1

| |________Team 2

| | |________Repo 1

| |________ Team 3

| | |________Repo 2

| | |________ Repo 11

| |________Team 4

| |________Repo 3

getOrgDetails.py - API which takes organisation Id(through AJAX) from frontend as input and returns a JSON object representing the structure of organisation and its teams and their repos.
getUserOrg.py - API that would return the repos, teams and organizations the logged-in/authenticated user is associated with.(here assuming the logged in userid = 1)
Databse dump - org_struct.sql

For Database, I have used "PostgresSQL","AngularJs" for frontend,"Python" and "Flask" on the server side.
I have set up the "uWSGI" application server to launch the application and "Nginx" to act as a front end reverse proxy.
Install uwsgi with - pip install uwsgi 
Command to start the uwsgi server :- uwsgi --ini organisation.ini,the logs are stored in organisation.log
Install nginx server with nginx.conf file provided.
