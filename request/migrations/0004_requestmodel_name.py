# Generated by Django 5.1.4 on 2025-02-13 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_alter_requestmodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestmodel',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
