from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


CustomUser = get_user_model()


class Category(models.Model):
    """Category of dishes."""

    title = models.CharField(
        max_length=settings.MAX_LENGTH,
        verbose_name='Menu category',
    )
    slug = models.SlugField(unique=True, verbose_name='Shortcut',)

    class Meta:
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'

    def __str__(self):
        return self.title


class Dish(models.Model):
    """Dishes in menu."""

    name = models.CharField(
        max_length=settings.MAX_LENGTH,
    )
    description_short = models.TextField(verbose_name='Short description')
    description = models.TextField(verbose_name='Description')
    category = models.ForeignKey(
        Category,
        to_field='slug',
        null=True,
        on_delete=models.SET_NULL,
        related_name='dishes',
    )
    image = models.ImageField(
        upload_to='dishes/',
        null=True,
        blank=True,
    )
    price = models.FloatField(
        verbose_name='Price',
        validators=[
            MinValueValidator(
                settings.MIN_PRICE,
                message=f'Minimum price is {settings.MIN_PRICE}'
            ),
            MaxValueValidator(
                settings.MAX_PRICE,
                message=f'Maximum price is {settings.MAX_PRICE}'
            )
        ],
    )
    is_served = models.BooleanField(
        verbose_name='Is served',
    )
    on_homepage = models.BooleanField(
        verbose_name='Is on the homepage',
        default=False,
    )

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Table(models.Model):
    """Tables in restaurant."""

    table_number = models.IntegerField(
        verbose_name='Table number',
        unique=True,
    )
    capacity = models.IntegerField(
        verbose_name='Number of seats available at the table',
        validators=[
            MinValueValidator(
                settings.MIN_NUMBER_OF_SEATS,
                message=f'Minimum number of seats is '
                        f'{settings.MIN_NUMBER_OF_SEATS}'
            ),
            MaxValueValidator(
                settings.MAX_NUMBER_OF_SEATS,
                message=f'Maximum number of seats is '
                        f'{settings.MAX_NUMBER_OF_SEATS}'
            )
        ],
    )
    is_active = models.BooleanField(
        verbose_name='Is active',
    )

    def __str__(self):
        return str(self.table_number)


class Reservation(models.Model):
    """Reservations made by customers."""

    customer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reservations',
        verbose_name='Guest',
    )
    date = models.DateTimeField(
        verbose_name='Date and time of reservation',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date and time of creation',
    )
    party_size = models.IntegerField(
        verbose_name='Number of guests',
        default=1,
        validators=[
            MinValueValidator(
                settings.MIN_NUMBER_OF_SEATS,
                message=f'Minimum number of guests is '
                        f'{settings.MIN_NUMBER_OF_SEATS}'
            ),
            MaxValueValidator(
                settings.MAX_NUMBER_OF_SEATS,
                message=f'Maximum number of guests is '
                        f'{settings.MAX_NUMBER_OF_SEATS}'
            ),
        ]
    )
    table = models.ForeignKey(
        Table,
        on_delete=models.SET_NULL,
        null=True,
        related_name='reservations',
        verbose_name='Table for reservation',
    )
    status = models.CharField(
        max_length=settings.MAX_LENGTH,
        choices=settings.RESERVATION_STATUS,
        default='pending',
    )

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
        ordering = ('-date', '-created_at',)
