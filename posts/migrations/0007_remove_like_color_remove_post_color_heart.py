# Generated by Django 4.2.6 on 2024-01-11 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_color_heart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='color',
        ),
        migrations.RemoveField(
            model_name='post',
            name='color_heart',
        ),
    ]