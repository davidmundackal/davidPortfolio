from django.db import models

# Create your models here.
class newEmp(models.Model):
    fullname = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phone = models.IntegerField()
    message = models.TextField()