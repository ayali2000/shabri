from django.urls import path
from . views import *

urlpatterns = [
    path('',allblogs,name='blog'),
    path('<int:pk>/',detail,name='detail'),
]