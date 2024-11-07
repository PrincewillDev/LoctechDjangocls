from django.db import models

# Create your models here.
class FeedBack(models.Model):
    id = models.IntegerField(primary_key=True, blank=None)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    designation = models.CharField(max_length=70)
    feedback = models.CharField(max_length= 255)
