from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Mac', 'Mac'),
        ('iPad', 'iPad'),
        ('iPhone', 'iPhone'),
        ('Watch', 'Watch'),
        ('Music', 'Music'),
        ('TV & Home', 'TV & Home'),
        ('Accessories', 'Accessories'),
        ('Services', 'Services'),
        ('Offers', 'Offers'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    color = models.CharField(max_length=50, null=True, blank=True)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Mac')

    def __str__(self):
        return self.name
