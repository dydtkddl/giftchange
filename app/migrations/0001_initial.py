# Generated by Django 4.1.1 on 2022-10-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brandlist",
            fields=[
                (
                    "name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("category", models.CharField(max_length=100)),
                (
                    "imageurl",
                    models.CharField(default=None, max_length=1000, null=True),
                ),
            ],
            options={"db_table": "brandlist",},
        ),
        migrations.CreateModel(
            name="Typelist",
            fields=[
                (
                    "name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
            ],
            options={"db_table": "typelist",},
        ),
    ]