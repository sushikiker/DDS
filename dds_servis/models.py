from django import models
from sqlalchemy import ForeignKey

class DDS_record(models.Model):
  
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeingKey('category', on_delete = models.SET_NULL, null = True, blank = True)

class Status(models.Model):
    status_name = models.CharField(max_length=100)
     
    def __str__(self):
        return self.status_name

class Type(models.Model):
    type_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.type_name
    
class category(models.Model):
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name

class subcategory(models.Model):
    subcategory_name = models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='subcategories')
    
    def __str__(self):
        return self.subcategory_name