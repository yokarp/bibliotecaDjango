# Generated by Django 3.2.5 on 2021-07-16 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('fecha', models.DateField(verbose_name='Fecha de lanzamiento')),
                ('portada', models.ImageField(upload_to='portada')),
                ('visitas', models.PositiveBigIntegerField()),
                ('autores', models.ManyToManyField(to='autor.Autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.categoria')),
            ],
        ),
    ]
