from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Currency


class CurrencyListView(ListView):
    """ Список видов валюты """
    model = Currency
    request = Currency.objects.all()
    template_name = 'conversion/currency_list.html'
