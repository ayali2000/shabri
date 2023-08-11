from email.policy import default
from enum import auto
from django.db import models

# Create your models here.

class Items(models.Model):
    Name = models.CharField(max_length=100)
    Cat = [
        ('Choose item category','Choose item category'),
        ('Phones','Phones'),
        ('Health','Health'),
        ('Wears','Wears'),
        ('Others','Others'),
    ]
    Category = models.CharField(max_length=50, choices=Cat,default='Choose item category')
    Description = models.CharField(max_length=500)
    Location = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to = 'products')
    approved = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return str(self.Name)
    
    class Meta:
        ordering = ['-date_added']
    
    def phonecat(self):
        return self.Category == "Phones"
        
    def cat1(self):
        return self.Category == "Health"
    
    def cat2(self):
        return self.Category == "Wears"
    
    def cat3(self):
        return self.Category == "Others"
    
    
class OrderItem(models.Model):
    Item_id = models.ForeignKey(Items,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    Phone_num = models.CharField(max_length=15)
    Quantity = models.PositiveIntegerField(default=1)
    Address = models.TextField()
    delivered = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return str(self.Name)
        
    class Meta:
        ordering = ['-date']
    
