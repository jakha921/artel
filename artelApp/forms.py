from .models import *
from django.forms import ModelForm, TextInput, Textarea, ImageField


class categoryForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = categories
        fields = ["cat_name_uz", "cat_name_ru", "cat_name_us", "cat_name_tr", "cat_img"]     # "cat_img" do not work add with this 
        widgets = {
            "cat_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the category name'
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
            "cat_id": TextInput(attrs={
                'class': 'form-control',
            }),   
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title of good'
            }),   
            "specif": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'specification'
            }),   
            "good_info": Textarea(attrs={
                "class" : "form-control",
                'placeholder': 'Enter the category name',
                'rows':4,
                'cols':15
            }),    
        }