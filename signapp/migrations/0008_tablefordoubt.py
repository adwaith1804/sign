# Generated by Django 5.0.1 on 2024-03-02 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signapp', '0007_alter_studentsmod_admissionno'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableForDoubt',
            fields=[
                ('doubtid', models.AutoField(primary_key=True, serialize=False)),
                ('doubt', models.CharField(max_length=1000)),
                ('teacherloginid', models.CharField(max_length=10)),
                ('studentloginid', models.CharField(max_length=50)),
                ('currentdate', models.DateField(null=True)),
            ],
        ),
    ]
