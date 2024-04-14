# Generated by Django 4.2.11 on 2024-01-31 16:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('preview_text', models.CharField(max_length=200)),
                ('body_text', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('testimony', models.CharField(max_length=500)),
                ('pictures', models.ImageField(blank=True, upload_to='Pictures/')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
