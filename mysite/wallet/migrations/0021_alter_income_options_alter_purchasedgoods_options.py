# Generated by Django 4.0.5 on 2022-09-20 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0020_remove_income_author_remove_purchasedgoods_author_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='income',
            options={'ordering': ['-id'], 'verbose_name': 'Income', 'verbose_name_plural': 'Incomes'},
        ),
        migrations.AlterModelOptions(
            name='purchasedgoods',
            options={'ordering': ['-id'], 'verbose_name': 'Purchased good', 'verbose_name_plural': 'Purchased goods'},
        ),
    ]
