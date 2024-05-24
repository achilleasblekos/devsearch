# Generated by Django 4.2.4 on 2024-05-21 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
        ("projects", "0003_project_featured_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
        ),
    ]