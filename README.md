# SHANYRAQ


## Description
Shanyraq is a web application for a restaurant called "Shanyraq", which translates to "the top of a traditional house of nomads." This project was created as part of the final assignment for 'CS50 Introduction to Computer Science.'


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
