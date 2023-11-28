from django.test import TestCase
from django.urls import reverse_lazy
from .models import UserPlayList

# Create your tests here.


class TestPlaylistInfo(TestCase):
    def test_one_playlist_page_should_success(self):
        playlist_object = UserPlayList.objects.create(
            name="test playlist 1"
        )
        response = self.client.get(f'/playlist/{playlist_object.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, playlist_object.name)
