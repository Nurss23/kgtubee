from django.shortcuts import render
from .models import UserPlayList

# Create your views here.
def playlists(request):
    # SELECT * FROM UserPlayList;
    query_result = UserPlayList.objects.all()

    # query_result является списком 
    context = {"objects_list": query_result}

    return render(
        request,
        'playlists.html',
        context
    )

def playlist(request, id):
    playlist_object = UserPlayList.objects.get(id=id)
    return render(request, 'playlist.html', {"playlists": playlist_object})