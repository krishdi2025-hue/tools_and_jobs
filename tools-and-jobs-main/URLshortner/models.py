from django.db import models

# Create your models here.
class Route(models.Model):
    original_url = models.URLField(help_text= "Add the original URL that you want to shorten.")
    key = models.CharField(unique= True, max_length=30, help_text= "Add your words to shorten URL with.")

    def __str__(self):
        return f"{self.key}"
