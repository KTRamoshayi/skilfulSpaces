# Generated by Django 3.2 on 2021-10-23 05:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registrarion',
            new_name='Registration',
        ),
    ]