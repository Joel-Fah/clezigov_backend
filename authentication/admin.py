from django.contrib import admin
from django.db import models
from authentication.models import Profile
from core.admin import CustomAdminFileWidget
from django_summernote.admin import SummernoteModelAdmin


class ProfileAdmin(SummernoteModelAdmin):
    model = Profile
    list_display = ['id', 'get_user_name', 'get_user_email', 'phone_number']
    search_fields = ['get_user_name']
    list_filter = ['date_of_birth']

    summernote_fields = 'bio'

    # formfield_overrides = {
    #     models.ImageField: {"widget": CustomAdminFileWidget}
    # }

    # get user's name
    @admin.display(description='User name', ordering='user__name')
    def get_user_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

    # get user's email
    @admin.display(description='User email', ordering='user__email')
    def get_user_email(self, obj):
        return obj.user.email


# Register in admin dashboard
admin.site.register(Profile, ProfileAdmin)
