# Generated by Django 3.1.8 on 2021-04-25 09:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Case', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='case',
            options={'ordering': ['Case_Number']},
        ),
        migrations.AlterField(
            model_name='case',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]