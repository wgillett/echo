from django.test.client import Client
from django.test import TestCase

from nest.models import Artist


class ArtistTest(TestCase):
    fixtures = ['artists.json']

    def test_create_artist(self):
        artist = Artist(name='Gaga')
        artist.save()
        self.assertEqual(artist.name, 'Gaga')

    def test_artists_list_view(self):
        c = Client()
        response = c.get('/artists/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artists/index.html')
        for artist in response.context['artists']:
            self.assertContains(response, artist.name, count=1)

