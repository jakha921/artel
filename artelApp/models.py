from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.postgres.fields import ArrayField
from django.utils import tree
from django.utils.safestring import mark_safe
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator



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
        verbose_name_plural = "Языки"

    def __str__(self):
        return self.choose_lang 


# categories
class categories(models.Model):
    category_name_uz = models.CharField('Узбекский', max_length=200)
    category_name_ru = models.CharField('Русский', max_length=200)
    category_name_us = models.CharField('Английский', max_length=200, blank=True)
    category_name_tr = models.CharField('Турецкий', max_length=200, blank=True)
    category_img = ImageField('Икона' ,upload_to='categories/')
    counter_total_product = models.IntegerField('Cчетчик продуктов' , default=0)
    category_category_create_date = models.DateField(auto_now=True)
    
    def image_category(self):
        if self.category_img:
            return mark_safe('<img src="%s" style="width: 60px; height:60px;" />' % self.category_img.url)
        else:
            return 'No Image Found'
    image_category.short_description = 'Просмотр иконы'
    image_category.allow_tags = True
    
    def get_num_product(self):
        return goods.objects.filter(category_id=self).count()
    
    counter_total_product = get_num_product

    image_category.short_description = 'Просмотр иконы'
    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "1. Категории"

    def __str__(self):
        return self.category_name_uz
    
    

# goods or good... is mean product
class goods(models.Model):
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE, verbose_name='Категория')
    title_uz = models.CharField('Загл. Узб', max_length=250)
    title_ru = models.CharField('Загл. Рус', max_length=250)
    title_us = models.CharField('Загл. Анг', max_length=250, blank=True)
    title_tr = models.CharField('Загл. Тур', max_length=250, blank=True)
    section_name_uz = ArrayField(ArrayField(models.CharField(max_length=999)), verbose_name='Разд Узб')
    section_name_ru = ArrayField(ArrayField(models.CharField(max_length=999)), verbose_name='Разд Рус')
    section_name_us = ArrayField(ArrayField(models.CharField(max_length=999)), blank=True, verbose_name='Разд Анг')
    section_name_tr = ArrayField(ArrayField(models.CharField(max_length=999)), blank=True, verbose_name='Разд Тур')
    section_description_uz = ArrayField(ArrayField(models.CharField(max_length=999)), blank=True, verbose_name='Опис Узбекский')
    section_description_ru = ArrayField(ArrayField(models.CharField(max_length=999)), blank=True, verbose_name='Опис Русский')
    section_description_us = ArrayField(ArrayField(models.CharField(max_length=999)), blank=True, verbose_name='Опис Английский')
    section_description_tr = ArrayField(ArrayField(models.CharField(max_length=999)), blank=True, verbose_name='Опис Турецкий')
    good_create_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "2.1 Продукты"

    def __str__(self):
        return str(self.category_id) + " -> " + str(self.title_uz)
    
    
# good_sections 
class good_images(models.Model):
    good_id = models.ForeignKey(goods, on_delete=models.CASCADE, verbose_name='Название продукта', related_name='goodImage')
    good_img = models.ImageField('Изображения', upload_to='goods/', blank=True)
    good_badge = models.ImageField('Значок', upload_to='badges/', blank=True)

    class Meta:
        verbose_name = "Изображение продукту"
        verbose_name_plural = "2.2 Продукты -> Картинки "
        
    def image_good(self):
        if self.good_img:
            return mark_safe('<img src="%s" style="width: 60px; height:60px;" />' % self.good_badge.url)
        else:
            return 'No Image Found'
        
    def image_badge(self):
        if self.good_badge:
            return mark_safe('<img src="%s" style="width: 60px; height:60px;" />' % self.good_badge.url)
        else:
            return 'No Image Found'
        
    image_good.short_description = 'Просмотр изображение'
    image_good.allow_tags = True
        
    image_badge.short_description = 'Просмотр иконы'
    image_badge.allow_tags = True
    
    def __str__(self):
        return 'image: ' + 'https://artel-catalog.s3.amazonaws.com/media/' + str(self.good_img) + '  ' + ' badge: ' + 'https://artel-catalog.s3.amazonaws.com/media/'+ str(self.good_badge)
    


