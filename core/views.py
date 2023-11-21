from django.shortcuts import render, HttpResponse, redirect
from video.models import Video
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages
# Create your views here.

def homepage(request):
    # return  HttpResponse("hello world")
    return render(request, "home.html")

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def team_view(request):
    return render(request, 'team.html')

def search(request):
    key_word = request.GET["key_word"]
    # SELECT * FROM Video WHERE name LIKE '%key_word%'
    videos_query = Video.objects.filter(name__contains=key_word)
    context = {"videos_list": videos_query}
    return render(request, "videos.html", context)

def profile_create_df(request):
    context = {}

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            user = request.user
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(homepage)

    profile_form = ProfileForm()
    context["profile_form"] = profile_form
    return render(request, "profile_create_df.html", context)

def profile_detail(request, id):
    profile_object = Profile.objects.get(id=id)
    return render(
        request,
        'profile.html',
        {"profile_object": profile_object}
    )

def profile_update(request, id):
    context = {}
    profile_object = Profile.objects.get(id=id)
    if request.user == profile_object.user:
        if request.method == "POST":
            profile_form = ProfileForm(
                instance=profile_object,
                data=request.POST
            )
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, "Профиль успешно обновлён!")
                return redirect(profile_detail, id=profile_object.id)

        profile_form = ProfileForm(instance=profile_object)
        context["profile_form"] = profile_form
        return render(request, "profile_update.html", context)
    else:
        return HttpResponse("Нет доступа")
    
def profile_delete(request, id):
    profile_object = Profile.objects.get(id=id)
    if request.user == profile_object.user:
        context = {"profile_object": profile_object}
        if request.method == "POST":
            profile_object.delete()
            return redirect(homepage)
        return render(request, "profile_delete.html", context)
    else:
        return HttpResponse("Нет доступа")