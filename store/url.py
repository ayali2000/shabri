from django.urls import path
from . views import *

urlpatterns = [
    path('',genindex,name='genindex'),
    path('store/',index,name='store'),
    path('products/<int:pk>/',detail,name='phone_detail'),
    path('sell/',sell,name='sell'),
    path('Phone/',phone,name='cat'),
    path('accessories/',access,name='access'),
    path('foot_wears/',sneaker,name='sneaker'),
    path('others/',others,name='others'),
]
