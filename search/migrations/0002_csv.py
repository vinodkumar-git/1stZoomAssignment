# Generated by Django 3.2 on 2021-04-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='csvs')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
