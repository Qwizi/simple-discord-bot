# Generated by Django 5.0.6 on 2024-05-10 10:20

import django.db.models.deletion
import prefix_id.field
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("guilds", "0004_remove_guild_members"),
    ]

    operations = [
        migrations.CreateModel(
            name="Embed",
            fields=[
                (
                    "id",
                    prefix_id.field.PrefixIDField(
                        editable=False,
                        max_length=28,
                        prefix="embed",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("color", models.CharField(blank=True, max_length=255, null=True)),
                ("footer", models.CharField(blank=True, max_length=255, null=True)),
                ("image", models.CharField(blank=True, max_length=255, null=True)),
                ("thumbnail", models.CharField(blank=True, max_length=255, null=True)),
                ("author", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="EmbedField",
            fields=[
                (
                    "id",
                    prefix_id.field.PrefixIDField(
                        editable=False,
                        max_length=34,
                        prefix="embed_field",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("value", models.CharField(blank=True, max_length=255, null=True)),
                ("inline", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name="guild",
            name="embed",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="guilds.embed",
            ),
        ),
        migrations.AddField(
            model_name="embed",
            name="fields",
            field=models.ManyToManyField(blank=True, to="guilds.embedfield"),
        ),
    ]