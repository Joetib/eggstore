# Generated by Django 3.0.6 on 2020-05-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200508_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('feature', models.CharField(max_length=500)),
            ],
        ),
    ]
