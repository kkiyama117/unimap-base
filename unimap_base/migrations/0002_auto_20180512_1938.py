# Generated by Django 2.0.5 on 2018-05-12 10:38

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unimap_base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Border',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefecture', models.CharField(max_length=10, verbose_name='都道府県名')),
                ('branch', models.CharField(blank=True, max_length=20, verbose_name='支庁名')),
                ('major_city', models.CharField(blank=True, max_length=20, verbose_name='群・政令市名')),
                ('city', models.CharField(blank=True, max_length=20, verbose_name='市区町村名')),
                ('code', models.CharField(max_length=5, verbose_name='行政区域コード')),
                ('border', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4612)),
            ],
            options={
                'verbose_name': '行政区域',
                'verbose_name_plural': '行政区域一覧',
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('group', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'campuses',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(default=35.026304)),
                ('longitude', models.FloatField(default=135.780816)),
            ],
            options={
                'verbose_name_plural': 'location',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unimap_base_place_location', related_query_name='unimap_base_places', to='unimap_base.Location')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('floor', models.IntegerField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unimap_base.Building')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unimap_base_room_location', related_query_name='unimap_base_rooms', to='unimap_base.Location')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('slug', models.SlugField(max_length=32)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unimap_base_university_location', related_query_name='unimap_base_universitys', to='unimap_base.Location')),
            ],
            options={
                'verbose_name_plural': 'universities',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('latitude', 'longitude')},
        ),
        migrations.AddField(
            model_name='campus',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unimap_base_campus_location', related_query_name='unimap_base_campuss', to='unimap_base.Location'),
        ),
        migrations.AddField(
            model_name='campus',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unimap_base.University'),
        ),
        migrations.AddField(
            model_name='building',
            name='campus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unimap_base.Campus'),
        ),
        migrations.AddField(
            model_name='building',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unimap_base_building_location', related_query_name='unimap_base_buildings', to='unimap_base.Location'),
        ),
    ]
