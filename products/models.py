from django.db import models
from category.models import Category


class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products_images')
    price = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category,
                                 related_name='categories',
                                 on_delete=models.CASCADE
                                 )
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


