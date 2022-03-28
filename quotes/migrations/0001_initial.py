# Generated by Django 4.0.3 on 2022-03-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('author', models.TextField(blank=True)),
                ('image_url', models.URLField(blank=True)),
            ],
        ),
    ]
