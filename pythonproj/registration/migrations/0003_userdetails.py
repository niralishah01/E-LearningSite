# Generated by Django 3.0.2 on 2020-04-08 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0002_delete_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emailID', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
