# Generated by Django 4.2.3 on 2023-08-15 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0009_remove_cita_fecha_remove_cita_hora_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cita',
            old_name='año',
            new_name='anio',
        ),
    ]
