# Generated by Django 4.2.4 on 2023-09-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_bunny_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='bunny',
            name='title',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]