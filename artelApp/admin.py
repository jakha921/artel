from django.contrib import admin
from django.contrib.postgres import fields
from .models import *
from .forms import goodSectionForm


admin.site.register(reportsOfLanguage)
admin.site.register(reportsOfCategory)
admin.site.register(reportsOfGood)



# custimize admin panel

# tabele
@admin.register(categories)
class categoryAdmin(admin.ModelAdmin):
    fields = ("category_name_uz", "category_name_ru", "category_name_us", "category_name_tr", ('category_img', 'image_category'), 'counter_total_product')
    list_display = ("category_name_uz", "category_name_ru","category_name_us", "category_name_tr", 'image_category', 'counter_total_product')
    list_filter = (
        ('category_name_us', admin.EmptyFieldListFilter), 
        ('category_name_tr', admin.EmptyFieldListFilter), 
    )
    readonly_fields = ('image_category', 'counter_total_product')
    
    
    def counter(self, obj):
        count = obj.Good_set.count()
        return count

    counter.short_description = ""


# 2 models show in 1
class goodImageAdmin(admin.StackedInline):
    model = good_images
    extra = 1
    fields = ('good_img', 'image_good'), ('good_badge','image_badge')
    # list_display = ('image_good', 'image_badge')
    readonly_fields = ('image_good', 'image_badge')

class goodSectionAdmin(admin.StackedInline):
    model = good_section
    form = goodSectionForm
    extra = 1
    list_display = ('good_id', 
                    'section_name_uz', 'section_description_uz', 'section_name_ru', 'section_name_us', 'section_name_tr',
                        'section_description_ru', 'section_description_us', 'section_description_tr',
                    )
    fields = ('good_id', 
                    ('section_name_uz', 'section_description_uz'), 
                    ('section_name_ru', 'section_description_ru'),
                    ('section_name_us', 'section_description_us'),
                    ('section_name_tr', 'section_description_tr'),
                    )
    list_filter = (
        ('section_name_us', admin.EmptyFieldListFilter),
        ('section_name_tr', admin.EmptyFieldListFilter),
        ('section_description_us', admin.EmptyFieldListFilter), 
        ('section_description_tr', admin.EmptyFieldListFilter), 
    )

@admin.register(goods)
class goodsInline(admin.ModelAdmin):
    model = goods
    inlines = [
        goodImageAdmin,goodSectionAdmin,
    ]
    list_display  = ('category_id', 'title_uz', 'title_ru',
                    'get_images', #'get_badge',
                    )
    list_filter = (
        ('title_us', admin.EmptyFieldListFilter), 
        ('title_tr', admin.EmptyFieldListFilter), 
    )
    
    search_fields  = ('category_id', 'title_uz', 'title_ru')
    
    def get_images(self, obj):
        preview = [s.good_img.url for s in good_images.objects.filter(good_id = obj)]
        if preview:
            return mark_safe('<img src="%s" style="width: 60px; height:60px;" />' % preview[0])
    
    get_images.short_description = 'Изображение'
    
    def get_badge(self, obj):
        preview = [s.good_badge.url for s in good_images.objects.filter(good_id = obj)] 
        if preview:
            return mark_safe('<img src="%s" style="width: 60px; height:60px;" />' % preview[0])


    get_badge.short_description = 'Бадже'
    
    # def get_section(self, obj):
    #     """show description"""
    #     sectionUZ = [s.section_name_uz for s in good_section.objects.filter(good_id = obj)] 
    #     section_display = mark_safe('<p>"%s"</p>' % sectionUZ[0])
    #     return section_display
        
        


# demo
# @admin.register(good_section)
# class goodSectionAdmin(admin.ModelAdmin):
#     form = goodSectionForm
#     list_display = ('good_id', 'section_name_uz', 'section_name_ru', 'section_name_us', 'section_name_tr')
#     list_filter = (
#         ('section_name_us', admin.EmptyFieldListFilter),
#         ('section_name_tr', admin.EmptyFieldListFilter),
#     )

# @admin.register(good_section_description)
# class goodSectionDescriptionAdmin(admin.ModelAdmin):
#     list_display = ('good_section_id', 'section_description_uz', 'section_description_ru', 'section_description_us', 'section_description_tr')
#     list_filter = (
#         ('section_description_us', admin.EmptyFieldListFilter), 
#         ('section_description_tr', admin.EmptyFieldListFilter), 
#     )


@admin.register(feedback)
class feedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'phone', 'starts', 'comment')
    readonly_fields = ('name', 'lastname', 'phone', 'starts', 'comment')


