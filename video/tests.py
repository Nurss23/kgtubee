from django.test import TestCase
from django.urls import reverse_lazy
from .models import Video
from .factories import *

# Create your tests here.
class TestVideoDetail(TestCase):
    def test_one_video_page_should_success(self):
        video_object = Video.objects.create(
            file_path="/static/video/test_video.mp4",
            name="test video 1"
        )
        response = self.client.get(f'/video/{video_object.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, video_object.name)
    def test_one_video_via_factory_boy(self):
        video_object = VideoFactory()
        response = self.client.get(f'/video/{video_object.id}/')
        # print(video_object.name)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, video_object.name)

class TestVideoList(TestCase):
    def test_video_list_should_success(self):
        for i in range(3):
            video_obj = VideoFactory(name=f"test video number {i}")

        profile = ProfileFactory(
            user=video_obj.author
        )

        response = self.client.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test video number 0")
        self.assertContains(response, "test video number 1")
        self.assertContains(response, "test video number 2")

# class TestCommentVideo(TestCase):
#     def test_comment_video_page_should_success(self):
#         comment_object = Video.objects.create(
#             video="/static/video/test_video.mp4",
#             txt = "test comment 1"
#             user = 
#         )
#         response = self.client.get(f'/video/{comment_object.id}/')
#         self.assertEqual(response.status_code, 200)