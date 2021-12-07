from .models import *
from django.forms import ModelForm, TextInput, Textarea, Select, DateField


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
            "cat_id": Select(attrs={
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
