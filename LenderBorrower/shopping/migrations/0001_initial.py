# Generated by Django 3.1.3 on 2020-11-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10)),
                ('slot1', models.CharField(max_length=18)),
                ('slot2', models.CharField(max_length=18)),
                ('slot3', models.CharField(max_length=18)),
                ('slot4', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
    ]