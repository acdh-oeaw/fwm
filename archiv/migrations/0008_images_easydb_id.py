# Generated by Django 4.1.7 on 2023-06-20 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0007_rename_analyse_id_images_analyse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='easydb_id',
            field=models.IntegerField(blank=True, help_text='whatever', null=True, verbose_name='easyDB ID'),
        ),
    ]
