# Generated by Django 4.2.6 on 2023-10-30 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='react',
            name='date',
            field=models.DateTimeField(max_length=200),
        ),
        migrations.AlterField(
            model_name='react',
            name='symbol',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
