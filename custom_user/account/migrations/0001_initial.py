# Generated by Django 3.0 on 2021-01-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email address')),
                ('company_name', models.CharField(max_length=100, unique=True, verbose_name='company_name')),
                ('phone', models.CharField(max_length=50, verbose_name='company phone')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='company date')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='company last date')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
