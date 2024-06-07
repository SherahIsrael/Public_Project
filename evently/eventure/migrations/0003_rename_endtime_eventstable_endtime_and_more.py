# Generated by Django 5.0.6 on 2024-06-07 11:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventure', '0002_alter_eventstable_attendees'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventstable',
            old_name='EndTime',
            new_name='endTime',
        ),
        migrations.RenameField(
            model_name='eventstable',
            old_name='StartTime',
            new_name='startTime',
        ),
        migrations.AlterField(
            model_name='eventstable',
            name='attendees',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
