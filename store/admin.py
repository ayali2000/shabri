from django.contrib import admin
from . models import *

# Register your models here.
class AdminItems(admin.ModelAdmin):
    list_display = ['Name','Category','Description','Location','Price','image','date_added','approved']
    
admin.site.register(Items,AdminItems)

class AdminOrderItem(admin.ModelAdmin):
    list_display = ['Name','Phone_num','Address','product_name','Quantity','date','delivered']
    
admin.site.register(OrderItem,AdminOrderItem)