# about -> company
class company(models.Model):
    company_icon = models.ImageField('значок компании', upload_to="company/")
    company_short_info = models.CharField('Название', max_length=150)
    company_info = models.TextField('Информация')
    company_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Информацию о компании"
        verbose_name_plural = "5. О нас -> Информацию компании"
    
    def __str__(self):
        return str(self.company_short_info)
    
    def image_icon(self):
        if self.company_icon:
            return mark_safe('<img src="%s" style="width: 60px; height:60px;" />' % self.company_icon.url)
        else:
            return 'No Image Found'
        
    image_icon.short_description = 'Просмотр иконы'
    image_icon.allow_tags = True


# about -> info -> partners (LOGO)
class partners(models.Model):
    partner_img = models.ImageField('Значки брендов' , upload_to="partners/")
    partner_category_create_date = models.DateField(auto_now=True)
    
    def image_partner(self):
        if self.partner_img:
            return mark_safe('<img src="%s" style="width: 80px; height:60px;" />' % self.partner_img.url)
        else:
            return 'No Image Found'
        
    image_partner.short_description = 'Просмотр изображение'
    image_partner.allow_tags = True
    
    class Meta:
        verbose_name = "Партнера"
        verbose_name_plural = "4. Партнеры"
    


# about -> info -> export (countries & info about export)
class exports(models.Model):
    country = models.CharField('Страна', max_length=50)
    country_icon = models.ImageField('Значок страны', upload_to="exports/")
    description_uz = models.TextField('Описание на Узбекском', blank=True)
    description_ru = models.TextField('Описание на Русском', blank=True)
    description_us = models.TextField('Описание на Английском', blank=True)
    description_tr = models.TextField('Описание на Турецком', blank=True)
    export_percent_before = models.FloatField('Проценты до', default=0, max_length=100)
    export_percent_after = models.FloatField('Проценты после', default=0, max_length=100)
    export_year_before = models.CharField('Годом ранее', max_length=4)
    export_year_after = models.CharField('Год спустя', max_length=4)
    export_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Экспорт"
        verbose_name_plural = "6.1 О нас -> Информации -> Экспорты"
    
    def __str__(self):
        return str(self.country)
    
    def image_export(self):
        """show image in admin panel on table"""
        if self.country_icon:
            return mark_safe('<img src="%s" style="width: 60px; height:60px;" />' % self.country_icon.url)
        else:
            return 'No Image Found'
        
    image_export.short_description = 'Просмотр значка'
    image_export.allow_tags = True
    

# about -> info -> ecology (posts img & desc)
class ecology(models.Model):
    ecology_img = models.ImageField("Изображениe", upload_to="ecology/")
    ecology_desc = models.TextField("Описание")
    ecology_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Экологию"
        verbose_name_plural = "6.2 О нас -> Информации -> Экологии"

    def __str__(self):
        return self.ecology_desc
    
    
    def image_ecology(self):
        """show image in admin panel on table"""
        if self.ecology_img:
            return mark_safe('<img src="%s" style="width: 60px; height:60px;" />' % self.ecology_img.url)
        else:
            return 'No Image Found'
        
    image_ecology.short_description = 'Просмотр изображение'
    image_ecology.allow_tags = True
    
    
    
# about -> info -> innovation (posts img & desc)
class innovations(models.Model):
    innovation_img = models.ImageField("Изображениe", upload_to="innovations/")
    innovation_desc = models.TextField("Описание")
    innovation_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Информацию об инновации"
        verbose_name_plural = "6.3 О нас -> Информации -> Инноватции"
    
    def image_innovation(self):
        """show image in admin panel on table"""
        if self.innovation_img:
            return mark_safe('<img src="%s" style="width: 60px; height:60px;" />' % self.innovation_img.url)
        else:
            return 'No Image Found'
        
    image_innovation.short_description = "Просмотр изображение"
    image_innovation.allow_tags = True
    


