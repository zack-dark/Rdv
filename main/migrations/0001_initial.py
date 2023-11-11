# Generated by Django 4.2.7 on 2023-11-11 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('dateN', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rendezvous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rendezvous', models.CharField(max_length=30)),
                ('nomclient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('traitement', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('idrendezvous', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.rendezvous')),
            ],
        ),
    ]