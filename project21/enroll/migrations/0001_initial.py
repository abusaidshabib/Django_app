# Generated by Django 4.2.7 on 2023-11-09 07:23

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
                ('suid', models.IntegerField()),
                ('sname', models.CharField(max_length=70)),
                ('semail', models.EmailField(max_length=254)),
                ('spass', models.CharField(max_length=70)),
            ],
        ),
    ]
