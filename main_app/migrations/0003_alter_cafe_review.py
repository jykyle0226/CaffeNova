# Generated by Django 4.0.5 on 2022-07-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_cafe_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='review',
            field=models.FloatField(),
        ),
    ]
