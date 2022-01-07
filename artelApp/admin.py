from django.contrib import admin
from django.contrib.postgres import fields
from .models import *


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


# # 2 models show in 1
# class goodsType(admin.TabularInline):
#     model = goods
#     extra = 3
#     list_display = ('category_id', 'title_uz', 'title_ru', 'title_us', 'title_tr', 
#                     'section_name_uz', 'section_name_ru',
#                     'section_description_uz', 'section_description_ru',)
#     list_filter = (
#         ('title_us', admin.EmptyFieldListFilter), 
#         ('title_tr', admin.EmptyFieldListFilter), 
#     )
#     search_fields  = ('category_id', 'title_uz', 'title_ru')
    
#     def English():
#         return ('title_us', admin.EmptyFieldListFilter), 

# class goodImageType(admin.TabularInline):
#     model = good_images
#     extra = 3
#     fields = ('good_id', ('good_img', 'image_good'), ('good_badge','image_badge'))
#     list_display = ('good_id', 'image_good', 'image_badge')
#     readonly_fields = ('image_good', 'image_badge')

#     inlines = [
#         goodsType,
#     ]
# class goodsAdmin(admin.ModelAdmin):    
#     inlines = [
#         goodImageType,
#     ]
# admin.site.register(goods, goodsAdmin)


@admin.register(goods)
class goodAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'title_uz', 'title_ru', 'title_us', 'title_tr', 
                    'section_name_uz', 'section_name_ru',
                    'section_description_uz', 'section_description_ru',)
    list_filter = (
        ('title_us', admin.EmptyFieldListFilter), 
        ('title_tr', admin.EmptyFieldListFilter), 
    )
    search_fields  = ('category_id', 'title_uz', 'title_ru')
    
    def get_list_display(self, request):
        return super().get_list_display(request)
    
        


@admin.register(good_images)
class goodImagesAdmin(admin.ModelAdmin):
    fields = ('good_id', ('good_img', 'image_good'), ('good_badge','image_badge'))
    list_display = ('good_id', 'image_good', 'image_badge')
    readonly_fields = ('image_good', 'image_badge')


@admin.register(feedback)
class feedbackAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'lastname', 'phone', 'starts', 'comment')


@admin.register(partners)
class partnerAdmin(admin.ModelAdmin):
    fields = (('partner_img', 'image_partner'))
    list_display = ('image_partner', 'partner_img',)
    readonly_fields = ('image_partner',)


@admin.register(company)
class companyAdmin(admin.ModelAdmin):
    fields = (("company_icon", 'image_icon'), "company_short_info", "company_info")
    list_display = ('company_short_info', 'company_info', 'image_icon')
    readonly_fields = ('image_icon',)


@admin.register(ecology)
class ecologAdmin(admin.ModelAdmin):
    fields = ("ecology_desc", ("ecology_img", 'image_ecology'))
    list_display = ('ecology_desc', 'image_ecology')
    readonly_fields = ('image_ecology',)


@admin.register(innovations)
class innovationAdmin(admin.ModelAdmin):
    fields = ('innovation_desc', ('innovation_img', 'image_innovation'))
    list_display = ('innovation_desc', 'image_innovation')
    readonly_fields = ('image_innovation',)


@admin.register(product_bases)
class productBaseAdmin(admin.ModelAdmin):
    fields = ('product_bases_desc', ('product_bases_img', 'image_prod_base'))
    list_display = ('product_bases_desc', 'image_prod_base')
    readonly_fields = ('image_prod_base',)


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
    fields = (("country", "country_icon"), 'image_export', 
                    "description_uz", "description_ru", "description_us", "description_tr",
                    "export_percent_before", "export_percent_after", 
                    "export_year_before", "export_year_after")
    list_display = ("country", 'image_export', 
                    "description_uz", "description_ru", "description_us", "description_tr", 
                    "export_year_before", "export_percent_before", 
                    'export_year_after', "export_percent_after",)
    readonly_fields = ('image_export', )
    list_filter = (
        ("description_us", admin.EmptyFieldListFilter), 
        ("description_tr", admin.EmptyFieldListFilter),
    )

@admin.register(services)
class servic(admin.ModelAdmin):
    list_display = ('service_city', 'service_address_list', 'service_phone', )