from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html
from django.db import models
from .models import Availability, Category, Contact, Document, Image


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


class DocumentAdmin(admin.ModelAdmin):
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


# Register in admin dashboard
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Document, DocumentAdmin)
