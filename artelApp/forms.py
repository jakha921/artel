from .models import categories, goods, good_section, good_images, company, innovations, product_bases, exports, stocks, \
                    stocks, partners, services, ecology
from django.forms import ModelForm, TextInput, Textarea, Select
from django.contrib.postgres.forms import SimpleArrayField
from django.forms.fields import CharField
from django.forms.widgets import Textarea


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
        }
        

class goodImageForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = good_images
        fields = ["good_id", "good_img", "good_badge"] 
        widgets = {
            "good_id": Select(attrs={
                'class': 'form-control col-md-7 col-xs-12',
            }),   
        }

# goodSection

class goodSectionForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    section_name_uz = SimpleArrayField(CharField(), delimiter='</>', widget=Textarea())
    section_name_ru = SimpleArrayField(CharField(), delimiter='</>', widget=Textarea())
    section_name_us = SimpleArrayField(CharField(), delimiter='</>', widget=Textarea())
    section_name_tr = SimpleArrayField(CharField(), delimiter='</>', widget=Textarea())
    section_description_uz = SimpleArrayField(CharField(), delimiter='</>', widget=Textarea())
    section_description_ru = SimpleArrayField(CharField(), delimiter='</>', widget=Textarea())
    section_description_us = SimpleArrayField(CharField(), delimiter='</>', widget=Textarea())
    section_description_tr = SimpleArrayField(CharField(), delimiter='</>', widget=Textarea())
    

    class Meta:
        model = good_section
        fields = ["good_id",
                    "section_name_uz", "section_name_ru", "section_name_us", "section_name_tr", 
                    "section_description_uz", "section_description_ru", "section_description_us", "section_description_tr"]
        widgets = {
            "good_id": Select(attrs={
                'class': 'form-control col-md-7 col-xs-12',
            }),
            "section_name_uz": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'specification name'
            }),  
            "section_name_ru": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'specification name'
            }),   
            "section_name_us": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'specification name'
            }),   
            "section_name_tr": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'specification name'
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


# company
class companiesForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = company
        # fields = ["company_icon", "company_short_info", "company_info"] 
        fields = '__all__'
        widgets = {
            "company_short_info": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'about company short info'
            }),
            "company_info": Textarea(attrs={                
                'class': 'form-control col-md-7 col-xs-12',
                'rows':1,
                'cols':15
            }),
        }


# partners
class partnerForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = partners
        fields = ["partner_img"] 


# exports
class exportForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = exports
        fields = ['country_uz', 'country_ru', 'country_us', 'country_tr', "country_icon", 
                    "description_uz", "description_ru", "description_us", "description_tr",
                    "export_percent_before", "export_percent_after", 
                    "export_year_before", "export_year_after"
                    ]
        widgets = {
            "country": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Enter country name'
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
            "export_percent_before": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Export number',
                'type' :"number"
            }),
            "export_percent_after": TextInput(attrs={
                'class': 'date-picker form-control col-md-7 col-xs-12',
                'placeholder': 'stock start date',
            }),
            "export_year_before": TextInput(attrs={
                'class': 'date-picker form-control col-md-7 col-xs-12',
                'placeholder': 'stock end date',
                'type' :"date"
            }),
            "export_year_after": TextInput(attrs={
                'class': 'date-picker form-control col-md-7 col-xs-12',
                'placeholder': 'stock end date',
            }),
        }


# ecology
class ecologyForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = ecology
        fields = ["ecology_img", 'ecology_desc_uz', 'ecology_desc_ru', 'ecology_desc_us', 'ecology_desc_tr',]
        widgets = {
            "ecology_desc": Textarea(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'rows':1,
                'cols':15
            }),
        }


# innovation
class innovationForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = innovations
        fields = ["innovation_img", 'innovation_desc_uz', 'innovation_desc_ru', 'innovation_desc_us', 'innovation_desc_tr', ]
        widgets = {
            "innovation_desc": Textarea(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'rows':1,
                'cols':15
            }),
        }


# productBases
class productBaseForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = product_bases
        fields = ["product_bases_img", 'product_bases_desc_uz', 'product_bases_desc_ru', 'product_bases_desc_us', 'product_bases_desc_tr',]
        widgets = {
            "product_bases_desc": Textarea(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'rows':1,
                'cols':15
            }),
        }


# services
class serviceForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = services
        fields = [ 'service_city_uz', 'service_city_ru', 'service_city_us', 'service_city_tr',
                    'service_address_list_uz', 'service_address_list_ru', 'service_address_list_us', 'service_address_list_tr',
                    "service_phone" ]
        widgets = {
            "service_city": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'service city name'
            }), 
            "service_address_list": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'service region name(exp: "Chilonzor, Oqtepa and etc")'
            }),
            "service_phone": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'Service number',
                'type' :"number"
            }),   
        }