# Generated by Django 4.2.16 on 2024-12-07 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habits",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="название привычки",
                        max_length=20,
                        verbose_name="название",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="активная привычка",
                        verbose_name="активно",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="время создания привычки",
                        null=True,
                        verbose_name="время",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="время последнего обновления",
                        null=True,
                        verbose_name="время обновления",
                    ),
                ),
                (
                    "count",
                    models.SmallIntegerField(
                        default=1,
                        help_text="сколько раз нужно выполнить привычку за день",
                        verbose_name="число выполнений",
                    ),
                ),
                (
                    "day_count",
                    models.SmallIntegerField(
                        default=0,
                        help_text="сколько раз была выполнена привычка за день",
                        verbose_name="число выполнений в день",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_habit",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "привычка",
                "verbose_name_plural": "привычки",
            },
        ),
    ]
