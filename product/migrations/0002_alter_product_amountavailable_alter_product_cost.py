# Generated by Django 4.1.2 on 2022-10-04 11:34

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amountAvailable',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.IntegerField(validators=[product.models.Product.validate_amount]),
        ),
    ]
