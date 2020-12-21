from django.shortcuts import render
from .models import Gallary
from countries_cities.models import Country, City



def countries_gallery(request):
    countries = Country.objects.all()
    context = {'countries': countries}
    return render(request, 'portfolio.html', context)


def cities(request, id):
    cities = City.objects.filter(country=id)
    content = {'cities': cities}
    return render(request, 'cities.html', content)



def cour_view(request):
    gallery = Gallary.objects.all()
    last = Gallary.objects.all()[4]
    content = {'gallery': gallery, 'last': last}
    return render(request, 'portfolio.html', content)