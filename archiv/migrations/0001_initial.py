# Generated by Django 3.2.8 on 2021-11-03 12:51

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vocabs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('legacy_pk', models.IntegerField(blank=True, help_text='whatever', null=True, verbose_name='alt id')),
                ('description', models.TextField(blank=True, help_text='description of the artefact', null=True, verbose_name='description')),
                ('find_spot_extra', models.TextField(blank=True, help_text='additional notes of the find spot', null=True, verbose_name='find spot notes')),
                ('measurement', models.TextField(blank=True, help_text='measurement information of the artefact', null=True, verbose_name='measurement')),
                ('preservation', models.TextField(blank=True, help_text='preservation information', null=True, verbose_name='preservation')),
                ('images', models.CharField(blank=True, help_text='images of the artefact', max_length=250, null=True, verbose_name='images')),
                ('literature', models.CharField(blank=True, help_text='literature', max_length=250, null=True, verbose_name='literature')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
                ('artefact_type', models.ForeignKey(blank=True, help_text='type of the artefact; controlled vocabulary', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_artifact_artefact_type_skosconcept', to='vocabs.skosconcept', verbose_name='artefact type')),
                ('dating', models.ForeignKey(blank=True, help_text='dating information; controlled vocabulary', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_artifact_dating_skosconcept', to='vocabs.skosconcept', verbose_name='dating')),
            ],
            options={
                'verbose_name': 'Artifact',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('name', models.CharField(blank=True, help_text='name of the geographic location', max_length=250, null=True, verbose_name='name')),
                ('identifier', models.CharField(blank=True, help_text='identifier of the geographic location; gazetteers', max_length=250, null=True, verbose_name='identifier')),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(blank=True, help_text='coordinates of the geographic location (X, Y)', null=True, srid=4326, verbose_name='coordinates')),
                ('polygon', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, help_text='MultiPolygonField to depict the area of the location', null=True, srid=4326, verbose_name='polygon')),
                ('notes', models.TextField(blank=True, help_text='additional notes', null=True, verbose_name='notes')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
            ],
            options={
                'verbose_name': 'Geography',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('name', models.CharField(blank=True, help_text='name of the institution', max_length=250, null=True, verbose_name='name')),
                ('identifier', models.CharField(blank=True, help_text='identifier of the institution; gazetteers', max_length=250, null=True, verbose_name='identifier')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
            ],
            options={
                'verbose_name': 'Insititution',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Quarry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('name', models.CharField(blank=True, help_text='name of the quarry', max_length=250, null=True, verbose_name='name')),
                ('images', models.CharField(blank=True, help_text='images', max_length=250, null=True, verbose_name='images')),
                ('description', models.TextField(blank=True, help_text='description of the quarry', null=True, verbose_name='description')),
                ('literature', models.CharField(blank=True, help_text='literature', max_length=250, null=True, verbose_name='literature')),
                ('open_access', models.BooleanField(blank=True, default=False, help_text='open access', null=True, verbose_name='open access')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
                ('geography', models.ForeignKey(blank=True, help_text='geographical location of the quarry', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_quarry_geography_geography', to='archiv.geography', verbose_name='geographical location')),
            ],
            options={
                'verbose_name': 'Quarry',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='QuarryGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('name', models.CharField(blank=True, help_text='name of the quarry group', max_length=250, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, help_text='description of the quarry group', null=True, verbose_name='description')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
            ],
            options={
                'verbose_name': 'QuarryGroup',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('oeai_inventory_number', models.CharField(blank=True, help_text='OeAI inventory number; unique', max_length=250, null=True, verbose_name='OeAI inventory number')),
                ('color_description', models.TextField(blank=True, help_text='precise description of the color', null=True, verbose_name='color description')),
                ('color_kodak', models.CharField(blank=True, help_text='more detailed information about the kodak color', max_length=250, null=True, verbose_name='color kodak')),
                ('stdcolor', models.CharField(blank=True, help_text='more detailed information about the kodak color', max_length=250, null=True, verbose_name='color stdcolor')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, help_text='weight of the sample', max_digits=19, null=True, verbose_name='weight')),
                ('notes', models.TextField(blank=True, help_text='notes', null=True, verbose_name='notes')),
                ('sampling', models.CharField(blank=True, help_text='information about the sampling', max_length=250, null=True, verbose_name='sampling')),
                ('literature', models.CharField(blank=True, help_text='literature', max_length=250, null=True, verbose_name='literature')),
                ('image', models.CharField(blank=True, help_text='images', max_length=250, null=True, verbose_name='images')),
                ('open_access', models.BooleanField(blank=True, default=False, help_text='open access', null=True, verbose_name='open access')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
                ('artefakt_id', models.ForeignKey(blank=True, help_text='sampled artefact', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_sample_artefakt_id_artifact', to='archiv.artifact', verbose_name='artefact')),
                ('color', models.ForeignKey(blank=True, help_text='color of the sample; controlled vocabulary', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_sample_color_skosconcept', to='vocabs.skosconcept', verbose_name='color')),
                ('grain_size_max', models.ForeignKey(blank=True, help_text='maximum grain size; controlled vocabulary', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_sample_grain_size_max_skosconcept', to='vocabs.skosconcept', verbose_name='grain size max')),
                ('grain_size_min', models.ForeignKey(blank=True, help_text='minimum grain size; controlled vocabulary', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_sample_grain_size_min_skosconcept', to='vocabs.skosconcept', verbose_name='grain size min')),
                ('material', models.ForeignKey(blank=True, help_text='material of the sample; controlled vocabulary', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_sample_material_skosconcept', to='vocabs.skosconcept', verbose_name='material')),
                ('quarry', models.ForeignKey(blank=True, help_text='sampled quarry', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_sample_quarry_quarry', to='archiv.quarry', verbose_name='quarry')),
                ('quarry_group', models.ForeignKey(blank=True, help_text='quarry group', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_sample_quarry_group_quarrygroup', to='archiv.quarrygroup', verbose_name='quarry group')),
                ('smell', models.ForeignKey(blank=True, help_text='smell of the sample; entries from 0 to 4', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_sample_smell_skosconcept', to='vocabs.skosconcept', verbose_name='smell')),
            ],
            options={
                'verbose_name': 'Sample',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('legacy_pk', models.IntegerField(blank=True, help_text='whatever', null=True, verbose_name='alt id')),
                ('number', models.CharField(blank=True, help_text='other number', max_length=250, null=True, verbose_name='number')),
                ('notes', models.TextField(blank=True, help_text='additional notes', null=True, verbose_name='notes')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
                ('institute', models.ForeignKey(blank=True, help_text='institute that assigned then number', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_number_institute_institution', to='archiv.institution', verbose_name='institute')),
                ('number_type', models.ForeignKey(blank=True, help_text='type of the number; controlled vocabulary', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_number_number_type_skosconcept', to='vocabs.skosconcept', verbose_name='number type')),
                ('oeai_inventory_number', models.ForeignKey(blank=True, help_text='OeAI inventory number', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_number_oeai_inventory_number_sample', to='archiv.sample', verbose_name='OeAI inventory number')),
            ],
            options={
                'verbose_name': 'Number',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='artifact',
            name='find_spot',
            field=models.ForeignKey(blank=True, help_text='find spot of the artefact ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_artifact_find_spot_geography', to='archiv.geography', verbose_name='find spot'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='material',
            field=models.ForeignKey(blank=True, help_text='the artefacts material; controlled vocabulary', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_artifact_material_skosconcept', to='vocabs.skosconcept', verbose_name='material'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='storage_place',
            field=models.ForeignKey(blank=True, help_text='storage institution', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_artifact_storage_place_institution', to='archiv.institution', verbose_name='storage place'),
        ),
        migrations.CreateModel(
            name='Analyse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legacy_id', models.CharField(blank=True, max_length=300, verbose_name='Legacy ID')),
                ('legacy_pk', models.IntegerField(blank=True, help_text='whatever', null=True, verbose_name='alt id')),
                ('date', models.DateField(blank=True, help_text='analyse date', null=True, verbose_name='date')),
                ('notes_thinsection', models.TextField(blank=True, help_text='helptext for notes_thinsection', null=True, verbose_name='thinsection notes')),
                ('mgco3', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for mgco3', max_digits=19, null=True, verbose_name='MgCO3')),
                ('fe', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for fe', max_digits=19, null=True, verbose_name='Fe')),
                ('mn', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for mn', max_digits=19, null=True, verbose_name='Mn')),
                ('sr', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for sr', max_digits=19, null=True, verbose_name='Sr')),
                ('ion_li', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_li', max_digits=19, null=True, verbose_name='Li')),
                ('ion_na', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_na', max_digits=19, null=True, verbose_name='Na')),
                ('ion_k', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_k', max_digits=19, null=True, verbose_name='K')),
                ('ion_mg', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_mg', max_digits=19, null=True, verbose_name='MgCO3')),
                ('ion_ca', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_ca', max_digits=19, null=True, verbose_name='Ca')),
                ('ion_f', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_f', max_digits=19, null=True, verbose_name='Fe')),
                ('ion_cl', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_cl', max_digits=19, null=True, verbose_name='Cl')),
                ('ion_br', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_br', max_digits=19, null=True, verbose_name='Br')),
                ('ion_j', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_j', max_digits=19, null=True, verbose_name='J')),
                ('ion_no3', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_no3', max_digits=19, null=True, verbose_name='NO3')),
                ('ion_so4', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_so4', max_digits=19, null=True, verbose_name='SO4')),
                ('ion_li_na', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_li_na', max_digits=19, null=True, verbose_name='Li/Na')),
                ('ion_k_na', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_k_na', max_digits=19, null=True, verbose_name='K/Na')),
                ('ion_cl_na', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_cl_na', max_digits=19, null=True, verbose_name='Cl/Na')),
                ('ion_br_na', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_br_na', max_digits=19, null=True, verbose_name='Br/Na')),
                ('ion_i_na', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_i_na', max_digits=19, null=True, verbose_name='I/Na')),
                ('ion_so4_na', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_so4_na', max_digits=19, null=True, verbose_name='SO4/Na')),
                ('ion_f_na', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_f_na', max_digits=19, null=True, verbose_name='F/Na')),
                ('ion_no3_na', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for ion_no3_na', max_digits=19, null=True, verbose_name='NO3/Na')),
                ('iso_d18o', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for iso_d18o', max_digits=19, null=True, verbose_name='d18O (PDB)')),
                ('iso_d13c', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for iso_d13c', max_digits=19, null=True, verbose_name='D13c (PDB)')),
                ('icp_mg', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_mg', max_digits=19, null=True, verbose_name='Mg')),
                ('icp_mn', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_mn', max_digits=19, null=True, verbose_name='Mn')),
                ('icp_fe', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_fe', max_digits=19, null=True, verbose_name='Fe')),
                ('icp_sr', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_sr', max_digits=19, null=True, verbose_name='Sr')),
                ('icp_cr', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_cr', max_digits=19, null=True, verbose_name='Cr')),
                ('icp_cr_n2o', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_cr_n2o', max_digits=19, null=True, verbose_name='Cr (N2O)')),
                ('icp_v', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_v', max_digits=19, null=True, verbose_name='V')),
                ('icp_y', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_y', max_digits=19, null=True, verbose_name='Y')),
                ('icp_cd', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_cd', max_digits=19, null=True, verbose_name='Cd')),
                ('icp_ba', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_ba', max_digits=19, null=True, verbose_name='Ba')),
                ('icp_la', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_la', max_digits=19, null=True, verbose_name='La')),
                ('icp_ce', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_ce', max_digits=19, null=True, verbose_name='Ce')),
                ('icp_pr', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_pr', max_digits=19, null=True, verbose_name='Pr')),
                ('icp_dy', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_dy', max_digits=19, null=True, verbose_name='Dy')),
                ('icp_ho', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_ho', max_digits=19, null=True, verbose_name='Ho')),
                ('icp_yb', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_yb', max_digits=19, null=True, verbose_name='Yb')),
                ('icp_pb', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_pb', max_digits=19, null=True, verbose_name='Pb')),
                ('icp_u', models.DecimalField(blank=True, decimal_places=2, help_text='helptext for icp_u', max_digits=19, null=True, verbose_name='U')),
                ('orig_data_csv', models.TextField(blank=True, null=True, verbose_name='The original data')),
                ('analyse_type', models.ForeignKey(blank=True, help_text='analyse typ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_analyse_analyse_type_skosconcept', to='vocabs.skosconcept', verbose_name='analyse typ')),
                ('institute', models.ForeignKey(blank=True, help_text='institute where the analysis took place', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_analyse_institute_institution', to='archiv.institution', verbose_name='institute')),
                ('oeai_inventory_number', models.ForeignKey(blank=True, help_text='OeAI inventory number; unique', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rvn_analyse_oeai_inventory_number_sample', to='archiv.sample', verbose_name='OeAI inventory number')),
            ],
            options={
                'verbose_name': 'Analyse',
                'ordering': ['id'],
            },
        ),
    ]
