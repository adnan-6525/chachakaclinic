# Generated by Django 5.0.1 on 2024-01-06 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptext', '0002_patient_date_patient_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
