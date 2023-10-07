# SHANYRAQ


## Description
Shanyraq is a web application for a restaurant called "Shanyraq", which translates to "the top of a traditional house of nomads." This project was created as part of the final assignment for 'CS50 Introduction to Computer Science.'


## Project Structure
shanyraq_project/
├── media/
│   └── dishes                # Contains images for dish entries in Dish model
├── restaurant/               # Restaurant application
│   ├── management
│   │   └── commands
│   │       └── import_data   # Script for Django Management command to import sample data, if database is empty. Run `python manage.py import_data`
│   ├── migrations/           # Database migration files.
│   │   └── ...               # Auto-generated migration files.
│   ├── __init__.py           # Initialization file for the restaurant app.
│   ├── admin.py              # Admin panel configurations.
│   ├── apps.py               # App configuration.
│   ├── forms.py              # Forms for restaurant application views.
│   ├── mixins.py             # View class mixin for restaurant views.
│   ├── models.py             # Define database models for the restaurant app.
│   ├── urls.py               # URL routing for restaurant app.
│   ├── validators.py         # Validators for forms and models.
│   └── views.py              # Define views and view functions for the restaurant app.
├── sent_emails/              # Auto-generated folder for storing emails sent by Django emain backend
├── shanyraq/                 # Main project
│   ├── __init__.py
│   ├── asgi.py               # ASGI configuration for deployment.
│   ├── settings.py           # Project-wide settings and configurations.
│   ├── urls.py               # URL routing for the project.
│   └── wsgi.py               # ASGI configuration for deployment.
├── static/                   # Directory for static files (CSS, images, etc.)
│   ├── css/
│   │   └── styles.css        # Custom css settings
│   ├── csv_fiels/            # .csv files to import sample data into database
│   │   └── ...
│   └── img/
│       └── fav/              # Favicon icons
│       └── ...               # Images for background and logo
├── templates/
│   ├── errors/               # Folder with custom templates for error pages
│   ├── includes/             # Folder with include parts for templates (e.g. footer, header)
│   ├── registration/         # Folder with templates for login, logout, registration, password change, password reset, etc.
│   ├── restaurant/           # Folder with templates for restaurant app
│   ├── users/                # Folder with templates for users app (profile details and profile update)
│   ├── base.html             # Base template that other templates can extend.
├── users/                    # Users application
│   ├── management
│   │   └── commands
│   │       └── createadminuser.py   # Script to create a user with admin rights. Run `python manage.py createadminuser`
│   ├── __init__.py
│   ├── admin.py              # Admin panel configurations of CustomUser model.
│   ├── apps.py               # App configuration.
│   ├── forms.py              # Forms for Users views.
│   ├── models.py             # Define database models for the Users app.
│   ├── urls.py               # URL routing for Users app.
│   └── views.py              # Define views and view functions for the restaurant app.
├── .gitignore                # File with list of objects preventing them from sending to GitHub repository
├── db.sqlite3                # Database of the project
├── manage.py                 # Django management script for various tasks.
└── requirements.txt          # List of required Python packages and their versions.


## How to Launch the Application:

1. Clone repository:
```
git clone git@github.com:kareits/shanyraq.git
```

2. Create and activate virtual environment:
```
source venv/Scripts/activate
```
3. Navigate to the folder with the project:
```
cd shanyraq

```
4. Install dependencies from requirements.txt:
```
pip install -r requirements.txt
```

5. Make migrations and create tables in the database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

6. Assuming database is empty, download sample data from .csv files:
```
python manage.py import_data
```

7. Ensure that all dish pictures are present in the shanyraq/media/ folder; otherwise, they will not display correctly.

8. Create a superuser for administering the website:
```
python manage.py createsuperuser
```

9. Create an admin user to gain access to all actions associated with the Restaurant model:
```
python manage.py createadminuser
```

Launch the project:
```
python3 manage.py runserver
```


## Main Functionality

- The homepage displays several dishes with the attribute `on_homepage = True.`
- Users can access menu categories through the navigation bar, which redirects them to lists of dishes grouped by the selected category.
- Detailed information about a dish can be obtained by clicking on its image.
- Anonymous users can sign up and access personal profile management functionalities:
  - Change password
  - Update personal information
  - Reset the password if forgotten
- Logged-in users can book tables in the restaurant via the Reservation menu. According to the implemented logic:
  - Guests can book only one table on the same day.
  - Tables are booked based on availability, depending on the party size.
  - Reservations placed have a 'pending' status until an administrator changes it to 'confirmed' from the admin panel.
- Logged-in users can manage their reservations by changing or canceling them.
- In the admin panel, users with 'admin' role (i.e., `is_staff = True`) have all permissions for the Restaurant model, allowing them to perform all actions related to Menu categories, Tables, Dishes, and Reservations. They also have view permission for the CustomUser model, allowing them to view user information.


## Technology Stack

- Framework: Django
- Frontend: HTML, CSS, JavaScript


## Disclaimer

> All images used in this project were obtained from publicly accessible sources on the Internet and are used solely for educational and non-commercial purposes. If you are the copyright owner of any images used and have concerns about their usage, please contact me at kareits@gmail.com.
