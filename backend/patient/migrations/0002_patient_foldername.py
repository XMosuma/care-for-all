# Generated by Django 5.1.2 on 2024-10-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='folderName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
