# Generated by Django 4.2.4 on 2024-05-22 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0004_project_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={"ordering": ["-vote_ratio", "-vote_total", "title"]},
        ),
    ]