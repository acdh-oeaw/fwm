# Generated by Django 4.1.7 on 2023-06-20 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0006_alter_artifact_images_alter_artifact_literature_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='analyse_id',
            new_name='analyse',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='artefact_id',
            new_name='artefact',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='quarry_id',
            new_name='quarry',
        ),
    ]
