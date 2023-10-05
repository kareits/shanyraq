from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from phonenumber_field.formfields import PhoneNumberField


CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """Custom User Creation Form."""

    phone = PhoneNumberField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone',)


class CustomUserChangeForm(UserChangeForm):
    """Custom User Change Form."""

    phone = PhoneNumberField()

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone',)
