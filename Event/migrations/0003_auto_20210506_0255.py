# Generated by Django 3.1.8 on 2021-05-06 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0002_auto_20210501_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicevent',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='publicevent',
            name='xCoord',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publicevent',
            name='yCoord',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
