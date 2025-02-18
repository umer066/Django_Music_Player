# Generated by Django 5.1.5 on 2025-02-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="audio_link",
            field=models.CharField(blank=True, default=" ", max_length=200),
        ),
        migrations.AlterField(
            model_name="song",
            name="image",
            field=models.ImageField(upload_to=None, verbose_name=""),
        ),
        migrations.AlterField(
            model_name="song",
            name="lyrics",
            field=models.TextField(blank=True, default=" "),
        ),
        migrations.AlterField(
            model_name="song",
            name="singer",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="song",
            name="title",
            field=models.CharField(max_length=50),
        ),
    ]
