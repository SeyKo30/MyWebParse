from django.shortcuts import render
from .rss_feed import fetch_rss_feed


def index(request):
    rss_url = 'https://www.thesun.my/rss/world'
    articles = fetch_rss_feed(rss_url)
    return render(request, 'CoreApplication/index.html', {'articles': articles})


def help(request):
    return render(request, 'CoreApplication/help.html')
