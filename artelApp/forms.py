from .models import *
from django.forms import ModelForm, TextInput, Textarea, Select, DateField


class categoryForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = categories
        fields = ["cat_name_uz", "cat_name_ru", "cat_name_us", "cat_name_tr", "cat_img"]     # "cat_img" do not work add with this 
        widgets = {
            "cat_name_uz": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Enter the category name in Uzbek'
            }),
            "cat_name_ru": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Enter the category name in Russian'
            }),
            "cat_name_us": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Enter the category name in English'
            }),
            "cat_name_tr": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Enter the category name in Turkish'
            }),
        }


class goodForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = goods
        fields = ["cat_id", 
                    "title_uz", "title_ru", "title_us", "title_tr", 
                    "specif_uz", "specif_ru", "specif_us", "specif_tr", 
                    "good_info_uz", "good_info_ru", "good_info_us", "good_info_tr",
                    "good_img"]
        widgets = {
            "cat_id": Select(attrs={
                'class': 'form-control col-md-7 col-xs-12',
            }),   
            "title_uz": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Enter title of good'
            }),    
            "title_ru": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Enter title of good'
            }),   
            "title_us": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Enter title of good'
            }),   
            "title_tr": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Enter title of good'
            }),  
            "specif_uz": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'specification'
            }),  
            "specif_ru": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'specification'
            }),   
            "specif_us": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'specification'
            }),   
            "specif_tr": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'specification'
            }),    
            "good_info_uz": Textarea(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'rows':1,
                'cols':15
            }),   
            "good_info_ru": Textarea(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'rows':1,
                'cols':15
            }),   
            "good_info_us": Textarea(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'rows':1,
                'cols':15
            }),   
            "good_info_tr": Textarea(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'rows':1,
                'cols':15
            }),
        }


class stockForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = stocks
        fields = ["title", "icon", "banner", "description", "date"] 
        widgets = {
            "title": TextInput(attrs={                
                'placeholder': 'Enter the stock name'
            }),  
        }
