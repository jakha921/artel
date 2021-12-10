from .models import *
from django.forms import ModelForm, TextInput, Textarea, Select, DateField


class categoryForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = categories
        fields = ["category_name_uz", "category_name_ru", "category_name_us", "category_name_tr", "category_img"]     # "cat_img" do not work add with this 
        widgets = {
            "category_name_uz": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Enter the category name in Uzbek'
            }),
            "category_name_ru": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Enter the category name in Russian'
            }),
            "category_name_us": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Enter the category name in English'
            }),
            "category_name_tr": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Enter the category name in Turkish'
            }),
        }


class goodForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = goods
        fields = ["category_id", 
                    "title_uz", "title_ru", "title_us", "title_tr",
                    "section_name_uz_list", "section_name_ru_list", "section_name_us_list", "section_name_tr_list",
                    "section_description_uz_list", "section_description_ru_list", "section_description_us_list", "section_description_tr_list",
                    ]
        widgets = {
            "category_id": Select(attrs={
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
            "section_name_uz_list": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'specification (list ex: func, size and etc)'
            }),  
            "section_name_ru_list": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'specification (list ex: func, size and etc)'
            }),   
            "section_name_us_list": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'specification (list ex: func, size and etc)'
            }),   
            "section_name_tr_list": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'specification (list ex: func, size and etc)'
            }),    
            "section_description_uz_list": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'description (list ex: quality, easy and etc)'
            }),    
            "section_description_ru_list": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'description (list ex: quality, easy and etc)'
            }),    
            "section_description_us_list": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'description (list ex: quality, easy and etc)'
            }),    
            "section_description_tr_list": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'description (list ex: quality, easy and etc)'
            }),    
            # "good_info_uz": Textarea(attrs={
            #     'class': 'form-control col-md-7 col-xs-12',
            #     'rows':1,
            #     'cols':15
            # }),   
        }
        

class goodImagesForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = good_images
        fields = ["good_id", "good_img", "good_badge"] 
        widgets = {
            "good_id": Select(attrs={
                'class': 'form-control col-md-7 col-xs-12',
            }),   
        }


class stockForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = stocks
        fields = ["title_uz", "title_ru", "title_us", "title_tr",
                    "icon", "banner", 
                    "description_uz", "description_ru", "description_us", "description_tr", 
                    "start_date", "end_date"] 
        widgets = {
            "title_uz": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'title'
            }),
            "title_ru": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'title'
            }),
            "title_us": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'title'
            }),
            "title_tr": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'title'
            }),
            "description_uz": Textarea(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'rows':1,
                'cols':15
            }), 
            "description_ru": Textarea(attrs={                
                'class': 'form-control col-md-7 col-xs-12',
                'rows':1,
                'cols':15
            }),  
            "description_us": Textarea(attrs={                
                'class': 'form-control col-md-7 col-xs-12',
                'rows':1,
                'cols':15
            }),  
            "description_tr": Textarea(attrs={                
                'class': 'form-control col-md-7 col-xs-12',
                'rows':1,
                'cols':15
            }),
            "start_date": TextInput(attrs={
                'class': 'date-picker form-control col-md-7 col-xs-12',
                'placeholder': 'stock start date',
                'type' :"date"
            }),
            "start_date": TextInput(attrs={
                'class': 'date-picker form-control col-md-7 col-xs-12',
                'placeholder': 'stock start date',
                'type' :"date"
            }),
            "end_date": TextInput(attrs={
                'class': 'date-picker form-control col-md-7 col-xs-12',
                'placeholder': 'stock end date',
                'type' :"date"
            }),
        }
