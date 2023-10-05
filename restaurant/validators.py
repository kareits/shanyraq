from datetime import time

from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone


def datetime_validator(value):
    """Validates date and hours for reservation."""
    request_time = value.time()
    start_time = settings.WORKING_HOURS_START
    end_time = settings.WORKING_HOURS_END
    start_time_datetime = time.fromisoformat(start_time)
    end_time_datetime = time.fromisoformat(end_time)
    if not (start_time_datetime <= request_time <= end_time_datetime):
        raise ValidationError(
            ('We appologize, our hours for reservation are ({} - {}).').format(
                start_time, end_time
            ),
            code='not working time'
        )
    if value < timezone.now():
        raise ValidationError(
            'The reservation date and time cannot be in the past.')


def table_free_validator(value, instance):
    """Validates availability of a table."""
    pass
