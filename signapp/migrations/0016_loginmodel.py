# Generated by Django 5.0.1 on 2024-03-08 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signapp', '0015_alter_studentsmod_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=34)),
            ],
        ),
    ]
