from django.contrib import admin
from django.conf import settings

from restaurant.models import Category, Dish, Table, Reservation


@admin.display(description='short description')
def short_text(obj):
    """Trancate description."""
    return (obj.description_short[:settings.SHORT_LENGTH])


class DishAdmin(admin.ModelAdmin):
    """Settings for Dish model in admin zone."""

    list_display = (
        'name', short_text, 'category', 'price', 'is_served', 'on_homepage',
    )
    list_editable = ('price', 'is_served', 'on_homepage',)
    search_fields = ('name',)
    list_filter = ('category',)
    list_display_links = ('name',)
    list_per_page = settings.LIST_PER_PAGE
    ordering = ('pk',)


class CategoryAdmin(admin.ModelAdmin):
    """Settings for Category model in admin zone."""

    list_display = (
        'pk', 'title', 'slug',
    )

    list_display_links = ('title',)
    ordering = ('pk',)


class TableAdmin(admin.ModelAdmin):
    """Settings for Table mode in admin zone."""

    list_display = ('table_number', 'capacity', 'is_active')
    list_editable = ('is_active',)
    ordering = ('table_number',)


class ReservationAdmin(admin.ModelAdmin):
    """"Settings for Reservation model in admin zone."""

    list_display = (
        'customer', 'date', 'party_size', 'table', 'status', 'created_at',
    )
    list_editable = ('date', 'table', 'status',)
    search_fields = ('customer',)
    list_filter = ('customer',)
    list_display_links = ('customer',)
    list_per_page = settings.LIST_PER_PAGE
    ordering = ('date',)


admin.site.register(Dish, DishAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Reservation, ReservationAdmin)
