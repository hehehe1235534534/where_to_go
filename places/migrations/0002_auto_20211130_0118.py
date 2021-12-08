# Generated by Django 3.2.9 on 2021-11-29 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('order_number', models.IntegerField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place')),
            ],
        ),
    ]
