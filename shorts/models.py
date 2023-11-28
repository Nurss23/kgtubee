from django.db import models
from django.contrib.auth.models import User
from playlist.models import UserPlayList
# from core.models import Profile
from django.core.validators import FileExtensionValidator 
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=65, db_index=True)
    description = models.TextField(db_index=True,blank=True,null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    # ordering = [F('category').asc(nulls_last=True)]

    def __str__(self):
        return self.name
    
class Shorts(models.Model):
    file_path = models.FileField(
        upload_to="shorts/",
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    name = models.CharField(max_length=60)
    description = models.TextField(null=True)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    playlist = models.ForeignKey(
        to=UserPlayList,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    like = models.ManyToManyField(
        to=User,
        related_name="shorts_likes",
        verbose_name="Лайки",
        blank=True
    )
    dislike = models.ManyToManyField(
        to=User,
        related_name="shorts_dislikes",
        verbose_name="Дизлайки",
        blank=True
    )
    category = models.ManyToManyField(
        to=Category,
        verbose_name = 'Категория',
        blank=True
    )
    
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True,blank=True, null=True)
    # updated_by = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    
class ShComment(models.Model):
    txt = models.TextField(verbose_name="Текст комментария")
    shorts = models.ForeignKey(
        to=Shorts,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True,blank=True, null=True)
    # updated_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.txt[:30]
    
class ShortsView(models.Model):
    shorts = models.ForeignKey(
        to=Shorts,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    created_by = models.DateTimeField(auto_now_add=True)
    # start_v = models.TimeField(auto_now_add=True)
    # end_v = models.TimeField(auto_now=True)

    class Meta:
        verbose_name = "Просмотр"
        verbose_name_plural = "Просмотры"
        unique_together = [["shorts", "user"]]

    # class CheckConstraint