# Generated by Django 2.1.7 on 2019-02-25 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0003_auto_20190225_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='csp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('kcs601', models.CharField(max_length=100)),
                ('kcs602', models.CharField(max_length=100)),
                ('kcs603', models.CharField(max_length=100)),
                ('kcs604', models.CharField(max_length=100)),
                ('kcs605', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'csp',
            },
        ),
    ]
