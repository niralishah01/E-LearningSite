# Generated by Django 3.0.2 on 2020-04-24 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20200424_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='categoryname',
        ),
        migrations.DeleteModel(
            name='categories',
        ),
        migrations.DeleteModel(
            name='courses',
        ),
    ]