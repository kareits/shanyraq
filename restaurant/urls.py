from django.urls import include, path

from .views import (
    DishListView,
    CategoryListView,
    DishDetailView,
    ReservationListView,
    ReservationCreateView,
    ReservationUpdateView,
    get_categories,
)


app_name = 'restaurant'

urlpatterns = [
    path('', DishListView.as_view(), name='index'),
    path(
        'category/<slug:category_slug>/',
        CategoryListView.as_view(),
        name='category'
    ),
    path('categories/', get_categories, name='categories'),
    path('dishes/<int:pk>', DishDetailView.as_view(), name='dish_detail'),
    path(
        'reservation/',
        ReservationListView.as_view(),
        name='reservation'
    ),
    path(
        'reservation/create/',
        ReservationCreateView.as_view(),
        name='reservation_create',
    ),
    path(
        'reservation/<int:pk>/update/',
        ReservationUpdateView.as_view(),
        name='reservation_update',
    ),
    path(
        'reservation/<int:pk>/cancel/',
        ReservationUpdateView.as_view(),
        name='reservation_cancel',
    ),
]
