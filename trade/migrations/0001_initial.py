# Generated by Django 3.2.19 on 2023-06-15 14:27

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('excerpt', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('likes', models.ManyToManyField(blank=True, related_name='blog_likes', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='trade.listing')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
