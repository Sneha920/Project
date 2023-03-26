# Generated by Django 4.1.7 on 2023-03-24 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='blog.product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='blog.user'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to='blog.product'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to='blog.user'),
        ),
    ]
