from django.shortcuts import render, get_object_or_404
from .models import Country, City


def get_countries(request):
    countries = Country.objects.all()
    content = {'title': 'Countries list', 'countries': countries}
    return render(request, 'countries.html', content)


def country_details(request, id):
    details = City.objects.filter(country=id)
    content = {'details': details}
    return render(request, 'country_detail.html', content)