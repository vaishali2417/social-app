# Generated by Django 5.0.6 on 2024-05-27 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0001_initial'),
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='app_users.profile'),
        ),
    ]
