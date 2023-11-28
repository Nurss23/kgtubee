from django.test import TestCase
from django.urls import reverse_lazy

# Create your tests here.

class TestHomepage(TestCase):
    def test_open_homepage_should_success(self):
        # response = self.client.get("/")
        response = self.client.get(reverse_lazy("home"))
        assert response.status_code == 200

class TestAboutpage(TestCase):
    def test_open_aboutpage_should_success(self):
        response = self.client.get("/about/")
        assert response.status_code == 200

class TestTeampage(TestCase):
    def test_open_teampage_should_success(self):
        response = self.client.get("/team/")
        assert response.status_code == 200

class TestPlaylistspage(TestCase):
    def test_open_playlists_page_should_success(self):
        response = self.client.get("/playlists/")
        assert response.status_code == 200