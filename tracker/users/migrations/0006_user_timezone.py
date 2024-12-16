# Generated by Django 4.2.16 on 2024-12-14 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_managers"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="timezone",
            field=models.CharField(
                blank=True,
                default="Europe/Moscow",
                max_length=50,
                null=True,
                verbose_name="часовой пояс пользователя",
            ),
        ),
    ]
