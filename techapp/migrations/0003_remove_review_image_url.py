# Generated by Django 2.1.5 on 2019-06-06 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techapp', '0002_auto_20190606_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image_url',
        ),
    ]