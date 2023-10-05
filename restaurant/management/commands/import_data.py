"""
This module creates sample data for Shanyraq project
"""

import os
import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from restaurant.models import Category, Dish, Table


class Command(BaseCommand):
    """Downloading sample data from .csv files into database."""

    help = 'This module downloads sample data from .csv file into database.'
    csv_files_model_mapping = {
        'category.csv': Category,
        'dish.csv': Dish,
        'table.csv': Table,
    }

    def handle(self, *args, **options):
        """Importing data from .csv files."""
        csv_files = []
        for filename in self.csv_files_model_mapping:
            csv_files.append(
                (
                    os.path.join(settings.CSV_FILES_PATH, filename),
                    self.csv_files_model_mapping[filename]
                )
            )
        for csv_file, model in csv_files:
            self.stdout.write(
                self.style.WARNING(f'Importing data from: {csv_file}')
            )
            self.import_csv_data(csv_file, model)

    def import_csv_data(self, csv_file, model):
        """Reading from .csv and saving data into database models."""
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file, delimiter=';', dialect='excel')
            for row in reader:
                model(**row).save()
        self.stdout.write(self.style.SUCCESS(
            f'Successfully saved data from: {csv_file}'
        ))
