# Generated by Django 5.0.4 on 2024-04-06 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billingsystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
