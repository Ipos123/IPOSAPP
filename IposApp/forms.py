from .models import RTable,Register,RmUsed
from django import  forms

from django.forms import ModelChoiceField

class ProfileForm(forms.ModelForm):
    # CustomerName=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'size': '90'}))
    # MobileNumber = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # NoOfPerson = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # SelectTable = forms.ModelChoiceField(queryset=RTable.objects.all(),required=True, empty_label='Select the Table',widget=forms.Select(attrs={
    #   'class': 'form-control select-access-open select2-hidden-accessible'
    #   }))
    # TokenIn=forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'],
    #          widget = forms.DateTimeInput(
    #              attrs={'type': 'datetime-local'},
    #              format='%I:%M %p %d-%b-%Y'))
    class Meta:
        model =Register
        fields ='__all__'




