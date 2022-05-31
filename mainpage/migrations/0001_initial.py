# Generated by Django 4.0.4 on 2022-05-23 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('description', models.TextField(max_length=200)),
                ('title', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50)),
            ],
        ),
    ]