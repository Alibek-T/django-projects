from django.db import models


# Create your models here.
class RoleType(models.Model):
    role_name = models.CharField(max_length=100),

    def __str__(self):
        return self.role_name
