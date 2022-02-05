from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model



# lang serializer
class languageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'choose_lang')
        model = languages


# categories serializer
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 
                    "category_name_uz", "category_name_ru", "category_name_us", "category_name_tr",
                    "category_img", "counter_total_product")
        model = categories


class goodImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('good_img', 'good_badge')
        model = good_images
    
    # def to_representation(self, instance):
    #         fields = {'good_img', 'good_badge'}
    #         data = super().to_representation(instance)
    #         for field in fields:
    #             try:
    #                 if not data[field]:
    #                     data[field] = ""
    #             except KeyError:
    #                 pass
    #         return data


# goods serializer
class goodSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = good_section
        fields = ("section_name_uz", "section_name_ru", 
                    "section_name_us", "section_name_tr",
                    "section_description_uz", "section_description_ru", 
                    "section_description_us", "section_description_tr", 
                    )


class goodSerializer(serializers.ModelSerializer):
    goodImage = goodImageSerializer(many=True, read_only=True)
    goodSection = goodSectionSerializer(many=True,)
    
    class Meta:
        model = goods
        fields = ('id', 'category_id', 'title_uz', 'title_ru', 'title_us', 'title_tr', 
                    'goodImage', 'goodSection',)


# companies serializer
class companySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'company_icon', 'company_short_info_uz', 'company_short_info_ru', 'company_short_info_us', 'company_short_info_tr', 'company_info_uz', 'company_info_ru', 'company_info_us', 'company_info_tr', 'company_category_create_date', )
        model = company


# partners serializer
class partnerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "partner_img")
        model = partners


# export serializer
class exportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 
                    'country_uz', 'country_ru', 'country_us', 'country_tr',
                    "country_icon", 
                    "description_uz", "description_ru", "description_us", "description_tr",
                    "export_percent_before", "export_percent_after", 
                    "export_year_before", "export_year_after")
        model = exports


# ecologies serializer
class ecologySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "ecology_img", 
                    'ecology_desc_uz', 'ecology_desc_ru', 'ecology_desc_us', 'ecology_desc_tr',
                    )
        model = ecology


# innovations serializer
class innovationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "innovation_img", 
                    'innovation_desc_uz', 'innovation_desc_ru', 'innovation_desc_us', 'innovation_desc_tr', )
        model = innovations


# feedbacks serializer
class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "name", "lastname", "phone", "starts", "comment")
        model = feedback


# product_bases serializer
class productBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "product_bases_img", 
                    'product_bases_desc_uz', 'product_bases_desc_ru', 'product_bases_desc_us', 'product_bases_desc_tr', 
                    )
        model = product_bases


# services serializer
class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 
                    'service_city_uz', 'service_city_ru', 'service_city_us', 'service_city_tr',
                    'service_address_list_uz', 'service_address_list_ru', 'service_address_list_us', 'service_address_list_tr',
                    "service_phone")
        model = services


# reports serializer
class reportOfLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'language_id', 'click_language',)
        model = reportsOfLanguage


class reportsOfCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('category_id', 'click_category',)
        model = reportsOfCategory


class reportsOfGoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('good_id', 'click_good',)
        model = reportsOfGood


class stockSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title_uz', 'title_ru', 'title_us', 'title_tr',
                    'icon', 'banner', 
                    'description_uz', 'description_ru', 'description_us', 'description_tr',
                    'start_date', 'end_date')
        model = stocks


# list of users
class userSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username',)
        model = get_user_model()