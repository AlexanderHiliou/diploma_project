from django.shortcuts import render, get_object_or_404
from .models import Country, City, ArticlePreview, ArticleText


def get_countries(request):
    countries = Country.objects.all()
    content = {'title': 'Countries list', 'countries': countries}
    return render(request, 'countries.html', content)


def country_details(request, id):
    articles = ArticlePreview.objects.all()[:5]
    country = Country.objects.filter(country=id)
    content = {'country': country, 'articles': articles}
    return render(request, 'country_detail.html', content)


def article_detail(request, id):
    articles = ArticleText.objects.filter(article=id)
    articles_name = ArticlePreview.objects.filter(article=id)
    content = {'articles': articles, 'articles_name': articles_name}
    return render(request, 'article_detail.html', content)

