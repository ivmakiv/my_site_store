# Generated by Django 4.2 on 2024-10-21 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='decription',
            new_name='description',
        ),
    ]