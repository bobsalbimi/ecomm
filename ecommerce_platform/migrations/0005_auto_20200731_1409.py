# Generated by Django 3.0.3 on 2020-07-31 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_platform', '0004_auto_20200730_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='img/none/no-image.png', upload_to='img/'),
        ),
    ]
