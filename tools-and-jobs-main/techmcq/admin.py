from django.contrib import admin
from .models import TechMCQ, Category

# Register your models here.
admin.site.register(Category)


class TechMCQAdmin(admin.ModelAdmin):
    list_display = ('titles1', 'slug1', 'status','created_on1')
    list_filter = ("status",)
    search_fields = ['titles1', 'contents1']
    prepopulated_fields = {'slug1': ('titles1',)}
admin.site.register(TechMCQ,TechMCQAdmin)

