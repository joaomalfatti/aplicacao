# Generated by Django 3.1.2 on 2020-11-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotecaTeste', '0003_receita_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y'),
        ),
    ]
