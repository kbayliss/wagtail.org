# Generated by Django 1.9.8 on 2016-12-01 14:50

from django.db import migrations


# We need to remove all feature pages before deleting FeaturePage model
# to cleanup the wagtailcore_page table
# Will be great to run ./manage.py fixtree
def remove_feature_pages(apps, schema_editor):
    FeaturePage = apps.get_model("features", "FeaturePage")

    FeaturePage.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailredirects", "0005_capitalizeverbose"),
        ("wagtailcore", "0030_index_on_pagerevision_created_at"),
        ("wagtailforms", "0003_capitalizeverbose"),
        ("features", "0005_featureaspect_video_url"),
    ]

    operations = [
        migrations.RunPython(remove_feature_pages),
    ]
