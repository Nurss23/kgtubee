# Generated by Django 4.2.7 on 2023-11-26 17:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('playlist', '0002_userplaylist_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=65, null=True)),
                ('description', models.TextField(blank=True, db_index=True, null=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Shorts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='shorts/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_by', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(blank=True, to='shorts.category', verbose_name='Категория')),
                ('dislike', models.ManyToManyField(blank=True, related_name='shorts_dislikes', to=settings.AUTH_USER_MODEL, verbose_name='Дизлайки')),
                ('like', models.ManyToManyField(blank=True, related_name='shorts_likes', to=settings.AUTH_USER_MODEL, verbose_name='Лайки')),
                ('playlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='playlist.userplaylist')),
            ],
        ),
        migrations.CreateModel(
            name='ShComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.TextField(verbose_name='Текст комментария')),
                ('created_by', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.DateTimeField(auto_now=True, null=True)),
                ('shorts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shorts.shorts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_view', models.TimeField(auto_now_add=True, null=True)),
                ('end_view', models.TimeField(auto_now=True, null=True)),
                ('shorts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shorts.shorts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Просмотр',
                'verbose_name_plural': 'Просмотры',
                'unique_together': {('shorts', 'user')},
            },
        ),
    ]