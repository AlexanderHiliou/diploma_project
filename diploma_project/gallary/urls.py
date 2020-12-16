from django.urls import path
from . import views


urlpatterns = [
    path('', views.countries_gallery, name='countries_gallery'),
    path('<int:id>/', views.cities, name='cities'),
]