# Generated by Django 3.1.7 on 2021-03-23 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_classify', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='content',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='title',
        ),
        migrations.AddField(
            model_name='plant',
            name='result',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
