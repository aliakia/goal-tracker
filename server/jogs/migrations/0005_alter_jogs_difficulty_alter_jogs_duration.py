# Generated by Django 5.0.7 on 2024-07-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogs', '0004_alter_jogs_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogs',
            name='difficulty',
            field=models.CharField(choices=[('0', 'Easy'), ('1', 'Hard')], max_length=1),
        ),
        migrations.AlterField(
            model_name='jogs',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
