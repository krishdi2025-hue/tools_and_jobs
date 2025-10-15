from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Engifree(models.Model):
    img = models.ImageField(upload_to='pics')
    text = RichTextField(blank=True,null=True)
    title = models.CharField(max_length=3000)
    tex = RichTextField(blank=True,null=True)
    link = models.URLField()
    date_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title










class Learnfree(models.Model):
    img5 = models.ImageField(upload_to='pics')
    text5 = RichTextField(blank=True,null=True)
    title5 = models.CharField(max_length=300)
    tex5 = RichTextField(blank=True,null=True)
    link5 = models.URLField()
    date_time5 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title5

