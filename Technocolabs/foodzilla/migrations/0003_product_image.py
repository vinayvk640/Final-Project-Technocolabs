# Generated by Django 3.1.7 on 2021-05-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodzilla', '0002_auto_20210508_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]