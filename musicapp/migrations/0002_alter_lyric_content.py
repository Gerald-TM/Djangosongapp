# Generated by Django 4.1.2 on 2022-11-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("musicapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lyric", name="content", field=models.TextField(max_length=3000),
        ),
    ]
