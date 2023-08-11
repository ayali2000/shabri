from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder':'username'
    }))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'email'
    }))
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'First name'
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Last name'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'password'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'comfirm password'
    }))
    
    