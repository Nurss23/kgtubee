from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.views.generic import ListView

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

class PlayListView(ListView):
    model = UserPlayList 

def playlist_add(request):
    if request.method == "POST":
        # request.POST - это словарь
        name = request.POST["playlist_name"] # str 
        description = request.POST["description"] # str
        # print(request.POST)
        # print(name)
        # INSERT INTO UserPlayList ...
        # playlist_object = UserPlayList.objects.create(
        playlist_object = UserPlayList(
            name=name,
            description=description,
            owner=request.user
        )
        playlist_object.save()
        return redirect(playlist_info, id=playlist_object.id)
    
    return render(request, "playlist_add.html")
    
def playlist_info(request, id):
    playlist_object = UserPlayList.objects.get(id=id)
    context = {"playlist_object": playlist_object}
    return render(request, "playlist_info.html", context)

def playlist_df_add(request):
    context = {}
    if request.method == "POST":
        # код создания playlist 

        # создаём объект формы с значениями
        playlist_form = PlayListForm(request.POST)
        # проверка валидности
        if playlist_form.is_valid():
            # создаём запись в БД
            playlist_object = playlist_form.save()
            return redirect(playlist_info, id=playlist_object.id)

    playlist_form = PlayListForm()
    context["playlist_form"] = playlist_form
    return render(request, "playlist_df_add.html", context)

# def playlist_update(request, id):
#     playlist_object = UserPlayList.objects.get(id=id)
#     context = {"playlist": playlist_object}

#     if request.method == "POST":
#         name = request.POST["playlist_name"]
#         # description = request.POST["description"] # str
#         playlist_object.name = name
#         playlist_object.save()
#         return redirect(playlist_info, id=playlist_object.id)
 
#     return render(request, "playlist_update.html", context)

def playlist_update_df(request, id):
    context = {}
    playlist_object = UserPlayList.objects.get(id=id)
    if request.user == playlist_object.owner:
        if request.method == "POST":
            playlist_form = PlayListForm(
                instance=playlist_object,
                data=request.POST
            )
            if playlist_form.is_valid():
                playlist_form.save()
                messages.success(request, "Плейлист успешно обновлён!")
                return redirect(playlist_info, id=playlist_object.id)
            
        playlist_form = PlayListForm(instance=playlist_object)
        context["playlist_form"] = playlist_form
        return render(request, "playlist_update_df.html", context)
    else:
        return HttpResponse("Нет доступа")

def playlist_delete(request, id):
    playlist_object = UserPlayList.objects.get(id=id)
    if request.user == playlist_object.owner:
        context = {"playlist_object": playlist_object}
        if request.method == "POST":
            playlist_object.delete()
            return redirect(playlists)
        return render(request, "playlist_delete.html", context)
    else:
        return HttpResponse("Нет доступа")
    
# def playlist_delete(request, id):
#     playlist_object = UserPlayList.objects.get(id=id)
#     playlist_object.delete()
#     return redirect(playlists)