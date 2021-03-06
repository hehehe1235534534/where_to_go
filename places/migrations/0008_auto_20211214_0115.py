# Generated by Django 3.2.9 on 2021-12-13 22:15

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20211213_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
