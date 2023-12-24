from django.db import models

formats = (
    ('Colored', 'Colored'),
    ('Black and White', 'Black and White'),
    ('Any', 'Any')
)

sizes = (
    ('A4', 'A4'),
    ('A3', 'A3'),
    ('A2', 'A2'),
    ('A1', 'A1')
)

class Paper(models.Model):
    product = models.ForeignKey('Products.Product', models.CASCADE)
    format = models.CharField(max_length=100, choices=formats, null=True)
    Price = models.PositiveIntegerField()
    Size = models.CharField(max_length=10, choices=sizes, null=True)
    Prints = models.ManyToManyField('Printing.Printing')

    def __str__(self):
        return f'{self.product.Name} {self.format}'
