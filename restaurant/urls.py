from django.urls import include, path

from .views import DishListView, CategoryListView, DishDetailView, get_categories


app_name = 'restaurant'

urlpatterns = [
    path('', DishListView.as_view(), name='index'),
    path(
        'category/<slug:category_slug>/',
        CategoryListView.as_view(),
        name='category'
    ),
    path('categories/', get_categories, name='categories'),
    path('dishes/<int:pk>', DishDetailView.as_view(), name='dish_detail')
]
