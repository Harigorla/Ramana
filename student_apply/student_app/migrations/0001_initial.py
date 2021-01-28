# Generated by Django 3.0 on 2021-01-12 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('fullname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('email', models.EmailField(max_length=200, primary_key=True, serialize=False)),
                ('phone', models.IntegerField()),
                ('ssc', models.CharField(max_length=100)),
                ('inter', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='images')),
                ('currentaddress', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=30)),
                ('positionapply', models.CharField(max_length=300)),
                ('isactive', models.BooleanField(default=False)),
            ],
        ),
    ]
