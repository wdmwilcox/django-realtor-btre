# Generated by Django 2.2 on 2019-04-09 14:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('garage', models.IntegerField(default=0)),
                ('square_feet', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('photo_main', models.ImageField(upload_to='photos/%Y%m%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y%m%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y%m%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y%m%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y%m%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y%m%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y%m%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
        ),
    ]
