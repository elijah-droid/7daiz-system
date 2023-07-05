from django.db import models

class EmailConfimation(models.Model):
    email = models.EmailField(max_length=1000)
    code = models.PositiveIntegerField()                                                 
