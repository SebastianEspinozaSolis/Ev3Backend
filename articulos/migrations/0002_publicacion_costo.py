# Generated by Django 5.1.3 on 2024-11-11 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='costo',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
