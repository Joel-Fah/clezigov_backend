from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html
from django.db import models
from .models import Availability, Category, Contact, Document, Image, Phone, Tag, Procedure


# Register your models here.
class CustomAdminFileWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        result = []
        if hasattr(value, "url"):
            result.append(
                f'''<a href="{value.url}" target="_blank">
                      <img 
                        src="{value.url}" alt="{value}" 
                        width="150" height="150"
                        style="object-fit: contain;"
                      />
                    </a>'''
            )
        result.append(super().render(name, value, attrs, renderer))
        return format_html("".join(result))


class AvailabilityAdmin(admin.ModelAdmin):
    model = Availability
    list_filter = ['date']
    search_fields = ['date']
    list_display = ['id', 'get_procedure_title', 'date', 'from_time', 'to_time', 'is_available']

    @admin.display(description='Procedure title', ordering='procedure__title')
    def get_procedure_title(self, obj):
        return obj.procedure.title


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['id', 'get_procedure_title', 'email', 'address']
    search_fields = ['email', 'address']
    list_filter = ['email', 'address']

    @admin.display(description='Procedure title', ordering='procedure__title')
    def get_procedure_title(self, obj):
        return obj.procedure.title


class DocumentAdmin(SummernoteModelAdmin):
    model = Document
    list_display = ['id', 'name', 'type']
    search_fields = ['name', 'description']
    list_filter = ['name', 'type']

    summernote_fields = ('description')

    formfield_overrides = {
        models.ImageField: {"widget": CustomAdminFileWidget}
    }


class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ['id', 'get_procedure_title']

    formfield_overrides = {
        models.ImageField: {"widget": CustomAdminFileWidget}
    }

    @admin.display(description='Procedure title', ordering='procedure__title')
    def get_procedure_title(self, obj):
        return obj.procedure.title

class PhoneAdmin(admin.ModelAdmin):
    model = Phone
    list_display = ['id', 'phone_number', 'is_whatsapp', 'is_calling', 'is_messaging']
    search_fields = ['phone_number']
    list_filter = ['phone_number']

class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ['id', 'name', 'get_procedure_title']
    search_fields = ['name']
    list_filter = ['name']

    @admin.display(description='Procedure title', ordering='procedure__title')
    def get_procedure_title(self, obj):
        return obj.procedure.title

class ProcedureAdmin(SummernoteModelAdmin):
    model = Procedure
    list_display = ['id', 'title', 'get_category_name', 'is_visible']
    search_fields = ['title', 'category']
    list_filter = ['title', 'category']

    summernote_fields = ('description')

    @admin.display(description='Category name', ordering='category__name')
    def get_category_name(self, obj):
        return obj.category.name

# Register in admin dashboard
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Procedure, ProcedureAdmin)
