# Generated by Django 4.0 on 2021-12-19 18:45

from django.db import migrations, models
import django.db.models.deletion
import measure_snow.util


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SnowSeason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SnowfallMeasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('inches', models.DecimalField(decimal_places=1, max_digits=4)),
                ('season', models.ForeignKey(default=measure_snow.util.get_current_season, on_delete=django.db.models.deletion.CASCADE, to='measure_snow.snowseason')),
            ],
        ),
    ]
