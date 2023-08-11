from django.shortcuts import redirect, render
from django.contrib import messages
from store.forms import OrederForm, SellForm
from . models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def genindex(request):
    return render(request,'general/index.html')

def index(request):
    all_prods = Items.objects.all().exclude(approved=False)
    all_phones = Items.objects.filter(Category='Phones').exclude(approved=False)[:10]
    all_health = Items.objects.filter(Category='Health').exclude(approved=False)[:10]
    all_wears = Items.objects.filter(Category='Wears').exclude(approved=False)[:10]
    others = Items.objects.filter(Category='Others').exclude(approved=False)[:10]
    if request.method == "GET":
        query = request.GET.get("q")
        queryset = Q(Name__icontains=query)|Q(Description__icontains=query)
        if query:
            result = Items.objects.filter(queryset) 
        else:
            result = all_prods
    context = {'all_prods':all_prods,
            'all_phones':all_phones,
            'query':query,
            'all_health':all_health,
            'others':others,
            'all_wears':all_wears,
            'queryset':queryset,
            'result':result}
    return render(request,'store/index.html',context)

def detail(request,pk):
    item = Items.objects.get(pk=pk)
    Ord_Form = OrederForm()
    context = {
        'Ord_Form':Ord_Form,
        'item':item
    }
    if request.method == "POST":
        Ord_Form = OrederForm(request.POST)
        if Ord_Form.is_valid():
            instance = Ord_Form.save(commit=False)
            instance.product_name = item.Name
            instance.Item_id = item
            instance.save()
            messages.success(request,'Item ordered. We will contact you')
            return render(request,'store/detail.html',context)
        else:
            for error in Ord_Form.errors:
                print(error)
            Ord_Form = OrederForm()
    return render(request,'store/detail.html',context)
    

@login_required
def sell(request):
    frm = SellForm()
    if request.method == "POST" and request.FILES:
        img = request.POST.get('image')
        frm = SellForm(request.POST,request.FILES)
        if frm.is_valid():
            instance=frm.save(commit=False)
            instance.image = "products/"+ img
            instance.save()
            messages.success(request,'Item posted')
            return redirect('sell')
        else:
            messages.error(request,'Item not posted')
            frm = SellForm()
    context = {'frm':frm}    
    return render(request,'store/sell.html',context)    

def phone(request):
    cat_prods = Items.objects.all()
    if request.method == "GET":
        query = request.GET.get("q")
        queryset = Q(Name__icontains=query)|Q(Description__icontains=query)
        if query:
            result = Items.objects.filter(queryset) 
        else:
            result = cat_prods
    context = {'cat_prods':cat_prods,
               'query':query,
               'queryset':queryset,
               'cat_prods':cat_prods,
               'result':result
               }

    return render(request,'store/phone.html',context)


def access(request):
    cat_prods = Items.objects.all()
    if request.method == "GET":
        query = request.GET.get("q")
        queryset = Q(Name__icontains=query)|Q(Description__icontains=query)
        if query:
            result = Items.objects.filter(queryset) 
        else:
            result = cat_prods
    context = {'cat_prods':cat_prods,
               'query':query,
               'queryset':queryset,
               'cat_prods':cat_prods,
               'result':result
               }

    return render(request,'store/access.html',context)

def sneaker(request):
    cat_prods = Items.objects.all()
    if request.method == "GET":
        query = request.GET.get("q")
        queryset = Q(Name__icontains=query)|Q(Description__icontains=query)
        if query:
            result = Items.objects.filter(queryset) 
        else:
            result = cat_prods
    context = {'cat_prods':cat_prods,
               'query':query,
               'queryset':queryset,
               'cat_prods':cat_prods,
               'result':result
               }

    return render(request,'store/sneakers.html',context)


def others(request):
    cat_prods = Items.objects.all()
    if request.method == "GET":
        query = request.GET.get("q")
        queryset = Q(Name__icontains=query)|Q(Description__icontains=query)
        if query:
            result = Items.objects.filter(queryset) 
        else:
            result = cat_prods
    context = {'cat_prods':cat_prods,
               'query':query,
               'queryset':queryset,
               'cat_prods':cat_prods,
               'result':result
               }

    return render(request,'store/others.html',context)
