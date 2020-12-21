from django.urls import path
from . import views


urlpatterns = [
    path('', views.cour_view, name='gallery'),
    path('<int:id>/', views.cities, name='cities'),
]