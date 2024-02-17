# Generated by Django 5.0.1 on 2024-02-17 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsMod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admissionno', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('guardianName', models.CharField(max_length=30)),
                ('guradPhone', models.CharField(max_length=10)),
                ('userName', models.CharField(max_length=6)),
                ('gender', models.CharField(max_length=7)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]
