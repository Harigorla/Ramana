# Generated by Django 3.0 on 2021-01-06 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipenewapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='title',
        ),
    ]