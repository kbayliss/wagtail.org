# Generated by Django 3.2.16 on 2022-10-14 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menusnippetlink",
            name="link_page",
        ),
        migrations.RemoveField(
            model_name="menusnippetlink",
            name="snippet",
        ),
        migrations.DeleteModel(
            name="LinkGroupLink",
        ),
        migrations.DeleteModel(
            name="LinkGroupSnippet",
        ),
        migrations.DeleteModel(
            name="MenuSnippet",
        ),
        migrations.DeleteModel(
            name="MenuSnippetLink",
        ),
    ]