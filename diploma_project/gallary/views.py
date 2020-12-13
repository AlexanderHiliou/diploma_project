from django.shortcuts import render
from .models import Gallary
from countries_cities.models import Country, City



def countries(request):
    countries = Country.objects.all()
    context = {'countries': countries}
    return render(request, 'gallery.html', context)


def cities(request, id):
    cities = City.objects.filter(country=id)
    content = {'cities': cities}
    return render(request, 'cities.html', content)