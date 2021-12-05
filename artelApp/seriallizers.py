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
        fields = ('id', "cat_name_uz", "cat_name_ru", "cat_name_us", "cat_name_tr", "cat_img")
        model = categories


# goods serializer
class goodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "cat_id", "title_uz", "title_ru", "title_us", "title_tr", 
                    "specif_uz", "specif_ru", "specif_us", "specif_tr", 
                    "good_info_uz", "good_info_ru", "good_info_us", "good_info_tr", "good_img")
        model = goods


# companies serializer
class companySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "company_icon", "short_info", "company_info",)
        model = company


# info serializer
class infoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "sub_section", "comp_icon")
        model = info


# partners serializer
class partnerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "partner_name", "partner_img")
        model = partners


# export serializer
class exportSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', "country", "export_img", "export_data", "export_year")
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
        fields = ('id', "service_city", "service_address", "service_phone")
        model = services


# reports serializer
class reportOfLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'lang_id', 'clc_lang',)
        model = reportsOfLanguage


class reportsOfCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('cat_id', 'clc_cat',)
        model = reportsOfCategory


class reportsOfGoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('good_id', 'clc_good',)
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