from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.views import View
from .filters import VideoFilter


def videos(request):
    context = {}
    filter_object = VideoFilter(request.GET, Video.objects.all())
    context["filter_object"] = filter_object

    return render(
        request,
        'videos.html',
        context
    )


def video(request, id):
    # 7
    # SELECT * FROM video_video WHERE id = 7;
    video_object = Video.objects.get(id=id)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse('Вы не авторизованы', status=401)
    try:
        video_object = Video.objects.get(id=id)
    except:
        return HttpResponse("Не найдено", status=404)
    context = {}
    if request.user.is_authenticated:
        video_view, created = VideoView.objects.get_or_create(
            user=request.user,
            video=video_object,
        )
        if request.method == 'POST':
            if "txt" in request.POST:
                comment_form = CommentForm(request.POST)
                if comment_form.is_valid():
                    comment = comment_form.save(commit=False) # ещё нет записи в БД
                    comment.user = request.user
                    comment.video = video_object
                    comment.save() # сохраняем в БД
                    messages.success(request, 'Комментарий успешно добавлен.')
                    return redirect(video, id=video_object.id)
                else:
                    messages.error(request, 'Ошибка! Данные не валидны')
            elif "like" in request.POST:
                video_object.likes += 1
                video_object.save()
                return redirect(video, id=video_object.id)
            elif "dislike" in request.POST:
                video_object.dislike.add(request.user)
                video_object.save()
            elif "dislike_r" in request.POST:
                video_object.dislike.remove(request.user)
                video_object.save()
            else:
                messages.error(request, 'Ошибка! Данные не валидны')

    context = {
        "video": video_object,
        "comment_form": CommentForm(),

    }
    return render(request, 'video.html', context)

def video_add(request):
    if request.method == "GET":
        return render(request, 'video_add.html')
    elif request.method == "POST":
        name = request.POST["video_name"]
        video_file = request.FILES["video_file"]
        video_object = Video(
            name=name,
            file_path=video_file,
            author=request.user
        )
        # video_object.description = "hello world"
        # INSERT INTO ...
        video_object.save()
        return redirect(video, id=video_object.id)

# def video_update(request, id):
#     video_object = Video.objects.get(id=id)
#     context = {"video": video_object}

#     if request.method == "POST":
#         name = request.POST["video_name"]
#         video_object.name = name
#         video_object.save()
#         return redirect(video, id=video_object.id)

#     return render(request, 'video_update.html', context)

class VideoUpdate(View):
    # read
    def get(self, request, *args, **kwargs):
        context = {}
        video_object = Video.objects.get(id=kwargs.get("pk"))
        video_form = VideoForm(
            instance=video_object,
            )
        context["video_form"] = video_form
        return render(request, "video_update.html", context)

    # update
    def post(self, request, *args, **kwargs):
        video_object = Video.objects.get(id=kwargs.get("pk"))
        if request.user == video_object.author:
            video_form = VideoForm(
                instance=video_object,
                data=request.POST,
                files=request.FILES,
            )
            if video_form.is_valid():
                video_form.save()
                messages.success(request, "Видео обновлено")
                return redirect("video-update-cbv", pk=video_object.id)
            else:
                return HttpResponse("Данные не валидны", status=400)
        else:
            return HttpResponse("Нет доступа", status=403)

def video_delete(request, id):
    video_object = Video.objects.get(id=id)
    video_object.delete()
    return redirect(videos)

def video_df_add(request):
    context = {}
    if request.method == "POST":
        video_form = VideoForm(request.POST,request.FILES)
        # video_author = Video(
        #     author=request.user
        # )
        if video_form.is_valid():
            video_object = video_form.save()
            return redirect(video, id=video_object.id)

    video_form = VideoForm()
    context["video_form"] = video_form
    return render(request, "video_df_add.html", context)