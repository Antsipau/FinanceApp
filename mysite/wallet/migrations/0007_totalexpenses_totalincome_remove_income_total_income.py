# Generated by Django 4.0.5 on 2022-07-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_remove_purchasedgoods_nameof_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_expenses', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Total expenses')),
            ],
        ),
        migrations.CreateModel(
            name='TotalIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_income', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Total income')),
            ],
        ),
        migrations.RemoveField(
            model_name='income',
            name='total_income',
        ),
    ]