from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'currency', 'balance', 'is_staff', 'is_active',)
    list_filter = ('email', 'currency', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'currency', 'balance', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'currency', 'balance', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    """
    Курсы валют
    """
    list_display = [field.name for field in Currency._meta.fields]  # все поля выводит в цикле
    search_fields = ["cur_name"]
    list_filter = ["cur_name", "data_update"]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """ Типы вопросов """
    list_display = [field.name for field in Transaction._meta.fields]  # все поля выводит в цикле
    search_fields = ["user"]
    list_filter = ["user", "currency", "balance", "destination"]
