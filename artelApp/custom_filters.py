from django.contrib.admin import SimpleListFilter
# from .admin import get_list_display

class LanguageListFilter(SimpleListFilter):
    title = 'Языки'
    parameter_name = 'lang'
    
    def lookups(self, request, model_admin):
        
        return (
            ('title_uz', 'Узбексий'),
            ('title_ru', 'Русский'),
            ('title_us', 'Английский'),
            ('title_tr', 'Турецкий'),
        )
        
    def hide_field(self, *args):
        
        pass
    
    def queryset(self, request, queryset):
        if self.value() == 'title_uz':
            return queryset.filter(title_uz__isnull=False)
        if self.value() == 'title_ru':
            return queryset.filter(title_ru__isnull=False)
        if self.value() == 'title_us':
            return queryset.list_display(filter(title_us__isnull=False))
        if self.value() == 'title_tr':
            return queryset.filter(title_tr__isnull=True)