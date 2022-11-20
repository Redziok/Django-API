# Generated by Django 4.1.2 on 2022-11-20 14:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='Ratings',
            new_name='Rating',
        ),
    ]