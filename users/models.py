from django.db import models


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=100),
    lastname = models.CharField(max_length=200),
    age = models.IntegerField(null=True),
    password = models.CharField(max_length=200),
    email = models.CharField(max_length=200),

    def __str__(self):
        return self.firstname
