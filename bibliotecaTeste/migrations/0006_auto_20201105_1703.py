# Generated by Django 3.1.2 on 2020-11-05 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotecaTeste', '0005_auto_20201105_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
