from django.contrib import admin
from .models import add_jobs

class add_jobsAdmin(admin.ModelAdmin):
    list_display = ('head', 'date_time', 'url', 'exper', 'vacc', 'loc', 'sal', 'skil', 'ind_type', 'func_area', 'role', 'empl_type', 'edu_or_elig')

admin.site.register(add_jobs, add_jobsAdmin)
