# Generated by Django 3.1.8 on 2021-05-08 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0005_remove_personalevent_append_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personalevent',
            options={'ordering': ('case', 'event')},
        ),
        migrations.AlterModelOptions(
            name='publicevent',
            options={'ordering': ('date', 'name')},
        ),
    ]
