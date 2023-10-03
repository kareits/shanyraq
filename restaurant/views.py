import json
import re
from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.db.models.query import QuerySet
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)
from django.views.generic.edit import FormMixin

# from .forms import CommentForm, PostsForm, ProfileForm
# from .mixins import PostListMixin, SharedCommentMixin, SharedPostViewMixin
from .models import Dish, Category


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

    def get_context_data(self, **kwargs: Any):
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


def get_categories(request):
    """Retrieves the list of categories and converts it into json."""
    queryset = Category.objects.all()
    categories = list(queryset.values())
    return JsonResponse(categories, safe=False)