@admin.register(partners)
class partnerAdmin(admin.ModelAdmin):
    fields = (('partner_img', 'image_partner'))
    list_display = ('image_partner', 'partner_img',)
    readonly_fields = ('image_partner',)


@admin.register(company)
class companyAdmin(admin.ModelAdmin):
    fields = (("company_icon", 'image_icon'), 'company_short_info_uz', 'company_short_info_ru', 'company_short_info_us', 'company_short_info_tr', 'company_info_uz', 'company_info_ru', 'company_info_us', 'company_info_tr', )
    list_display = ( "company_short_info_uz", "company_short_info_ru", "company_info_uz", "company_info_ru", 'image_icon')
    readonly_fields = ('image_icon',)
    list_filter = (
        ('company_short_info_us', admin.EmptyFieldListFilter),
        ('company_short_info_tr', admin.EmptyFieldListFilter),
        ('company_info_us', admin.EmptyFieldListFilter),
        ('company_info_tr', admin.EmptyFieldListFilter),
    )


@admin.register(ecology)
class ecologAdmin(admin.ModelAdmin):
    fields = ('ecology_desc_uz', 'ecology_desc_ru', 'ecology_desc_us',  'ecology_desc_tr', ("ecology_img", 'image_ecology'))
    list_display = ("ecology_desc_uz", "ecology_desc_ru", 'image_ecology')
    readonly_fields = ('image_ecology',)
    list_filter = (
        ('ecology_desc_us', admin.EmptyFieldListFilter),
        ('ecology_desc_tr', admin.EmptyFieldListFilter),
    )


@admin.register(innovations)
class innovationAdmin(admin.ModelAdmin):
    fields = ('innovation_desc_uz', 'innovation_desc_ru', 'innovation_desc_us', 'innovation_desc_tr', ('innovation_img', 'image_innovation'))
    list_display = ('innovation_desc_uz', 'innovation_desc_ru', 'image_innovation')
    readonly_fields = ('image_innovation',)
    list_filter = (
        ('innovation_desc_us', admin.EmptyFieldListFilter),
        ('innovation_desc_tr', admin.EmptyFieldListFilter),
    )


@admin.register(product_bases)
class productBaseAdmin(admin.ModelAdmin):
    fields = ('product_bases_desc_uz', 'product_bases_desc_ru', 'product_bases_desc_us', 'product_bases_desc_tr', ('product_bases_img', 'image_prod_base'))
    list_display = ('product_bases_desc_uz', 'product_bases_desc_ru',  'image_prod_base')
    readonly_fields = ('image_prod_base',)
    list_filter = (
        ('product_bases_desc_us', admin.EmptyFieldListFilter),
        ('product_bases_desc_tr', admin.EmptyFieldListFilter),
    )


@admin.register(stocks)
class stockAdmin(admin.ModelAdmin):
    fields = ("title_uz", "title_ru", "title_us", "title_tr", ("icon", 'icon_stock'), ("banner", 'banner_stock'), "description_uz", "description_ru", "description_us", "description_tr", "start_date", "end_date")
    list_display = ('title_uz', 'title_ru', "title_us", "title_tr", 'icon_stock', 'banner_stock', 'start_date', 'end_date')
    readonly_fields = ('icon_stock', 'banner_stock')
    list_filter = (
        ("title_us", admin.EmptyFieldListFilter),
        ("title_tr", admin.EmptyFieldListFilter),
        ("description_us", admin.EmptyFieldListFilter),
        ("description_tr", admin.EmptyFieldListFilter),
        )

@admin.register(exports)
class exportAdmin(admin.ModelAdmin):
    fields = ( 'country_uz', 'country_ru', 'country_us', 'country_tr',
                ("country_icon", 'image_export'), 
                "description_uz", "description_ru", "description_us", "description_tr",
                "export_percent_before", "export_percent_after", 
                "export_year_before", "export_year_after")
    list_display = ('country_uz', 'country_ru',   'image_export', 
                    "description_uz", "description_ru",
                    "export_year_before", "export_percent_before", 
                    'export_year_after', "export_percent_after",)
    readonly_fields = ('image_export', )
    list_filter = (
        ('country_us', admin.EmptyFieldListFilter), 
        ('country_tr', admin.EmptyFieldListFilter), 
        ("description_us", admin.EmptyFieldListFilter), 
        ("description_tr", admin.EmptyFieldListFilter),
    )

@admin.register(services)
class servic(admin.ModelAdmin):
    list_display = ('service_city_uz', 'service_city_ru','service_address_list_uz', 'service_address_list_ru', 'service_phone', )
    ('service_city_uz', 'service_city_ru', 'service_city_us', 'service_city_tr', 'service_address_list_uz',)