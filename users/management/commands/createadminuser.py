from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.core.validators import EmailValidator
from phonenumber_field.validators import validate_international_phonenumber


CustomUser = get_user_model()


class Command(BaseCommand):
    """Creates Django management comand to create admin user."""

    help = 'Creates a user with is_staff=True '
    'and assigns to admin_users group.'

    def handle(self, *args, **kwargs):
        # Prompt for username and validate it
        while True:
            username = input('Enter username: ')
            username_validator = UnicodeUsernameValidator()
            try:
                username_validator(username)
            except ValidationError as e:
                self.stderr.write(self.style.ERROR(f'Invalid username: {e}'))
            else:
                if CustomUser.objects.filter(username=username).exists():
                    self.stderr.write(self.style.ERROR(
                        f'User with this username already exists: {username}'
                    ))
                else:
                    break
        # Prompt for email and validate it
        while True:
            email = input('Enter email: ')
            email_validator = EmailValidator()
            try:
                email_validator(email)
            except ValidationError as e:
                self.stderr.write(self.style.ERROR(f'Invalid email: {e}'))
            else:
                if CustomUser.objects.filter(email=email).exists():
                    self.stderr.write(self.style.ERROR(
                        f'User with this email already exists: {email}'
                    ))
                else:
                    break
        # Prompt for password and validate it
        while True:
            password1 = input('Enter password: ')
            try:
                validate_password(password1)
            except ValidationError as e:
                self.stderr.write(self.style.ERROR(f'Invalid password: {e}'))
            else:
                password2 = input('Repeat password: ')
                if password1 != password2:
                    self.stderr.write(self.style.ERROR(
                        'Passwords do not match.'
                    ))
                else:
                    password = make_password(password1)
                    break
        # Prompt for phone number and validate it
        while True:
            phone = input('Enter phone: ')
            try:
                validate_international_phonenumber(phone)
            except ValidationError:
                self.stderr.write(self.style.ERROR(
                    'Enter a valid phone number (e.g. (201) 555-0123)'
                    ' or a number with an international call prefix.'
                    )
                )
            else:
                if CustomUser.objects.filter(phone=phone).exists():
                    self.stderr.write(self.style.ERROR(
                        f'User with this phone already exists: {phone}'
                    ))
                else:
                    break
        # Create user
        user = CustomUser.objects.create(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            phone=phone,
        )
        # Get or create the admin_users group
        # and assign permissions to this group: all permissions
        # for Restaurant model and view permission to CustomUser model
        admin_users_group, created = Group.objects.get_or_create(
            name='admin_users'
        )
        restaurant_app = apps.get_app_config('restaurant')
        for model in restaurant_app.get_models():
            permissions = Permission.objects.filter(
                content_type__app_label=model._meta.app_label
            )
            for permission in permissions:
                admin_users_group.permissions.add(permission)
        view_permission = Permission.objects.get(
            content_type__app_label=CustomUser._meta.app_label,
            codename='view_customuser'
        )
        admin_users_group.permissions.add(view_permission)
        # Add user to the admin_group
        user.groups.add(admin_users_group)
        self.stdout.write(self.style.SUCCESS(
            'Admin user created and assigned to admin_users group.'
        ))
