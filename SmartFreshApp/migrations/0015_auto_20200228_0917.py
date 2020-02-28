# Generated by Django 3.0.2 on 2020-02-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('SmartFreshApp', '0014_auto_20200227_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Francite',
            fields=[
                ('id',
                 models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='ID du lot francité')),
                ('contremarque', models.CharField(blank=True, max_length=128, null=True, verbose_name='Contremarque')),
                ('produit', models.CharField(max_length=32, verbose_name='Produit')),
                ('quantite', models.IntegerField(default=0, verbose_name='Quantité')),
            ],
        ),
        migrations.AlterField(
            model_name='lotbloque',
            name='quantite',
            field=models.IntegerField(default=0, verbose_name='Quantité'),
        ),
    ]