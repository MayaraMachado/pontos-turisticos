# Generated by Django 2.0.6 on 2018-09-18 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='enderecos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Endereco', to='enderecos.Endereco'),
        ),
    ]
