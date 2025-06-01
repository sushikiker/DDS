from django.db import models
from sqlalchemy import ForeignKey

class DDS_record(models.Model):
  
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('category', on_delete = models.SET_NULL, null = True, blank = True)
    summ = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

class Status(models.Model):
    status_name = models.CharField(max_length=100)
     
    def __str__(self):
        return self.status_name

class Type(models.Model):
    type_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.type_name
    
class category(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories')
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name

class subcategory(models.Model):
    subcategory_name = models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='subcategories')
    
    def __str__(self):
        return self.subcategory_name