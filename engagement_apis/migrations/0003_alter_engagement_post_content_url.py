# Generated by Django 4.2.5 on 2024-10-09 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engagement_apis', '0002_alter_engagement_post_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagement_post_content',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
