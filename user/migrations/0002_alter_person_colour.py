# Generated by Django 4.1.4 on 2023-01-10 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='colour',
            field=models.CharField(choices=[('red', 'Red'), ('blue', 'Blue')], max_length=50),
        ),
    ]