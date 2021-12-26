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

class goodSectionForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = good_section
        fields = ["good_id","section_name_uz", "section_name_ru", "section_name_us", "section_name_tr",] 
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


class goodSectionDescriptionForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = good_section_description
        fields = ["good_section_id","section_description_uz", "section_description_ru", "section_description_us", "section_description_tr"] 
        widgets = {
            "good_section_id": Select(attrs={
                'class': 'form-control col-md-7 col-xs-12',
            }),
            "section_description_uz": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'description for section',
            }),    
            "section_description_ru": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'description for section',
            }),    
            "section_description_us": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'description for section',
            }),    
            "section_description_tr": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'description for section',
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
        fields = ["company_icon", "company_short_info", "company_info"] 
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
        
        
# Info
class infosForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = info
        fields = ["sub_section", "comp_icon"] 
        widgets = {
            "sub_section": TextInput(attrs={
                'class': 'form-control col-md-7 col-xs-12',
                'placeholder': 'about company short info'
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
        fields = ["country", "country_icon", 
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
                'type' :"number"
            }),
            "export_year_before": TextInput(attrs={
                'class': 'date-picker form-control col-md-7 col-xs-12',
                'placeholder': 'stock end date',
                'type' :"date"
            }),
            "export_year_after": TextInput(attrs={
                'class': 'date-picker form-control col-md-7 col-xs-12',
                'placeholder': 'stock end date',
                'type' :"date"
            }),
        }


# ecology
class ecologyForm(ModelForm):
    """form for taking from fronend info & record to the base"""
    class Meta:
        model = ecology
        fields = ["ecology_img", "ecology_desc"]
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
        fields = ["innovation_img", "innovation_desc"]
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
        fields = ["product_bases_img", "product_bases_desc"]
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
        fields = ["service_city", "service_address_list", "service_phone"]
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