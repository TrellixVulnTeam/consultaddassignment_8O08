# Generated by Django 2.2 on 2019-09-19 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='image',
        ),
    ]
