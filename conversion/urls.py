from django.urls import path
from .views import CurrencyListView, CurrencyDetailView, CustomUserListView, \
    CustomUserDetailView, SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('currencies/<int:pk>', CurrencyDetailView.as_view(), name='currency-detail'),
    path('currencies/', CurrencyListView.as_view(), name='currency-list'),
    path('customusers/<int:pk>', CustomUserDetailView.as_view(), name='custom-user-detail'),
    path('customusers/', CustomUserListView.as_view(), name='custom-user-list'),
]
