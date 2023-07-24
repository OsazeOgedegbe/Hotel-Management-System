# Hotel-Management-System
A fullstack Hotel Management System made with Django.

The first page is an interface where guests can view some information about the hotel, register/signup and login (superuser login details will lead to admin interface).

Some Fuctionalities of Guest Interface:
* Guest can make, update and cancel reservations (guest will be able to know if and when a room is available)
* Guest can view details of their reservations
* Guest can require for extra services such as airport pickup and drop off
* Guest can message admin and vice versa

Some Functionalities of Admin Interface:
* Admin can create, read, update, and delete guest account
* Admin can view all the rooms, make reservations (overwrites any conflicting guest reservation) and cancel reserved rooms.
* Admin can message guests

## Setting up the project
You can install all the requirements needed to run the project by running this command on your terminal:

pip install -r requirements.txt

### Superuser Details:
* username: admin
* password: qweds12345

You can create a new superuser by running this command on your terminal:

python manage.py createsuperuser
