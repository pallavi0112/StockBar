# Generated by Django 3.2.9 on 2022-09-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('RELIANCE', 'RELIANCE'), ('SBIN', 'SBIN'), ('INFY', 'INFY')], max_length=30)),
            ],
        ),
    ]
