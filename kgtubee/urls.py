"""
URL configuration for kgtubee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *
from playlist.views import *
from video.views import *
from shorts.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('about/', about_view),
    path('contacts/', contacts_view),
    path('our_team/', team_view),
    path('search/', search, name='search'), # from core.views import search
    path('playlists/', playlists),
    path('videos/', videos),
    path('video/<int:id>/',video),
    path('playlist/<int:id>/', playlist_info, name='playlist-info'),
    path('video-add/', video_add, name='video-add'),
    path('playlist-add/', playlist_add, name ='playlist-add'),
    path('video-update/<int:id>/', video_update, name='video-update'),
    path('video-delete/<int:id>/', video_delete, name='video-delete'),
    path('playlist-update/<int:id>/', playlist_update_df, name='playlist-update-df'),
    path('playlist-delete/<int:id>/', playlist_delete, name='playlist-delete'),
    path('playlist-df/add/', playlist_df_add, name='playlist-df-add'),
    path('video-df/add/', video_df_add, name='video-df-add'),
    path('profile-create/', profile_create, name='profile-create'),
    path('profile-detail/<int:id>/', profile_detail, name='profile-detail'),
    path('profile-update/<int:id>/', profile_update, name='profile-update'),
    path('profile-delete/<int:id>/', profile_delete, name='profile-delete'),
    # path('subscriber-add/<int:id>/', subscriber_add, name='subscriber-add'),
    # path('subscriber-remove/<int:id>/', subscriber_remove, name='subscriber-remove'),
    path("registration/", registration, name="registration"),
    path('sign-in/', sign_in, name="sign-in"),
    path('sign-out/', sign_out, name="sign-out"),
    path('shorts-create/', shorts_create, name='shorts-create'),
    path('shorts-detail/<int:id>/', shorts, name='shorts-detail'),
    path('shorts-update/<int:id>/', shorts_update, name='shorts-update'),
    path('shorts-delete/<int:id>/', shorts_delete, name='shorts-delete'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)