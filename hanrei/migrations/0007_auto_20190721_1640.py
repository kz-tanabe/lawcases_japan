# Generated by Django 2.2.1 on 2019-07-21 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hanrei', '0006_hanreipost_judgement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hanreipost',
            name='date',
            field=models.DateField(),
        ),
    ]