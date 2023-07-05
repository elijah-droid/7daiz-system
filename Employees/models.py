from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    Branch = models.ForeignKey('Branches.Branch', models.CASCADE)
