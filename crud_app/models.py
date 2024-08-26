from django.db import models

# Create your models here.
class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=100)
    joined_date = models.DateField(null=True)
