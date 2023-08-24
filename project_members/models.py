from django.db import models
from projects.models import Project
from role_types.models import RoleType
from users.models import User


# Create your models here.
class ProjectMember(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE),
    member_id = models.ForeignKey(User, on_delete=models.CASCADE),
    role = models.ForeignKey(RoleType, on_delete=models.CASCADE),

    def __str__(self):
        return self.role
