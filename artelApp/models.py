from django.db import models
from django.db.models.fields.files import ImageField
import datetime

# choose lang for choices
lang = (
    ('uzbek', "O`zbek tili"),
    ('english', "English"),
    ('russian', "Русский язык"),
    ('turkey', 'Turk dili'),
)

class languages(models.Model):
    choose_lang = models.CharField(max_length=20, choices=lang)
    
    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "1. Языки"

    def __str__(self):
        return self.choose_lang 


# categories
class categories(models.Model):
    cat_name_uz = models.CharField(max_length=200)
    cat_name_ru = models.CharField(max_length=200, blank=True)
    cat_name_us = models.CharField(max_length=200, blank=True)
    cat_name_tr = models.CharField(max_length=200, blank=True)
    cat_img = ImageField(upload_to='categories/')
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "2. Категории"

    def __str__(self):
        return self.cat_name_uz


# sub categories
class goods(models.Model):
    cat_id = models.ForeignKey(categories, on_delete=models.CASCADE, blank=True)
    good_img = ImageField(upload_to='goods/')
    title_uz = models.CharField(max_length=200)
    title_ru = models.CharField(max_length=200, blank=True)
    title_us = models.CharField(max_length=200, blank=True)
    title_tr = models.CharField(max_length=200, blank=True)
    specif_uz = models.CharField(max_length=50)
    specif_ru = models.CharField(max_length=50, blank=True)
    specif_us = models.CharField(max_length=50, blank=True)
    specif_tr = models.CharField(max_length=50, blank=True)
    good_info_uz = models.TextField()
    good_info_ru = models.TextField(blank=True)
    good_info_us = models.TextField(blank=True)
    good_info_tr = models.TextField(blank=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "2.1 Товары"

    def __str__(self):
        return str(self.cat_id) + " -> " + str(self.title_uz)


# about 
# class about(models.Model):
#     section = models.CharField(max_length=50)
    
#     class Meta:
#         verbose_name = "О нас"
#         verbose_name_plural = "3. О нас"
    
#     def __str__(self):
#         return str(self.section)


# about -> company
class company(models.Model):
    # about_id = models.ForeignKey(about, on_delete=models.CASCADE)
    company_icon = models.ImageField(upload_to="company/")
    short_info = models.CharField(max_length=150)
    company_info = models.TextField()
    
    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "3.1 Компании"
    
    def __str__(self):
        return str(self.short_info)


# about -> collections
# class collections(models.Model):
#     about_id = models.ForeignKey(about, on_delete=models.CASCADE)
#     cat_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    
#     class Meta:
#         verbose_name = "Колекция"
#         verbose_name_plural = "3.2 Колекции"
    
#     def __str__(self):
#         return str(self.about_id) + " -> " + str(self.cat_id)


# about -> info (addition information)
class info(models.Model):
    # about_id = models.ForeignKey(about, on_delete=models.CASCADE)
    sub_section = models.CharField(max_length=150)
    comp_icon = models.ImageField(upload_to="info/")
    
    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "3.3 Информации"
    
    def __str__(self):
        return str(self.sub_section)


# about -> info -> partners (LOGO)
class partners(models.Model):
    # info_id = models.ForeignKey(info, on_delete=models.CASCADE)
    partner_name = models.CharField(max_length=150)
    partner_img = models.ImageField(upload_to="partners/")
    
    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "3.3.1 Партнеры"
    
    def __str__(self):
        return str(self.info_id) + " -> " + str(self.par_name)


# about -> info -> export (countries & info about export)
class exports(models.Model):
    # info_id = models.ForeignKey(info, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    export_img = models.ImageField(upload_to="exports/")
    export_data = models.IntegerField(default=0)
    export_year = models.DateField(default=datetime.date.today())
    
    class Meta:
        verbose_name = "Экспорт"
        verbose_name_plural = "3.3.2 Экспорты"
    
    def __str__(self):
        return str(self.info_id) + " -> " + str(self.country)
    

# about -> info -> ecology (posts img & desc)
class ecology(models.Model):
    # info_id = models.ForeignKey(info, on_delete=models.CASCADE)
    ecology_img = models.ImageField(upload_to="ecology/")
    ecology_desc = models.TextField()
    
    class Meta:
        verbose_name = "Экология"
        verbose_name_plural = "3.3.3 Экологии"
    
    def __str__(self):
        return str(self.info_id) + " -> " + str(self.eco_desc)
    
    
# about -> info -> innovation (posts img & desc)
class innovations(models.Model):
    # info_id = models.ForeignKey(info, on_delete=models.CASCADE)
    innovation_img = models.ImageField(upload_to="innovations/")
    innovation_desc = models.CharField(max_length=150)
    
    class Meta:
        verbose_name = "Инноватция"
        verbose_name_plural = "3.3.4 Инноватции"
    
    def __str__(self):
        return str(self.info_id) + " -> " + str(self.inno_desc)


# about -> info -> feedback (from clients get feedback to base)
class feedback(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone  = models.IntegerField()      # max_length=12
    starts = models.FloatField()
    comment = models.TextField()
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "3.3.5 Отзывы"
    
    def __str__(self):
        return str(self.name) + ' ' + str(self.lastname)


# about -> info -> product base (posts img & desc)
class product_bases(models.Model):
    # info_id = models.ForeignKey(info, on_delete=models.CASCADE)
    product_bases_img = models.ImageField(upload_to="ecology/")
    product_bases_desc = models.CharField(max_length=150)
    
    class Meta:
        verbose_name = "База продукта"
        verbose_name_plural = "3.3.6 База продуктов"
    
    def __str__(self):
        return str(self.info_id) + " -> " + str(self.prod_desc)


# about -> info -> services
class services(models.Model):
    """give info about centers from regions it is addres & phone number"""
    # info_id = models.ForeignKey(info, on_delete=models.CASCADE)
    service_city = models.CharField(max_length=150)
    service_address = models.CharField(max_length=150)
    service_phone = models.IntegerField()
    
    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "3.3.7 Сервисы"
    
    def __str__(self):
        return str(self.info_id) + " -> " + str(self.ser_city)


# reports count click from users
class reportsOfLanguage(models.Model):
    """count every click from user and write to the base
    for showing most popular thinds"""
    lang_id = models.ForeignKey(languages, on_delete=models.CASCADE,)
    clc_lang = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Отчет по языку"
        verbose_name_plural = "4.1 Отчеты по языкам"
    
    def __str__(self):
        return str(self.lang_id) + " " + str(self.clc_lang)


class reportsOfCategory(models.Model):
    """count every click from user and write to the base
    for showing most popular thinds"""
    cat_id = models.ForeignKey(categories, on_delete=models.CASCADE,)
    clc_cat = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Отчет по категорие"
        verbose_name_plural = "4.2 Отчеты по категории"
    
    def __str__(self):
        return str(self.cat_id) + " " + str(self.clc_cat)


class reportsOfGood(models.Model):
    """count every click from user and write to the base
    for showing most popular thinds"""
    good_id = models.ForeignKey(goods, on_delete=models.CASCADE, )
    clc_good = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Отчет по продукту"
        verbose_name_plural = "4.3 Отчеты по продуктам"
    
    def __str__(self):
        return str(self.good_id) + " " + str(self.clc_good)


# stocks
class stocks(models.Model):    
    title = models.CharField( max_length=150)
    icon = models.ImageField(upload_to="stocks/icon/")
    banner = models.ImageField(upload_to="stocks/banner/",)
    description = models.TextField()
    date = models.DateField()
    class Meta:
        verbose_name = "Отчет по продукту"
        verbose_name_plural = "4.3 Отчеты по продуктам"
    
    def __str__(self):
        return str(self.good_id) + " " + str(self.good_id)

