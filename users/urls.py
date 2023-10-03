from django.urls import path

from .views import ProfileDetailView, ProfileUpdateView


app_name = 'users'


urlpatterns = [
    path('<str:username>/', ProfileDetailView.as_view(), name='profile'),
    path(
        'edit/<str:username>/', ProfileUpdateView.as_view(),
        name='edit_profile'
    ),
]
