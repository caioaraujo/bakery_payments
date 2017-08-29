# bakery_payments

This Django API project uses django-rest-framework and django rest swagger.
After checkout the project, run "python manage.py makemigrations" then "python manage.py migrate"
from a terminal in project's root folder to migrate models into a SQLite database.
Then, run "python manage.py runserver" to start a local webserver.

You will be able to interact with the endpoints inside of Swagger documentation. If you are running locally, please
access http://localhost:"your port"/docs and start using the API.

Allowed endpoints:
/docs (GET)
/branches (POST)
/payment (GET,POST,PUT,DELETE)
/pay (POST)
