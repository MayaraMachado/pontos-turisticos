# Generated by Django 2.0.6 on 2018-09-21 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atracao',
            name='foto',
            field=models.ImageField(default='contato_foto3.png', upload_to='img', verbose_name='Atrações'),
            preserve_default=False,
        ),
    ]