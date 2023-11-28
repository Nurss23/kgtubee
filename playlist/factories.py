import factory
# from django.contrib.auth.models import User
from .models import UserPlayList
from video.factories import UserFactory

class PlaylistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserPlayList

    name = factory.Sequence(lambda n: f"Test playlist {n}")
    description = factory.Sequence(lambda n: f"Test description {n}")
    # videos_qty = factory.Sequence(lambda n: n)
    # views_qty = factory.Sequence(lambda n: n)
    # owner = factory.SubFactory(UserFactory)