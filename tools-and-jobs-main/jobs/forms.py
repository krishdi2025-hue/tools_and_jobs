from django import forms
from .models import add_jobs
from ckeditor.widgets import CKEditorWidget

class add_jobsForm(forms.ModelForm):    
    class Meta:
        model = add_jobs
        fields = '__all__'  
        widgets = {
            'desc': CKEditorWidget(),
            'descr': CKEditorWidget(),
            # add others as needed
        }
