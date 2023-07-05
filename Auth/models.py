from django.db import models

class EmailConfirmation(models.Model):
    email = models.EmailField(max_length=1000)
    code = models.PositiveIntegerField()                                                 
