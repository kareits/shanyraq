import json
import re
from datetime import timedelta
from typing import Any


from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.db.models import Count, Q
from django.db.models.query import QuerySet
from django.forms import ValidationError
from django.http import Http404, JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)
from django.views.generic.edit import FormMixin

from .forms import ReservationForm
from .mixins import SharedReservationMixin
from .models import Dish, Category, Reservation, Table


CustomUser = get_user_model()


class DishListView(ListView):
    """Shows dishes on Homepage."""

    model = Dish
    template_name = 'restaurant/index.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        return Dish.objects.select_related('category',).filter(
            is_served=True,
            on_homepage=True,
        )


class CategoryListView(ListView):
    """Shows dishes by category."""

    model = Dish
    template_name = 'restaurant/category.html'
    context_object_name = 'category_dishes'

    def get_queryset(self):
        """Filters dishes by category."""
        self.category_slug = self.kwargs.get('category_slug')
        return Dish.objects.select_related('category',).filter(
            is_served=True,
            category=self.category_slug,
        )

    def get_context_data(self, **kwargs):
        """Adds category into context dictionary."""
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.category_slug)
        context['category'] = category.title
        return context


class DishDetailView(DeleteView):
    """Shows details of a dish."""

    model = Dish
    template_name = 'restaurant/dish_detail.html'
    context_object_name = 'dish'


class ReservationListView(LoginRequiredMixin, ListView):
    """View to show and create reservations."""

    model = Reservation
    template_name = 'restaurant/reservation.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        """Filters reservations for a guest."""
        user_id = self.request.user.id
        queryset = (
            self.model.objects.select_related('customer', 'table',).filter(
                customer_id=user_id,
                date_time__gte=timezone.now(),
            ).exclude(status='canceled',)
        )
        return queryset


class ReservationCreateView(SharedReservationMixin, CreateView):
    """View to make reservation."""

    pass


class ReservationUpdateView(SharedReservationMixin, UpdateView):
    """Updates reservation."""

    def dispatch(self, request, *args, **kwargs):
        """
        Verifies that the user in the request
        is the customer in reservation being updated.
        """
        if self.get_object().customer != self.request.user:
            return redirect(reverse('restaurant:reservation'))
        return super().dispatch(request, *args, **kwargs)


def get_categories(reqeust):
    """Retrieves the list of categories and converts it into json."""
    queryset = Category.objects.all()
    categories = list(queryset.values())
    return JsonResponse(categories, safe=False)
