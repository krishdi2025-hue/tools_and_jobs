from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Engineering(models.Model):
    head = models.CharField(max_length=300)
    desc = RichTextField(blank=True,null=True)
    url = models.URLField()
    photo = models.ImageField(upload_to='pics')
    date_time = models.DateTimeField(auto_now=True)
    #read more field

    exper = models.CharField(max_length=30)
    vacc = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    sal = models.CharField(max_length=30)
    skil = models.CharField(max_length=1000)
    descr = RichTextField(blank=True,null=True)
    ind_type = models.CharField(max_length=100)
    func_area = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    empl_type = models.CharField(max_length=70)
    edu_or_elig = models.CharField(max_length=100)

    def __str__(self):
        return self.head


class Busi_Management_administration(models.Model):
    head6 = models.CharField(max_length=300)
    desc6 = RichTextField(blank=True,null=True)
    url6 = models.URLField()
    photo6 = models.ImageField(upload_to='pics')
    date_time6 = models.DateTimeField(auto_now=True)
    #read more field

    exper6 = models.CharField(max_length=30)
    vacc6 = models.CharField(max_length=100)
    loc6 = models.CharField(max_length=100)
    sal6 = models.CharField(max_length=30)
    skil6 = models.CharField(max_length=1000)
    descr6 = RichTextField(blank=True,null=True)
    ind_type6 = models.CharField(max_length=100)
    func_area6 = models.CharField(max_length=100)
    role6 = models.CharField(max_length=100)
    empl_type6 = models.CharField(max_length=70)
    edu_or_elig6 = models.CharField(max_length=100)

    def __str__(self):
        return self.head6


class Sales(models.Model):
    head8 = models.CharField(max_length=300)
    desc8 = RichTextField(blank=True,null=True)
    url8 = models.URLField()
    photo8 = models.ImageField(upload_to='pics')
    date_time8 = models.DateTimeField(auto_now=True)
    #read more field

    exper8 = models.CharField(max_length=30)
    vacc8 = models.CharField(max_length=100)
    loc8 = models.CharField(max_length=100)
    sal8 = models.CharField(max_length=30)
    skil8 = models.CharField(max_length=1000)
    descr8 = RichTextField(blank=True,null=True)
    ind_type8 = models.CharField(max_length=100)
    func_area8 = models.CharField(max_length=100)
    role8 = models.CharField(max_length=100)
    empl_type8 = models.CharField(max_length=70)
    edu_or_elig8 = models.CharField(max_length=100)

    def __str__(self):
        return self.head8

class Communication(models.Model):
    head9 = models.CharField(max_length=300)
    desc9 = RichTextField(blank=True,null=True)
    url9 = models.URLField()
    photo9 = models.ImageField(upload_to='pics')
    date_time1 = models.DateTimeField(auto_now=True)
    #read more field

    exper9 = models.CharField(max_length=30)
    vacc9 = models.CharField(max_length=100)
    loc9 = models.CharField(max_length=100)
    sal9 = models.CharField(max_length=30)
    skil9 = models.CharField(max_length=1000)
    descr9 = RichTextField(blank=True,null=True)
    ind_type9 = models.CharField(max_length=100)
    func_area9 = models.CharField(max_length=100)
    role9 = models.CharField(max_length=100)
    empl_type9 = models.CharField(max_length=70)
    edu_or_elig9 = models.CharField(max_length=100)

    def __str__(self):
        return self.head9