from django.contrib import admin
from core.admin import CustomAdminFileWidget
from .models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass


# Register in admin dashboard
admin.register(Profile, ProfileAdmin)
