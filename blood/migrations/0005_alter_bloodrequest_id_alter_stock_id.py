# Generated by Django 4.2.6 on 2023-10-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0004_bloodrequest_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
