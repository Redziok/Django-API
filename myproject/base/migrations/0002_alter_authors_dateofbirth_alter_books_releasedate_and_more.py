# Generated by Django 4.1.2 on 2022-10-16 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='dateOfBirth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='books',
            name='releaseDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='dateOfBirth',
            field=models.DateField(),
        ),
    ]
