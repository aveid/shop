from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'self', related_name='cat',
        on_delete=models.CASCADE, verbose_name='Category parent',
        blank=True, null=True
)

    def __str__(self):
        return f'{self.name}'

