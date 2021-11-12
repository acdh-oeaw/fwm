# Generated by Django 3.2.8 on 2021-11-12 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyse',
            name='epr_dolom',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Dolomitic Mn2+ DOLOM', max_digits=19, null=True, verbose_name='DOLOM'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_int',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Integral of the spectrum', max_digits=19, null=True, verbose_name='INT'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_integr',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Standardised value of variables', max_digits=19, null=True, verbose_name='INTEGR'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_intens',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Standardised value of variables', max_digits=19, null=True, verbose_name='INTENS'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_spectral_height',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='helptext for epr_spectral_height', max_digits=19, null=True, verbose_name='Spectral height'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_spectrometer',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='helptext for epr_spectrometer', max_digits=19, null=True, verbose_name='Gain of the Spectrometer'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_spli',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Standardised value of variables', max_digits=19, null=True, verbose_name='SPLI'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_spread',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Extension of the spectrum', max_digits=19, null=True, verbose_name='SPREAD'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_spread_standardised',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Standardised value of variables', max_digits=19, null=True, verbose_name='SPREAD Standardised'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_stdintegr',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Value of the standard variable', max_digits=19, null=True, verbose_name='STDINTEGR'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_stdintens',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Value of the standard variable', max_digits=19, null=True, verbose_name='STDINTENS'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_stdspli',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Value of the standard variable', max_digits=19, null=True, verbose_name='STDSPLI'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_stdspread',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Value of the standard variable', max_digits=19, null=True, verbose_name='STDSPREAD'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_stdw',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Value of the standard variable', max_digits=19, null=True, verbose_name='STDW'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_tot6',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Extension of doublet D6', max_digits=19, null=True, verbose_name='TOT6'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_w',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Average spectral width', max_digits=19, null=True, verbose_name='W'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='epr_w_standardised',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Standardised value of variables', max_digits=19, null=True, verbose_name='W Standardised'),
        ),
    ]
