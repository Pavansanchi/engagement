# Generated by Django 4.2.5 on 2024-10-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engagement_apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagement_post_product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
    ]
