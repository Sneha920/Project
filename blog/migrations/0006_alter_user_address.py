# Generated by Django 4.1.7 on 2023-03-24 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_user_created_at_alter_user_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.JSONField(blank=True, null=True),
        ),
    ]