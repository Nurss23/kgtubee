from django.shortcuts import render, redirect #HttpResponse
from video.models import Video
from .forms import *
from django.contrib.auth.models import User
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