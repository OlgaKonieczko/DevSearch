# Generated by Django 4.2.5 on 2023-09-19 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "projects",
            "0002_tag_project_value_ratio_project_value_total_review_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="value_ratio",
            new_name="vote_ratio",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="value_total",
            new_name="vote_total",
        ),
    ]
