# Generated by Django 2.1.15 on 2020-08-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todoarchive_date_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
