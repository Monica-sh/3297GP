# Generated by Django 3.2 on 2021-04-30 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Case', '0003_auto_20210425_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('xCoord', models.FloatField()),
                ('yCoord', models.FloatField()),
                ('date', models.DateField()),
                ('number_of_cases', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Case.case')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.publicevent')),
            ],
        ),
    ]
