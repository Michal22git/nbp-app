from django.urls import path

from .views import HomeView, GoldView, CurrenciesView

app_name = 'nbp'

urlpatterns = [
    path('', HomeView.as_view(), name='home-view'),
    path('gold/', GoldView.as_view(), name='gold-view'),
    path('currencies/', CurrenciesView.as_view(), name='currencies-view')
]
