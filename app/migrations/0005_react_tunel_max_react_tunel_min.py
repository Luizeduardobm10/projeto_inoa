# Generated by Django 4.2.6 on 2023-10-31 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_react_high_react_low_alter_react_monitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='react',
            name='tunel_max',
            field=models.FloatField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='react',
            name='tunel_min',
            field=models.FloatField(default=-1),
            preserve_default=False,
        ),
    ]
