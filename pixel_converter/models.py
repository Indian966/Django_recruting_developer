from django.db import models

# Create your models here.
class ImageModel(models.Model) :
    org_image = models.ImageField(blank=True, upload_to='pixel_converter/img')
    result = models.ImageField(blank=True, upload_to='pixel_converter/results')
