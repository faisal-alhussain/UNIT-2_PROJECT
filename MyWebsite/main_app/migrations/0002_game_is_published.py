# Generated by Django 4.2.1 on 2023-05-30 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
