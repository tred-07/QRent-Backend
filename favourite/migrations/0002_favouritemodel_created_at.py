# Generated by Django 5.1.4 on 2025-01-11 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favouritemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
