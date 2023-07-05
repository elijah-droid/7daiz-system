from django.db import models
from django.utils.timezone import now


class Expense(models.Model):
    Branch = models.ForeignKey('Branches.Branch', models.CASCADE)
    Date = models.DateTimeField(default=now)
    Amount = models.PositiveIntegerField()
    Reason = models.CharField(max_length=100)