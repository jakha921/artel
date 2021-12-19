from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.postgres.fields import ArrayField
import datetime



# choose lang for choices
lang = (
    ('Uzbek', "O`zbek tili"),
    ('English', "English"),
    ('Russian', "Русский язык"),
    ('Turkey', 'Turk dili'),
)

class languages(models.Model):
    choose_lang = models.CharField(max_length=20, choices=lang)
    language_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "1. Языки"

    def __str__(self):
        return self.choose_lang 


# categories
class categories(models.Model):
    category_name_uz = models.CharField(max_length=200)
    category_name_ru = models.CharField(max_length=200)
    category_name_us = models.CharField(max_length=200, blank=True)
    category_name_tr = models.CharField(max_length=200, blank=True)
    category_img = ImageField(upload_to='categories/')
    counter_total_product = models.IntegerField(default=0)
    category_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "2. Категории"

    def __str__(self):
        return self.category_name_uz
    
    

# goods
class goods(models.Model):
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    title_uz = models.CharField(max_length=150)
    title_ru = models.CharField(max_length=150)
    title_us = models.CharField(max_length=150, blank=True)
    title_tr = models.CharField(max_length=150, blank=True)
    section_name_uz_list = ArrayField(models.CharField(max_length=150))
    section_name_ru_list = ArrayField(models.CharField(max_length=150))
    section_name_us_list = ArrayField(models.CharField(max_length=150), blank=True)
    section_name_tr_list = ArrayField(models.CharField(max_length=150), blank=True)
    section_description_uz_list = ArrayField(models.CharField(max_length=150))
    section_description_ru_list = ArrayField(models.CharField(max_length=150))
    section_description_us_list = ArrayField(models.CharField(max_length=150), blank=True)
    section_description_tr_list = ArrayField(models.CharField(max_length=150), blank=True)
    good_create_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "2.1 Товары"

    def __str__(self):
        return str(self.category_id) + " -> " + str(self.title_uz)
    
    
# good_sections 
class good_images(models.Model):
    good_id = models.ForeignKey(goods, on_delete=models.CASCADE)
    good_img = models.ImageField(upload_to='goods/')
    good_badge = models.ImageField(upload_to='badges/')

    class Meta:
        verbose_name = "Картина Товара"
        verbose_name_plural = "2.2 Картинки Товара"


# about -> company
class company(models.Model):
    company_icon = models.ImageField(upload_to="company/")
    company_short_info = models.CharField(max_length=150)
    company_info = models.TextField()
    company_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "3.1 Компании"
    
    def __str__(self):
        return str(self.company_short_info)


# ! check it 
class info(models.Model):
    sub_section = models.CharField(max_length=150)
    comp_icon = models.ImageField(upload_to="info/")
    info_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "3.3 Информации"
    
    def __str__(self):
        return str(self.sub_section)


# about -> info -> partners (LOGO)
class partners(models.Model):
    partner_img = models.ImageField(upload_to="partners/")
    partner_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "3.3.1 Партнеры"
    


# about -> info -> export (countries & info about export)
class exports(models.Model):
    country = models.CharField(max_length=50)
    country_icon = models.ImageField(upload_to="exports/")
    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_us = models.TextField(blank=True)
    description_tr = models.TextField(blank=True)
    export_percent_before = models.FloatField(default=0, max_length=100)
    export_percent_after = models.FloatField(default=0, max_length=100)
    export_year_before = models.CharField(max_length=4)
    export_year_after = models.CharField(max_length=4)
    export_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Экспорт"
        verbose_name_plural = "3.3.2 Экспорты"
    
    def __str__(self):
        return str(self.country)
    

# about -> info -> ecology (posts img & desc)
class ecology(models.Model):
    ecology_img = models.ImageField(upload_to="ecology/")
    ecology_desc = models.TextField()
    ecology_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Экология"
        verbose_name_plural = "3.3.3 Экологии"
    
    
    
# about -> info -> innovation (posts img & desc)
class innovations(models.Model):
    innovation_img = models.ImageField(upload_to="innovations/")
    innovation_desc = models.TextField()
    innovation_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Инноватция"
        verbose_name_plural = "3.3.4 Инноватции"
    


# about -> info -> feedback (from clients get feedback to base)
class feedback(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone  = models.IntegerField()      # max_length=12
    starts = models.IntegerField()
    comment = models.TextField()
    feedback_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "3.3.5 Отзывы"
    
    def __str__(self):
        return str(self.name) + ' ' + str(self.lastname)


# about -> info -> product base (posts img & desc)
class product_bases(models.Model):
    product_bases_img = models.ImageField(upload_to="ecology/")
    product_bases_desc = models.CharField(max_length=150)
    product_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "База продукта"
        verbose_name_plural = "3.3.6 База продуктов"
    
    def __str__(self):
        return str(self.product_bases_desc)


# about -> info -> services
class services(models.Model):
    """give info about centers from regions it is addres & phone number"""
    service_city = models.CharField(max_length=150)
    service_address_list = ArrayField(models.CharField(max_length=150, blank=True))
    service_phone = models.IntegerField()
    
    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "3.3.7 Сервисы"
    
    def __str__(self):
        return str(self.service_city) + " -> " + str(self.service_address_list)


# reports count click from users
class reportsOfLanguage(models.Model):
    """count every click from user and write to the base
    for showing most popular thinds"""
    language_id = models.ForeignKey(languages, on_delete=models.CASCADE,)
    click_language = models.IntegerField(default=0)
    lang_rep_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Отчет по языку"
        verbose_name_plural = "4.1 Отчеты по языкам"
    
    def __str__(self):
        return str(self.language_id) + " " + str(self.click_language)


class reportsOfCategory(models.Model):
    """count every click from user and write to the base
    for showing most popular thinds"""
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE,)
    click_category = models.IntegerField(default=0)
    cat_rep_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Отчет по категорие"
        verbose_name_plural = "4.2 Отчеты по категории"
    
    def __str__(self):
        return str(self.category_id) + " " + str(self.click_category)


class reportsOfGood(models.Model):
    """count every click from user and write to the base
    for showing most popular thinds"""
    good_id = models.ForeignKey(goods, on_delete=models.CASCADE, )
    click_good = models.IntegerField(default=0)
    good_rep_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Отчет по продукту"
        verbose_name_plural = "4.3 Отчеты по продуктам"
    
    def __str__(self):
        return str(self.good_id) + " " + str(self.click_good)


# stocks
class stocks(models.Model):    
    title_uz = models.CharField( max_length=150)
    title_ru = models.CharField( max_length=150)
    title_us = models.CharField( max_length=150, blank=True)
    title_tr = models.CharField( max_length=150, blank=True)
    icon = models.ImageField(upload_to="stocks/icon/")
    banner = models.ImageField(upload_to="stocks/banner/",)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_us = models.TextField(blank=True)
    description_tr = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    stock_category_create_date = models.DateField(auto_now=True)
    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "4.4 Акции"
    
    def __str__(self):
        return str(self.title_uz)



