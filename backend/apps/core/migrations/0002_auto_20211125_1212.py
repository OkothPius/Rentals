# Generated by Django 3.2.9 on 2021-11-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]