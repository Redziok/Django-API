# Generated by Django 4.1.2 on 2022-11-23 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_person_rename_druzyna_team_delete_persons_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='base.team'),
        ),
    ]
