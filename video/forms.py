from django import forms
from .models import *


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'file_path','description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['txt']