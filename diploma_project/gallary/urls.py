from django.urls import path
from . import views


urlpatterns = [
    path('', views.countries, name='countries'),
    path('<int:id>/', views.cities, name='cities'),
]