# Generated by Django 5.0.3 on 2024-04-30 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0006_rename_image_receipe_receipe_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipe',
            old_name='ar',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='receipe',
            name='receipe_image',
            field=models.ImageField(default='a', upload_to='images'),
        ),
    ]