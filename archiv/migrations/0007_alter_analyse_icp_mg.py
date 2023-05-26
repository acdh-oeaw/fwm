# Generated by Django 4.1.7 on 2023-05-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0006_project_contact_email_project_contact_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyse',
            name='icp_mg',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_mg', max_digits=19, null=True, verbose_name='Mg'),
        ),
    ]