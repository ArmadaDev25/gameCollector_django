# Generated by Django 4.2.6 on 2023-10-23 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('developer', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
            ],
        ),
    ]