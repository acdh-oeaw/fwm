# Generated by Django 3.2.8 on 2021-11-04 09:29

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkosCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pref_label', models.CharField(blank=True, help_text='Collection label or name', max_length=300, null=True, verbose_name='skos:prefLabel')),
                ('definition', models.TextField(blank=True, help_text='definition', null=True, verbose_name='elaborate definition of the collection')),
                ('source_uri', models.CharField(blank=True, help_text='URI of the Resource', max_length=300, null=True, verbose_name='source URI')),
            ],
        ),
        migrations.CreateModel(
            name='SkosTechnicalCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pref_label', models.CharField(blank=True, help_text="e.g. 'Artifact__artefact_type", max_length=300, null=True, verbose_name='Model and property name')),
            ],
        ),
        migrations.CreateModel(
            name='SkosConcept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pref_label', models.CharField(help_text='Preferred label for concept', max_length=300, verbose_name='skos:prefLabel')),
                ('definition', models.TextField(blank=True, help_text='skos:definition', null=True, verbose_name='elaborate definition of the concept')),
                ('source_uri', models.CharField(blank=True, help_text='URI of the Resource', max_length=300, null=True, verbose_name='source URI')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('broader_concept', mptt.fields.TreeForeignKey(blank=True, help_text='Concept with a broader meaning that this concept inherits from', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='narrower_concepts', to='vocabs.skosconcept', verbose_name='skos:broader')),
                ('collection', models.ForeignKey(blank=True, help_text='Collection that this concept is a member of', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='has_members', to='vocabs.skoscollection', verbose_name='member of skos:Collection')),
                ('tech_collection', models.ManyToManyField(blank=True, help_text='Collection that this concept is a member of', related_name='has_members', to='vocabs.SkosTechnicalCollection', verbose_name='member of skos:Collection')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
