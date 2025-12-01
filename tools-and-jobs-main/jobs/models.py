from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import User

# Create your models here.
class add_jobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=200, blank=False, null=False, default='')
    disctrict = models.CharField(max_length=100, default="")
    head = models.CharField(max_length=300)
    desc = RichTextField(blank=True,null=True)
    url = models.URLField()
    photo = models.ImageField(upload_to='pics')
    date_time = models.DateTimeField(auto_now=True)
    #read more field

    experience = models.CharField(max_length=30)
    vacancy = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=30)
    skill = models.CharField(max_length=1000)
    descr = RichTextField(blank=True,null=True)
    ind_type = models.CharField(max_length=100)
    func_area = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    empl_type = models.CharField(max_length=70)
    edu_or_elig = models.CharField(max_length=100)
    posted_by = models.ForeignKey('register.Company', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.head

    class Meta:
        db_table = 'add_jobs'