import factory
from django.contrib.auth.models import User
from .models import UserPlayList


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = 'test_user_1'


class VideoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserPlayList

    name = factory.Sequence(lambda n: f"Test playlist {n}")
    owner = factory.SubFactory(UserFactory)