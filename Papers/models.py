from django.db import models

formats = (
    ('Colored', 'Colored'),
    ('Black and White', 'Black and White'),
    ('Any', 'Any')
)

class Paper(models.Model):
    product = models.ForeignKey('Products.Product', models.CASCADE)
    format = models.CharField(max_length=100, choices=formats, null=True)
    Price = models.PositiveIntegerField()
    Prints = models.ManyToManyField('Printing.Printing')

    def __str__(self):
        return self.product.Name
