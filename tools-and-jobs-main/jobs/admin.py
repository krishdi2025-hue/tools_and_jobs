from django.contrib import admin
from django.utils.html import strip_tags
from .models import add_jobs

@admin.register(add_jobs)
class add_jobsAdmin(admin.ModelAdmin):
    # adjust this tuple to match the columns you actually want
    list_display = (
        'id', 'company_name', 'disctrict', 'head',
        'short_description', 'url', 'photo', 'date_time',
        'experience', 'vacancy', 'location', 'salary', 'skill'
    )

    def short_description(self, obj):
        """
        Safe description preview:
        - tries multiple possible field names
        - strips HTML to avoid showing raw tags
        - truncates long text
        - never raises AttributeError
        """
        candidate_names = ('description', 'desc', 'descr', 'details', 'job_description', 'description_text')
        for name in candidate_names:
            # getattr returns None if attribute not present
            val = getattr(obj, name, None)
            if val:
                # val may be a RichTextField (HTML) or plain text
                try:
                    text = strip_tags(val)
                except Exception:
                    # fallback if strip_tags can't handle the value type
                    text = str(val)
                return (text[:150] + '...') if len(text) > 150 else text

        # nothing found — return empty string (keeps admin list tidy)
        return ''

    short_description.short_description = 'Description'


# from django.contrib import admin
# from .models import add_jobs

# @admin.register(add_jobs)
# class JobAdmin(admin.ModelAdmin):
#     list_display = ('title','posted_by','created_at')
#     list_filter = ('created_at',)
#     search_fields = ('title','description','posted_by__username')