# Generated by Django 4.2.6 on 2024-01-09 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_likes_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='color',
            field=models.BooleanField(default=False),
        ),
    ]
