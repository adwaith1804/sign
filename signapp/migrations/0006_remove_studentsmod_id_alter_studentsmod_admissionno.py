# Generated by Django 5.0.1 on 2024-02-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signapp', '0005_modelforteacher_tableofnotifications_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsmod',
            name='id',
        ),
        migrations.AlterField(
            model_name='studentsmod',
            name='admissionno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]