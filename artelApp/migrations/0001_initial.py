# Generated by Django 3.2.9 on 2021-12-06 15:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name_uz', models.CharField(max_length=200)),
                ('cat_name_ru', models.CharField(blank=True, max_length=200)),
                ('cat_name_us', models.CharField(blank=True, max_length=200)),
                ('cat_name_tr', models.CharField(blank=True, max_length=200)),
                ('cat_img', models.ImageField(upload_to='categories/')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': '2. Категории',
            },
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_icon', models.ImageField(upload_to='company/')),
                ('short_info', models.CharField(max_length=150)),
                ('company_info', models.TextField()),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': '3.1 Компании',
            },
        ),
        migrations.CreateModel(
            name='ecology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecology_img', models.ImageField(upload_to='ecology/')),
                ('ecology_desc', models.TextField()),
            ],
            options={
                'verbose_name': 'Экология',
                'verbose_name_plural': '3.3.3 Экологии',
            },
        ),
        migrations.CreateModel(
            name='exports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('export_img', models.ImageField(upload_to='exports/')),
                ('export_data', models.IntegerField(default=0)),
                ('export_year', models.DateField(default=datetime.date(2021, 12, 6))),
            ],
            options={
                'verbose_name': 'Экспорт',
                'verbose_name_plural': '3.3.2 Экспорты',
            },
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('starts', models.FloatField()),
                ('comment', models.TextField()),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': '3.3.5 Отзывы',
            },
        ),
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_img', models.ImageField(upload_to='goods/')),
                ('title_uz', models.CharField(max_length=200)),
                ('title_ru', models.CharField(blank=True, max_length=200)),
                ('title_us', models.CharField(blank=True, max_length=200)),
                ('title_tr', models.CharField(blank=True, max_length=200)),
                ('specif_uz', models.CharField(max_length=50)),
                ('specif_ru', models.CharField(blank=True, max_length=50)),
                ('specif_us', models.CharField(blank=True, max_length=50)),
                ('specif_tr', models.CharField(blank=True, max_length=50)),
                ('good_info_uz', models.TextField()),
                ('good_info_ru', models.TextField(blank=True)),
                ('good_info_us', models.TextField(blank=True)),
                ('good_info_tr', models.TextField(blank=True)),
                ('cat_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='artelApp.categories')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': '2.1 Товары',
            },
        ),
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_section', models.CharField(max_length=150)),
                ('comp_icon', models.ImageField(upload_to='info/')),
            ],
            options={
                'verbose_name': 'Информация',
                'verbose_name_plural': '3.3 Информации',
            },
        ),
        migrations.CreateModel(
            name='innovations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('innovation_img', models.ImageField(upload_to='innovations/')),
                ('innovation_desc', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Инноватция',
                'verbose_name_plural': '3.3.4 Инноватции',
            },
        ),
        migrations.CreateModel(
            name='languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose_lang', models.CharField(choices=[('uzbek', 'O`zbek tili'), ('english', 'English'), ('russian', 'Русский язык'), ('turkey', 'Turk dili')], max_length=20)),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': '1. Языки',
            },
        ),
        migrations.CreateModel(
            name='partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=150)),
                ('partner_img', models.ImageField(upload_to='partners/')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': '3.3.1 Партнеры',
            },
        ),
        migrations.CreateModel(
            name='product_bases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_bases_img', models.ImageField(upload_to='ecology/')),
                ('product_bases_desc', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'База продукта',
                'verbose_name_plural': '3.3.6 База продуктов',
            },
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_city', models.CharField(max_length=150)),
                ('service_address', models.CharField(max_length=150)),
                ('service_phone', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': '3.3.7 Сервисы',
            },
        ),
        migrations.CreateModel(
            name='stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('icon', models.ImageField(upload_to='stocks/icon/')),
                ('banner', models.ImageField(upload_to='stocks/banner/')),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'Отчет по продукту',
                'verbose_name_plural': '4.3 Отчеты по продуктам',
            },
        ),
        migrations.CreateModel(
            name='reportsOfLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clc_lang', models.IntegerField(default=0)),
                ('lang_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artelApp.languages')),
            ],
            options={
                'verbose_name': 'Отчет по языку',
                'verbose_name_plural': '4.1 Отчеты по языкам',
            },
        ),
        migrations.CreateModel(
            name='reportsOfGood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clc_good', models.IntegerField(default=0)),
                ('good_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artelApp.goods')),
            ],
            options={
                'verbose_name': 'Отчет по продукту',
                'verbose_name_plural': '4.3 Отчеты по продуктам',
            },
        ),
        migrations.CreateModel(
            name='reportsOfCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clc_cat', models.IntegerField(default=0)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artelApp.categories')),
            ],
            options={
                'verbose_name': 'Отчет по категорие',
                'verbose_name_plural': '4.2 Отчеты по категории',
            },
        ),
    ]
