from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm


CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    """Customized User Admin."""

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('id', 'username', 'email', 'phone',)
    list_editable = ('email', 'phone',)
    list_display_links = ('username',)
    fieldsets = [
        (None, {'fields': [
            'username', 'email', 'password',
        ]}),
        ('Personal Info', {'fields': ['first_name', 'last_name', 'phone']}),
        ('Permissions', {'fields': ['is_staff', 'is_superuser']}),
    ]
    search_fields = ['username']
    ordering = ['username']
    filter_horizontal = []
    add_fieldsets = (
        (None, {
            'fields': ('username', 'phone', 'password1', 'password2',),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
