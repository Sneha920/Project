# Generated by Django 4.1.7 on 2023-03-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Email_id',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
