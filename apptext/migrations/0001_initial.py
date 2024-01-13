# Generated by Django 5.0.1 on 2024-01-06 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=255)),
                ('mobile', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=255)),
                ('medicine', models.CharField(max_length=300)),
            ],
        ),
    ]
