# Generated by Django 4.0 on 2022-02-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artelApp', '0002_alter_feedback_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
