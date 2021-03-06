# Generated by Django 4.0.4 on 2022-06-27 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NFSDATA', '0009_brands_products_sizecategory_subcategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_selling_price', models.FloatField()),
                ('product_amount_sold', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('product_sold', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='NFSDATA.products')),
            ],
        ),
    ]
