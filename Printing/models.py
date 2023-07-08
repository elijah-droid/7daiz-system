from django.db import models
from django.utils.timezone import now

class Printing(models.Model):
    Branch = models.ForeignKey('Branches.Branch', models.CASCADE)
    Date = models.DateTimeField(default=now)
    Paper = models.ForeignKey('Papers.Paper', models.CASCADE)
    No_of_Papers = models.PositiveIntegerField()
    Amount_Paid = models.PositiveIntegerField()
