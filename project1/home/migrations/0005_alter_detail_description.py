# Generated by Django 4.1.4 on 2022-12-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_detail_description_detail_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
