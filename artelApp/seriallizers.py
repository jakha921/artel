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


# goods serializer
class goodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "category_id", 
                    "title_uz", "title_ru", "title_us", "title_tr", 
                    "section_name_uz_list", "section_name_ru_list", 
                    "section_name_us_list", "section_name_tr_list", 
                    "section_description_uz_list", "section_description_ru_list", 
                    "section_description_us_list", "section_description_tr_list", 
                    )
        model = goods


class goodImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('good_id', 'good_img', 'good_badge')
        model = good_images

# companies serializer
class companySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "company_icon", "company_short_info", "company_info",)
        model = company


# info serializer
class infoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "sub_section", "comp_icon")
        model = info


# partners serializer
class partnerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "partner_img")
        model = partners


# export serializer
class exportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "country", "country_icon", "export_percent_before", 
                    "export_percent_after", "export_year_before", "export_year_after")
        model = exports


# ecologies serializer
class ecologySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "ecology_img", "ecology_desc")
        model = ecology


# innovations serializer
class innovationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "innovation_img", "innovation_desc")
        model = innovations


# feedbacks serializer
class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "name", "lastname", "phone", "starts", "comment")
        model = feedback


# product_bases serializer
class productBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "product_bases_img", "product_bases_desc")
        model = product_bases


# services serializer
class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "service_city", "service_address_list", "service_phone")
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
        fields = ('id', 'title', 'icon', 'banner', 'description', 'date')
        model = stocks


# list of users
class userSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username',)
        model = get_user_model()