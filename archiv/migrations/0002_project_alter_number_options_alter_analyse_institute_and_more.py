# Generated by Django 4.1.7 on 2023-05-17 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vocabs', '0001_initial'),
        ('archiv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('name', models.CharField(blank=True, help_text='name of the project', max_length=250, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, help_text='description of the quarry group', null=True, verbose_name='description')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
            ],
            options={
                'verbose_name': 'Project',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='number',
            options={'ordering': ['id', 'number'], 'verbose_name': 'Number'},
        ),
        migrations.AlterField(
            model_name='analyse',
            name='institute',
            field=models.ForeignKey(blank=True, help_text='institute where the analysis took place', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Institution_Analysis', to='archiv.institution', verbose_name='institute'),
        ),
        migrations.AlterField(
            model_name='analyse',
            name='oeai_inventory_number',
            field=models.ForeignKey(blank=True, help_text='OeAI inventory number; unique', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Samples_Analysis', to='archiv.sample', verbose_name='OeAI inventory number'),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='find_spot',
            field=models.ForeignKey(blank=True, help_text='find spot of the artefact ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Geography_Artefact_Findspot', to='archiv.geography', verbose_name='find spot'),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='storage_place',
            field=models.ForeignKey(blank=True, help_text='storage institution', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Institution_Artefact_Storage', to='archiv.institution', verbose_name='storage place'),
        ),
        migrations.AlterField(
            model_name='number',
            name='oeai_inventory_number',
            field=models.ForeignKey(blank=True, help_text='OeAI inventory number', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Sample_Other_Numbers', to='archiv.sample', verbose_name='OeAI inventory number'),
        ),
        migrations.AlterField(
            model_name='quarry',
            name='geography',
            field=models.ForeignKey(blank=True, help_text='geographical location of the quarry', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Geography_Quarry', to='archiv.geography', verbose_name='geographical location'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='artefakt_id',
            field=models.ForeignKey(blank=True, help_text='sampled artefact', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artefact_samples', to='archiv.artifact', verbose_name='artefact'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='grain_size_max',
            field=models.ForeignKey(blank=True, help_text='0,5-1,2mm - fine grain; 1,2-2,5 mm medium grain; >2,5mm - coarse grain', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_sample_grain_size_max_skosconcept', to='vocabs.skosconcept', verbose_name='grain size max'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='grain_size_min',
            field=models.ForeignKey(blank=True, help_text='0,5-1,2mm - fine grain; 1,2-2,5 mm medium grain; >2,5mm - coarse grain', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_sample_grain_size_min_skosconcept', to='vocabs.skosconcept', verbose_name='grain size min'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='quarry',
            field=models.ForeignKey(blank=True, help_text='sampled quarry', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Quarry_Samples', to='archiv.quarry', verbose_name='quarry'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='quarry_group',
            field=models.ForeignKey(blank=True, help_text='quarry group', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='QuarryGroup_Samples', to='archiv.quarrygroup', verbose_name='quarry group'),
        ),
        migrations.AddField(
            model_name='analyse',
            name='project',
            field=models.ManyToManyField(help_text='project analyse', related_name='Analyse_Project', to='archiv.project'),
        ),
    ]