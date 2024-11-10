# Generated by Django 5.1.3 on 2024-11-10 18:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articulos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('calificacion', models.IntegerField(choices=[(1, '1 estrella'), (2, '2 estrellas'), (3, '3 estrellas'), (4, '4 estrellas'), (5, '5 estrellas')])),
                ('fecha_resena', models.DateTimeField(auto_now_add=True)),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reseñas', to='articulos.publicacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reseñas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
