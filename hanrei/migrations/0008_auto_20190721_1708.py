# Generated by Django 2.2.1 on 2019-07-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hanrei', '0007_auto_20190721_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hanreipost',
            name='date',
            field=models.DateTimeField(),
        ),
    ]