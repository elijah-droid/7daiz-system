from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    current_branch = models.ForeignKey('Branches.Branch', models.SET_NULL, null=True, blank=True)
