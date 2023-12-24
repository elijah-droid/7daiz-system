from django.db import models
from django.utils.timezone import now

colors = (
    ('Magenta', 'Magenta'),
    ('Cyan', 'Cyan'),
    ('Yellow', 'Yellow'),
    ('Black', 'Black')
)

types = (
    ('Solid Sticker', 'Solid Sticker'),
    ('One-way Sticker', 'One-way Sticker'),
    ('Banner', 'Banner'),
    ('Panaflex', 'Panaflex')
)

class Roll(models.Model):
    Type = models.CharField(max_length=100, choices=types)
    Width = models.FloatField(null=True)
    Price_per_sq_meter = models.IntegerField()
    Rolls_Available = models.IntegerField()
    Meters_Sold = models.FloatField(null=True, blank=True)
    Meters_Left = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.Type} {self.Width}'


class Ink(models.Model):
    Color = models.CharField(max_length=100, choices=colors)
    Bottles_Available = models.IntegerField()


class LargeformatPrinting(models.Model):
    Date = models.DateTimeField(default=now)
    Roll = models.ForeignKey('Roll', models.CASCADE)
    Width_Printed = models.FloatField(null=True, blank=True)
    Height_Printed = models.FloatField(null=True, blank=True)
    Amount_Paid = models.IntegerField(null=True, blank=True)
    Amount_Expected = models.IntegerField(null=True, blank=True)
    Total_Meters_Printed = models.FloatField(null=True, blank=True)
    Staff = models.ForeignKey('Employees.Employee', models.CASCADE, null=True, blank=True, related_name='employee_largeprint')

