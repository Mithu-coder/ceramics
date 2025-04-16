from django.shortcuts import render,redirect
from store.models import fac_challan
from store.forms import fac_challan_form
# Create your views here.



def home(request):
    people=[{'name':'Mithu'},{'name':'Hasan'},{'name':'Abir'},{'name':'Ronju'}]
    return render(request,'home.html',{'all':people})

def show_all(request):
    x=fac_challan.objects.all()
    return render(request,'show_all.html',{'all':x})

# store/views.py


def challan_form(request):
    if request.method=="POST":
        form=fac_challan_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/fac_challan/')
    else:
        form=fac_challan_form()
    return render(request,'fac_challan_form.html',{'form':form})

