# Generated by Django 4.2.4 on 2023-10-18 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_bunny_permission_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunny',
            name='main_url',
            field=models.TextField(max_length=2000, unique=True),
        ),
    ]