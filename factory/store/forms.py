from django import forms 
from store.models import fac_challan

class fac_challan_form(forms.ModelForm):
    class Meta:
        model=fac_challan
        fields='__all__'

