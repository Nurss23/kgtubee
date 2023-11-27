from django import forms
from .models import *


# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name', 'file_path']

class ShortsForm(forms.ModelForm):
    class Meta:
        model = Shorts
        fields = ['name', 'file_path','description']

class ShCommentForm(forms.ModelForm):
    class Meta:
        model = ShComment
        fields = ['txt']