# Generated by Django 4.1.7 on 2023-03-14 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email_id', models.CharField(max_length=155)),
                ('Created_at', models.DateTimeField()),
                ('Modified_at', models.DateTimeField()),
                ('user_name', models.CharField(max_length=155)),
                ('password', models.CharField(max_length=155)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.JSONField()),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
    ]
