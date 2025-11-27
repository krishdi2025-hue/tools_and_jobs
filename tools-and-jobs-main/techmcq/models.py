from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Category(models.Model):
    name = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name


class TechMCQ(models.Model):
    titles1 = models.CharField(max_length=300, unique=True)
    slug1 = models.SlugField(max_length=300, unique=True)
    desc = models.CharField(max_length=170,null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,default=1)
    photos1 = models.ImageField(upload_to='pics', blank=True, default='pics/autocad-engifree.jpg')
    
    contents1 = RichTextUploadingField(blank=True, null=True) ###############
    updated_on1 = models.DateTimeField(auto_now=True)
    created_on1 = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

#schema data models starts here
    age_range = models.CharField(blank=True, null=True, max_length=15)
    asseses = models.CharField(blank=True, null=True, max_length=200)

    target_name1 = models.CharField(blank=True, null=True, max_length=35)
    target_name2 = models.CharField(blank=True, null=True, max_length=35)
    name = models.CharField(blank=True, null=True, max_length=200)
    about_name = models.CharField(blank=True, null=True, max_length=150)

    # question
    que_name1 = models.CharField(blank=True, null=True, max_length=150)
    que_text1 = models.CharField(blank=True, null=True, max_length=320)
    que_hint1 = models.CharField(blank=True, null=True, max_length=100)

    # incorrect options
    ans_text0 = models.CharField(blank=True, null=True, max_length=150)
    ans_hint0 = models.CharField(blank=True, null=True, max_length=100)

    ans_text1 = models.CharField(blank=True, null=True, max_length=150)
    ans_hint1 = models.CharField(blank=True, null=True, max_length=100)

    ans_text2 = models.CharField(blank=True, null=True, max_length=150)
    ans_hint2 = models.CharField(blank=True, null=True, max_length=100)

    # correct answer
    accepted_text1 = models.CharField(blank=True, null=True, max_length=150)
    accepted_hint1 = models.CharField(blank=True, null=True, max_length=100)

    # ans explanation of only 2nd que
    ans_exp = models.CharField(blank=True, null=True, max_length=200)

    # 2nd question
    que_name2 = models.CharField(blank=True, null=True, max_length=150)
    que_text2 = models.CharField(blank=True, null=True, max_length=320)
    que_hint2 = models.CharField(blank=True, null=True, max_length=100)

    # incorrect options for 2nd que
    ans_text00 = models.CharField(blank=True, null=True, max_length=150)
    ans_hint00 = models.CharField(blank=True, null=True, max_length=100)

    ans_text11 = models.CharField(blank=True, null=True, max_length=150)
    ans_hint11 = models.CharField(blank=True, null=True, max_length=100)

    ans_text22 = models.CharField(blank=True, null=True, max_length=150)
    ans_hint22 = models.CharField(blank=True, null=True, max_length=100)

    # correct answer for 2nd que
    accepted_text11 = models.CharField(blank=True, null=True, max_length=150)
    accepted_hint11 = models.CharField(blank=True, null=True, max_length=100)

    # ans explanation of only 2nd que
    ans_expl = models.CharField(blank=True, null=True, max_length=200)
# schema data models finish here

    class Meta:
        ordering = ['-created_on1']

    def __str__(self):
        return self.titles1

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("test_detail", kwargs={"slug1": str(self.slug1)})







