# Generated by Django 4.1.5 on 2023-01-20 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("receipts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipt",
            name="date",
            field=models.DateTimeField(),
        ),
    ]