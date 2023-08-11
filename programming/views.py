from django.shortcuts import render

# Create your views here.

def proHome(request):
    return render(request,'programming/programmingPage.html')
