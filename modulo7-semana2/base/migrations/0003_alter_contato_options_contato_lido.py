# Generated by Django 4.2.1 on 2023-08-15 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_reservadebanho'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'ordering': ['-nome'], 'verbose_name': 'Formulário de Contato', 'verbose_name_plural': 'Formulários de Contatos'},
        ),
        migrations.AddField(
            model_name='contato',
            name='lido',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]