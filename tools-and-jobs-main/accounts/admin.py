from django.contrib import admin
from .models import User
# Register your models here.

admin.site.register(User)
class User(admin.ModelAdmin):
    list_display = ('email', 'username', 'company_name', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('email', 'username', 'company_name')
    list_filter = ('is_active', 'is_staff')
    ordering = ('date_joined',)

