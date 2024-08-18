from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from core.admin import CustomAdminFileWidget
from .models import CustomUser, Profile
from django_summernote.admin import SummernoteModelAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['is_staff', 'is_active']

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

    # readonly_fields = ['date_joined']

    ordering = ('email',)


class ProfileAdmin(SummernoteModelAdmin):
    model = Profile
    list_display = ['id', 'get_user_name', 'get_user_email', 'phone_number']
    search_fields = ['get_user_name']
    list_filter = ['date_of_birth']

    summernote_fields = 'bio'

    formfield_overrides = {
        models.ImageField: {"widget": CustomAdminFileWidget}
    }

    # get user's name
    @admin.display(description='User name', ordering='user__name')
    def get_user_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

    # get user's email
    @admin.display(description='User email', ordering='user__email')
    def get_user_email(self, obj):
        return obj.user.email


# Register in admin dashboard
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
