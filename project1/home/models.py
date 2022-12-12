from django.db import models

# Create your models here.
class Doc(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class detail(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='detailsimg')

class feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    
