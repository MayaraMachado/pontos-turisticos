# Generated by Django 2.0.6 on 2018-09-21 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0002_auto_20180919_1001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaliacao',
            old_name='usuario',
            new_name='user',
        ),
    ]
