# Generated by Django 5.1.2 on 2024-10-26 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthworker', '0003_rename_date_of_birth_healthworkerprofile_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthworkerprofile',
            name='jobTitle',
            field=models.CharField(choices=[('nurse', 'Nurse'), ('doc', 'Doctor'), ('ch_worker', 'Community Health Worker')], max_length=50),
        ),
    ]
