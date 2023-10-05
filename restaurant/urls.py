from django.urls import include, path

from .views import (
    DishListView,
    CategoryListView,
    DishDetailView,
    ReservationListView,
    ReservationCreateView,
    ReservationUpdateView,
    cancel_reservation,
    get_categories,
)


app_name = 'restaurant'
reservation_urls = [
    path('', ReservationListView.as_view(), name='reservation'),
    path(
        'create/',
        ReservationCreateView.as_view(),
        name='reservation_create',
    ),
    path(
        '<int:pk>/update/',
        ReservationUpdateView.as_view(),
        name='reservation_update',
    ),
    path('<int:pk>/cancel/', cancel_reservation, name='reservation_cancel',),
]
urlpatterns = [
    path('', DishListView.as_view(), name='index'),
    path(
        'category/<slug:category_slug>/',
        CategoryListView.as_view(),
        name='category'
    ),
    path('categories/', get_categories, name='categories'),
    path('dishes/<int:pk>', DishDetailView.as_view(), name='dish_detail'),
    path('reservation/', include(reservation_urls)),
]
