# Generated by Django 4.0 on 2022-02-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artelApp', '0003_alter_feedback_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='artel_or_texno_park',
            field=models.BooleanField(default=True, verbose_name='Artel'),
        ),
    ]
