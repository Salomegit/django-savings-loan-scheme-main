# Generated by Django 3.0.6 on 2020-05-14 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0003_auto_20200514_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saving',
            name='cycle',
        ),
    ]