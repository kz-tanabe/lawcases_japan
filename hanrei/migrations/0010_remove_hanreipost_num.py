# Generated by Django 2.2.1 on 2019-09-18 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hanrei', '0009_auto_20190722_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hanreipost',
            name='num',
        ),
    ]
