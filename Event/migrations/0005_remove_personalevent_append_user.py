# Generated by Django 3.1.8 on 2021-05-07 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0004_personalevent_append_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalevent',
            name='append_user',
        ),
    ]