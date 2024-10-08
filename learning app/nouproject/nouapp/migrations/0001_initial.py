# Generated by Django 4.2.3 on 2023-08-23 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.BigIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('dob', models.CharField(max_length=30)),
                ('addess', models.TextField()),
                ('program', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=100)),
                ('contactno', models.CharField(max_length=15)),
                ('emailaddress', models.CharField(max_length=15)),
                ('regdate', models.CharField(max_length=30)),
            ],
        ),
    ]
