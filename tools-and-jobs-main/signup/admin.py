from django.contrib import admin
from .models import Signup,Contact

# Register your models here
class SignupAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','updated_on')
admin.site.register(Signup, SignupAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email1', 'updated_on')
admin.site.register(Contact,ContactAdmin)