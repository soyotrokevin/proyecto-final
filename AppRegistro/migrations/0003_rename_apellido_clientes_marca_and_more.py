# Generated by Django 4.1.1 on 2022-10-03 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppRegistro', '0002_clientes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='apellido',
            new_name='marca',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='nombre',
            new_name='modelo',
        ),
    ]
