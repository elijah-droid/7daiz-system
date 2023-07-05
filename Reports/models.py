from django.db import models
from django.utils.timezone import now

class Report(models.Model):
    Branch = models.ForeignKey('Branches.Branch', models.CASCADE)
    Date = models.DateTimeField(default=now)
    Sales = models.PositiveIntegerField(null=True)
    Printing = models.PositiveIntegerField(null=True)
    Grand_Total = models.PositiveIntegerField()
    Cash_Taken = models.PositiveIntegerField(null=True)
    Balance = models.PositiveIntegerField(null=True)

