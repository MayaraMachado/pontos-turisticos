# Generated by Django 2.0.6 on 2018-09-24 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_pontoturistico_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pontoturistico',
            old_name='enderecos',
            new_name='endereco',
        ),
    ]
