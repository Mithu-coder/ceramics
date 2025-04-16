from django.urls import path
from .views import show_all,challan_form,home

urlpatterns=[
    path('fac_challan/',show_all,name='show_all'),
    path('challan_form/',challan_form, name='challan_form'),
    path('home/',home, name='home'),
]
