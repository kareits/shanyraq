# Generated by Django 3.2.16 on 2023-10-04 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_alter_dish_on_homepage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ('date', '-created_at'), 'verbose_name': 'Reservation', 'verbose_name_plural': 'Reservations'},
        ),
    ]