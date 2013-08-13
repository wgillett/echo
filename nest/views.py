from django.http import Http404
from django.shortcuts import render
import os

from nest.models import Artist

def index(request):
    artists = Artist.objects.all()
    context = {'artists': artists,
               'echo_nest_api_key': os.environ['ECHO_NEST_API_KEY']}
    return render(request, 'artists/index.html', context)

def detail(request, artist_id):
    try:
        artist = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        raise Http404
    return render(request, 'artists/detail.html', {'artist': artist})
