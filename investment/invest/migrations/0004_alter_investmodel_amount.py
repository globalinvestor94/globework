# Generated by Django 4.2.11 on 2024-02-04 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0003_investmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investmodel',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
