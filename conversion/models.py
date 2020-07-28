from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager


class Currency(models.Model):
    """
    Курсы валют
    """
    cur_name = models.CharField(default='RUB', max_length=3, unique=True, db_index=True,
                                verbose_name='Наименование валюты')
    curs = models.FloatField(default=0, verbose_name='Курс валюты')
    data_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.cur_name

    class Meta:
        """Вид в админке"""
        verbose_name = "Курс валюты"
        verbose_name_plural = "Курсы валют"
        ordering = ['cur_name']


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Настройка модели пользователя
    _('...') - ДАННАЯ СТРОКА ТРЕБУЕТ ПЕРЕВОДА НА ЯЗЫК ТЕКУЩЕГО ПОЛЬЗОВАТЕЛЯ
    """
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    currency = models.ForeignKey(Currency, default=1, on_delete=models.PROTECT, verbose_name='Наименование валюты')
    balance = models.FloatField(_('balance'), default=100)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()
    # авторизация по этому полю
    USERNAME_FIELD = 'email'
    # это список полей, которые будут обязательны для создания пользователя
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        """Вид в админке"""
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Transaction(models.Model):
    """
    Журнал транзакций
    """
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Пользователь')
    currency = models.ForeignKey(Currency, default=1, on_delete=models.PROTECT, verbose_name='Наименование валюты')
    balance = models.FloatField(default=0, verbose_name='Остаток валюты на счёте')
    destination = models.CharField(max_length=15, default='Открытие счёта', verbose_name='Назначение')
    data_transfer = models.DateTimeField(auto_now_add=True, verbose_name='Дата проведения')

    class Meta:
        """Вид в админке"""
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
