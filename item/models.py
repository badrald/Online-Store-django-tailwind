from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
        ordering = ['name']
        
class Item(models.Model):
    category= models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    image =models.ImageField(upload_to='items_images/%y/%m/%d',blank=True,null=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'item'
        verbose_name_plural = 'items'
    

