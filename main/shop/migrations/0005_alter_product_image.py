# Generated by Django 5.0.6 on 2024-12-10 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='templates/photos/1.webp', upload_to='uploads/%y/%m/%d'),
        ),
    ]