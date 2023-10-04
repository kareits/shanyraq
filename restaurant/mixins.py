from datetime import timedelta


# from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.urls import reverse

from .forms import ReservationForm
from .models import Reservation, Table


# CustomUser = get_user_model()


class SharedReservationMixin(LoginRequiredMixin):
    """View to make reservation."""

    model = Reservation
    template_name = 'restaurant/reservation_create.html'
    form_class = ReservationForm

    def form_valid(self, form):
        """Checks availability of the table for reservation."""
        requested_datetime = form.cleaned_data.get('date_time')
        id = self.kwargs.get('pk')
        # Checks if user has already made reservation in the same date
        if id:
            active_reservations = Reservation.objects.filter(
                customer=self.request.user,
                date_time__date=requested_datetime.date()
            ).exclude(id=id)
        else:
            active_reservations = Reservation.objects.filter(
                customer=self.request.user,
                date_time__date=requested_datetime.date()
            )
        if active_reservations:
            form.add_error(
                None,
                'We appologize, you cannot make more than one reservation '
                'for the same date. Please choose another date.'
            )
            return self.form_invalid(form)
        # Finds table for reservation
        requested_datetime = form.cleaned_data.get('date_time')
        party_size = form.cleaned_data.get('party_size')
        tables_suitable = Table.objects.values('id').filter(
            is_active=True, capacity__range=(
                party_size, party_size + settings.EMPTY_SEATS
            )
        ).order_by('capacity')
        tables_suitable_ids = [item['id'] for item in tables_suitable]
        tables_reserved = Reservation.objects.values('table_id').filter(
            status='confirmed',
            date_time__lte=requested_datetime+timedelta(
                hours=settings.RESERVE_HOURS_RANGE
            ),
            date_time__gte=requested_datetime-timedelta(
                hours=settings.RESERVE_HOURS_RANGE
            ),
        )
        tables_reserved_ids = [item['table_id'] for item in tables_reserved]
        tables_available = [
            item for item in tables_suitable_ids
            if item not in tables_reserved_ids
        ]
        if not tables_available:
            form.add_error(
                None,
                'We appologize, there are no tables available for the date '
                'and time specified in your request. '
                'Please try another date or company size.'
            )
            return self.form_invalid(form)
        form.instance.table_id = tables_available[0]
        form.instance.customer = self.request.user
        form.instance.status = 'pending'
        return super().form_valid(form)

    def get_success_url(self):
        """Defines the redirect url in case of successful reservation."""
        return reverse('restaurant:reservation')
