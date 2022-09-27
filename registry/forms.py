from .models import *
from django import forms

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username','bio','contact','avatar']

class ReportModelForm(forms.ModelForm):
   
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3} ))
   

    class Meta:
        model = Report
        fields = ['report_name','description','image']  