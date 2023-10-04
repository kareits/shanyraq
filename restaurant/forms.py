from datetime import datetime

from django import forms
from django.utils import timezone

from .models import Reservation
from .validators import datetime_validator


class ReservationForm(forms.ModelForm):
    """Form to make reservation."""

    class Meta:
        model = Reservation
        fields = ('date_time', 'party_size',)
        widgets = {
            'date_time': forms.DateInput(attrs={
                'type': 'datetime-local',
                'format': '%Y-%m-%dT%H:%M'
            }),
        }

    def clean_date_time(self):
        """Validates date and time for reservation."""
        date_time = self.cleaned_data.get('date_time')
        datetime_validator(date_time)
        return date_time
