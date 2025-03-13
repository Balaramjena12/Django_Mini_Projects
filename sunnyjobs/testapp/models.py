from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    eligibility = models.CharField(max_length=30)
    address = models.CharField(max_length=64)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
