# Generated by Django 2.0.5 on 2018-05-02 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unimap_base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('name', models.CharField(max_length=256)),
                ('group', models.CharField(default=models.CharField(max_length=256), max_length=128)),
            ],
            options={
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
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('slug', models.SlugField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
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
    ]
