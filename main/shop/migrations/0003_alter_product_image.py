# Generated by Django 5.0.6 on 2024-12-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_user_attempts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='templates\\photos\x01.webp', upload_to='uploads/% Y/% m/% d/'),
        ),
    ]