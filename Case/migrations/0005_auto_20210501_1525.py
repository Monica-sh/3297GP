# Generated by Django 3.1.8 on 2021-05-01 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Case', '0004_auto_20210501_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='Date_of_Birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='case',
            name='Date_of_Confirmation',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='case',
            name='Date_of_Symptons',
            field=models.DateField(),
        ),
    ]
