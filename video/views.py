from django.shortcuts import render
from .models import Video

# Create your views here.
# def video(request):
#     query_result = Video.objects.all()

#     context = {"objects_list": query_result}

#     return render(
#         request,
#         'videos.html',
#         context
#     )

def videos(request):
    videos_list = Video.objects.all()
    context = {"videos_list": videos_list}
    return render(request, 'videos.html', context)


def video(request, id):
    video_object = Video.objects.get(id=id)
    return render(request, 'video.html', {"video": video_object})