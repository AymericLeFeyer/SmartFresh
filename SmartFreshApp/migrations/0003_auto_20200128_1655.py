# Generated by Django 3.0.2 on 2020-01-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartFreshApp', '0002_auto_20200128_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='commentaires',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]