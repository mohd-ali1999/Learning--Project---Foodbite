# Generated by Django 3.1.1 on 2020-11-06 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_delivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(default=True),
        ),
    ]
