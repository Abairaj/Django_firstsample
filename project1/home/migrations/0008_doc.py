# Generated by Django 4.1.4 on 2022-12-08 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_about_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
