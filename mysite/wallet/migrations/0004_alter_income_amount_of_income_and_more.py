# Generated by Django 4.0.5 on 2022-06-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_alter_purchasedgoods_quantity_of_goods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='amount_of_income',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Amount of income'),
        ),
        migrations.AlterField(
            model_name='income',
            name='date_of_income',
            field=models.DateField(auto_now_add=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='income',
            name='total_income',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Total income'),
        ),
    ]