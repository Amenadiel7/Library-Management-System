# Generated by Django 4.0.6 on 2022-12-10 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_1', '0002_alter_order_cust_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cust_date',
            field=models.DateField(null=True),
        ),
    ]
