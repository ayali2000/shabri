from django.shortcuts import render,redirect
from . forms import *
from django.contrib import messages

# Create your views here.

def signup(request):
    frm = SignUpForm()
    if request.method == "POST":
        frm = SignUpForm(request.POST)
        if frm.is_valid():
            frm.save()
            frm.clean()
            messages.success(request,'Account created successfully')
            return redirect('login')
        else:
            messages.success(request,'Account not created. Password must be strong, at least 8 characters and must contain numbers,letters and symbols')                
    else:
        frm = SignUpForm()
    context = {'frm':frm}    
        
    return render(request,'users/signup.html',context)
