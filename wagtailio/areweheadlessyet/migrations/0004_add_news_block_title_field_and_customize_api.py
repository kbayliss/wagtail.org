# Generated by Django 3.2.8 on 2022-02-08 12:57

from django.db import migrations

import wagtail.blocks
import wagtail.fields

import wagtailio.areweheadlessyet.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("areweheadlessyet", "0003_add_issue_model_and_section"),
    ]

    operations = [
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
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "blog_posts",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "blog_post",
                                                wagtailio.areweheadlessyet.blocks.BlogPostChooserBlock(
                                                    page_type=["blog.BlogPage"]
                                                ),
                                            )
                                        ]
                                    ),
                                ),
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
                                                wagtailio.areweheadlessyet.blocks.IssueChooserBlock(
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
        migrations.AlterField(
            model_name="areweheadlessyettopicpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("text", wagtail.blocks.RichTextBlock()),
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
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "blog_posts",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "blog_post",
                                                wagtailio.areweheadlessyet.blocks.BlogPostChooserBlock(
                                                    page_type=["blog.BlogPage"]
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