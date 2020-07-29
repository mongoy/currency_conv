from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Currency, CustomUser


class CurrencyListView(ListView):
    """ Список видов валюты """
    model = Currency
    request = Currency.objects.all()
    template_name = 'conversion/currency_list.html'
    paginate_by = 5


class CurrencyDetailView(DetailView):
    """
    Валюта
    """
    model = Currency

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            return context
        else:
            return Currency.objects.none()


class CustomUserListView(ListView):
    """ Список клиентов """
    model = CustomUser
    request = CustomUser.objects.all()
    template_name = 'conversion/custom_user_list.html'


class CustomUserDetailView(DetailView):
    """
    Клиент
    """
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            return context
        else:
            return CustomUser.objects.none()

