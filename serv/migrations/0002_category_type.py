# Generated by Django 5.0.2 on 2025-06-01 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='serv.type'),
            preserve_default=False,
        ),
    ]
