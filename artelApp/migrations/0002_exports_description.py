# Generated by Django 3.2.9 on 2021-12-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artelApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exports',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]