# Generated by Django 4.1.7 on 2023-05-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0003_alter_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarrygroup',
            name='quarry',
            field=models.ManyToManyField(help_text='Quarry Quarrygroup', related_name='Quarrygroup_Quarry', to='archiv.quarry'),
        ),
    ]