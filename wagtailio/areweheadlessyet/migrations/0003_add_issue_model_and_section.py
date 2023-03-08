# Generated by Django 3.2.8 on 2022-01-27 10:27

from django.db import migrations, models

import wagtail.blocks
import wagtail.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("areweheadlessyet", "0002_add_topic_page_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="WagtailHeadlessIssue",
            fields=[
                (
                    "number",
                    models.PositiveIntegerField(primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name="areweheadlessyethomepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "section",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "content",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "text",
                                                wagtail.blocks.RichTextBlock(),
                                            ),
                                            (
                                                "link_group",
                                                wagtail.blocks.StreamBlock(
                                                    [
                                                        (
                                                            "link",
                                                            wagtail.blocks.StructBlock(
                                                                [
                                                                    (
                                                                        "link",
                                                                        wagtail.blocks.URLBlock(
                                                                            required=True
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "link_text",
                                                                        wagtail.blocks.CharBlock(
                                                                            required=True
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                        )
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "news",
                        wagtail.blocks.StreamBlock(
                            [
                                (
                                    "blog_post",
                                    wagtail.blocks.PageChooserBlock(
                                        page_type=["blog.BlogPage"]
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "topics",
                        wagtail.blocks.StructBlock(
                            [("title", wagtail.blocks.CharBlock())]
                        ),
                    ),
                    (
                        "issues",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "summary",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "issues",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "issue",
                                                wagtail.snippets.blocks.SnippetChooserBlock(
                                                    "areweheadlessyet.WagtailHeadlessIssue"
                                                ),
                                            )
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        ),
    ]