# Generated by Django 5.0.1 on 2024-01-05 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default='images.jpg', max_length=100),
        ),
    ]
