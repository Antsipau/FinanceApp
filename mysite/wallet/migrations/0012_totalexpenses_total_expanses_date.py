# Generated by Django 4.0.5 on 2022-07-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0011_remove_totalincome_my_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalexpenses',
            name='total_expanses_date',
            field=models.DateField(auto_now=True, db_index=True, verbose_name='Date'),
        ),
    ]