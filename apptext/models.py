from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    mobile = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255)
    medicine = HTMLField(null=True)
    date = models.CharField(max_length=200,null=True)
    time = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name