# Generated by Django 4.2.1 on 2023-09-25 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_petshop_alter_reservadebanho_diadareserva_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservadebanho',
            name='petshop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='reserva.petshop'),
        ),
    ]