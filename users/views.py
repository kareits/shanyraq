from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)
from django.views.generic.edit import FormMixin

from .forms import CustomUserChangeForm


CustomUser = get_user_model()


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """View to retrieve information about user."""

    model = CustomUser
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        """Get object based on the username in URL."""
        username = self.kwargs.get('username')
        if not self.model.objects.filter(username=username).exists():
            return None
        return self.model.objects.get(username=username)

    def dispatch(self, request, *args, **kwargs):
        """Authorize client."""
        if self.get_object() != self.request.user:
            return redirect(reverse('restaurant:index'))
        return super().dispatch(request, *args, **kwargs)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """View to update user profile."""

    model = CustomUser
    template_name = 'users/profile_update.html'
    form_class = CustomUserChangeForm

    def get_object(self, queryset=None):
        """Get object based on the username in URL."""
        username = self.kwargs.get('username')
        if not self.model.objects.filter(username=username).exists():
            return None
        return self.model.objects.get(username=username)

    def dispatch(self, request, *args, **kwargs):
        """Authorize client."""
        if self.get_object() != self.request.user:
            return redirect(reverse('restaurant:index'))
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        """Redirects to updated profile."""
        return reverse(
            'users:profile', kwargs={'username': self.kwargs.get('username')}
        )
