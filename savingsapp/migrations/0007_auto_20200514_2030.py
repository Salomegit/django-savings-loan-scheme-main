# Generated by Django 3.0.6 on 2020-05-14 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savingsapp', '0006_auto_20200514_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
