# Generated by Django 4.1.2 on 2022-11-23 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_alter_person_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to=settings.AUTH_USER_MODEL),
        ),
    ]
