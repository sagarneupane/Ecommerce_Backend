# Generated by Django 4.0.4 on 2022-06-26 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NFSDATA', '0007_remove_nepalicustom_date_auto_add'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
