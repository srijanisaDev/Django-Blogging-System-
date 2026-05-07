from django.db import models

# Create your models here.

class Category(models.Model):   ## the category will be automatically written as Categorys to change that we use meta
    category_name = models.CharField(max_length=50 , unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField( auto_now=False)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name    
