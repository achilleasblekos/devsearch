# Generated by Django 4.2.4 on 2024-05-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_auto_20240517_1256"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="featured_image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to=""
            ),
        ),
    ]
