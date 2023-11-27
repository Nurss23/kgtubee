from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def all_shorts(request):
    shorts_list = Shorts.objects.all()
    context = {"shorts_list": shorts_list}
    return render(request, 'shorts/shorts_list.html', context)

def shorts(request, id):
    shorts_object = Shorts.objects.get(id=id)
    context = {}
    if request.user.is_authenticated:
        shorts_view, created = ShortsView.objects.get_or_create(
            user=request.user,
            shorts=shorts_object,
        )
        if request.method == 'POST':
            if "txt" in request.POST:
                comment_form = ShCommentForm(request.POST)
                if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.user = request.user
                    comment.shorts = shorts_object
                    comment.save()
                    messages.success(request, 'Комментарий успешно добавлен.')
                    return redirect(shorts, id=shorts_object.id)
                else:
                    messages.error(request, 'Ошибка! Данные не валидны')
            elif "like" in request.POST:
                shorts_object.dislike.add(request.user)
                shorts_object.save()
                return redirect(shorts, id=shorts_object.id)
            elif "like_r" in request.POST:
                shorts_object.like.remove(request.user)
                shorts_object.save()
            elif "dislike" in request.POST:
                shorts_object.dislike.add(request.user)
                shorts_object.save()
            elif "dislike_r" in request.POST:
                shorts_object.dislike.remove(request.user)
                shorts_object.save()
            else:
                messages.error(request, 'Ошибка! Данные не валидны')

    context = {
        "shorts": shorts_object,
        "shcomment_form": ShCommentForm(),

    }
    return render(request, 'shorts/shorts.html', context)

def shorts_create(request):
    context = {}
    if request.method == "POST":
        shorts_form = ShortsForm(request.POST,request.FILES)
        if shorts_form.is_valid():
            shorts_object = shorts_form.save(commit=False)
            shorts_object.author = request.user
            shorts_object.save()
            # return redirect(shorts, id=shorts_object.id)
            return redirect(all_shorts)

    shorts_form = ShortsForm()
    context["shorts_form"] = shorts_form
    return render(request, "shorts/shorts_create.html", context)

def shorts_update(request, id):
    context = {}
    shorts_object = Shorts.objects.get(id=id)
    if request.user == shorts_object.author:
        if request.method == "POST":
            shorts_form = ShortsForm(
                instance=shorts_object,
                data=request.POST
            )
            if shorts_form.is_valid():
                shorts_form.save()
                messages.success(request, "Шортс успешно обновлён!")
                return redirect(shorts, id=shorts_object.id)
            
        shorts_form = ShortsForm(instance=shorts_object)
        context["shorts_form"] = shorts_form
        return render(request, "shorts/shorts_update.html", context)
    else:
        return HttpResponse("Нет доступа")

def shorts_delete(request, id):
    shorts_object = Shorts.objects.get(id=id)
    if request.user == shorts_object.author:
        context = {"shorts_object": shorts_object}
        if request.method == "POST":
            shorts_object.delete()
            return redirect(all_shorts)
        return render(request, "shorts/shorts_delete.html", context)
    else:
        return HttpResponse("Нет доступа")