# about -> info -> feedback (from clients get feedback to base)
class feedback(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone  = models.IntegerField()      # max_length=12
    starts = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField()
    feedback_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "8. Отзывы"
    
    def __str__(self):
        return str(self.name) + ' ' + str(self.lastname)


# about -> info -> product base (posts img & desc)
class product_bases(models.Model):
    product_bases_img = models.ImageField("Изображениe", upload_to="ecology/")
    product_bases_desc = models.CharField("Описание", max_length=150)
    product_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Производственную базу"
        verbose_name_plural = "6.4 О нас -> Информации -> База продуктов"
    
    def __str__(self):
        return str(self.product_bases_desc)
    
    def image_prod_base(self):
        """show image in admin panel on table"""
        if self.product_bases_img:
            return mark_safe('<img src="%s" style="width: 60px; height:60px;" />' % self.product_bases_img.url)
        else:
            return 'No Image Found'
        
    image_prod_base.short_description = 'Просмотр изображение'
    image_prod_base.allow_tags = True


# about -> info -> services
class services(models.Model):
    """give info about centers from regions it is addres & phone number"""
    service_city = models.CharField('Название города', max_length=150)
    service_address_list = ArrayField(ArrayField(models.CharField(max_length=250, blank=True)), verbose_name="Адресса")
    service_phone = models.IntegerField("Номер телефона", blank=True)
    
    class Meta:
        verbose_name = "Сервисный центр"
        verbose_name_plural = "6.5 О нас -> Информации -> Сервисы"
    


# reports count click from users
class reportsOfLanguage(models.Model):
    """count every click from user and write to the base
    for showing most popular thinds"""
    language_id = models.ForeignKey(languages, on_delete=models.CASCADE, verbose_name='Язык')
    click_language = models.IntegerField('Количество кликов', default=0)
    lang_rep_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Отчет по языку"
        verbose_name_plural = "7.1 Отчеты по языкам"
    
    def __str__(self):
        return str(self.language_id) + " " + str(self.click_language)


class reportsOfCategory(models.Model):
    """count every click from user and write to the base
    for showing most popular thinds"""
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE, verbose_name='Категория')
    click_category = models.IntegerField('Количество кликов', default=0)
    cat_rep_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Отчет по категорие"
        verbose_name_plural = "7.2 Отчеты по категории"
    
    def __str__(self):
        return str(self.category_id) + " " + str(self.click_category)


class reportsOfGood(models.Model):
    """count every click from user and write to the base
    for showing most popular thinds"""
    good_id = models.ForeignKey(goods, on_delete=models.CASCADE, verbose_name='Продукт')
    click_good = models.IntegerField('Количество кликов', default=0)
    good_rep_category_create_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Отчет по продукту"
        verbose_name_plural = "7.3 Отчеты по продуктам"
    
    def __str__(self):
        return str(self.good_id) + " " + str(self.click_good)


# stocks
class stocks(models.Model):    
    title_uz = models.CharField('Узбекский', max_length=150)
    title_ru = models.CharField('Русский', max_length=150)
    title_us = models.CharField('Английский', max_length=150, blank=True)
    title_tr = models.CharField('Турецкий', max_length=150, blank=True)
    icon = models.ImageField('Икона', upload_to="stocks/icon/")
    banner = models.ImageField('Баннер', upload_to="stocks/banner/",)
    description_uz = models.TextField('Описание на узбекском',)
    description_ru = models.TextField('Описание на русском',)
    description_us = models.TextField('Описание на английском',blank=True)
    description_tr = models.TextField('Описание на турецком', blank=True)
    start_date = models.DateField('Дата стратра')
    end_date = models.DateField('Дата окончания')
    stock_category_create_date = models.DateField(auto_now=True)
    class Meta:
        verbose_name = "Акцию"
        verbose_name_plural = "3. Акции"
    
    def __str__(self):
        return str(self.title_uz)
    
    def icon_stock(self):
        if self.icon:
            return mark_safe('<img src="%s" style="width: 60px; height:60px;" />' % self.icon.url)
        else:
            return 'No Image Found'
        
    def banner_stock(self):
        if self.banner:
            return mark_safe('<img src="%s" style="width: 60px; height:60px;" />' % self.banner.url)
        else:
            return 'No Image Found'
        
    icon_stock.short_description = 'Просмотр иконы'
    icon_stock.allow_tags = True
        
    banner_stock.short_description = 'Просмотр баннера'
    banner_stock.allow_tags = True



