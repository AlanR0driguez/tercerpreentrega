# Generated by Django 4.2.3 on 2023-08-15 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='CI',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
