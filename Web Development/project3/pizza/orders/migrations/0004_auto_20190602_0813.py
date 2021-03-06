# Generated by Django 2.1.7 on 2019-06-02 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("orders", "0003_auto_20190514_2230"),
    ]

    operations = [
        migrations.CreateModel(
            name="MenuItemChoice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("size", models.CharField(max_length=5)),
                (
                    "extras",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.ExtraIngridient",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.MenuItem",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("confirmation", models.BooleanField()),
                ("timestamp", models.DateField(auto_now_add=True)),
                (
                    "items",
                    models.ManyToManyField(
                        related_name="choices",
                        through="orders.MenuItemChoice",
                        to="orders.MenuItem",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="menuitemchoice",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="orders.Order"
            ),
        ),
    ]
