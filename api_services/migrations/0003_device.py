# Generated by Django 4.2.3 on 2023-08-24 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_services', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('condition', models.CharField(max_length=100)),
            ],
        ),
    ]