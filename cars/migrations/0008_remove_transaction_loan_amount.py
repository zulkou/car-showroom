# Generated by Django 5.2 on 2025-04-28 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_remove_transaction_total_cost_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='loan_amount',
        ),
    ]
