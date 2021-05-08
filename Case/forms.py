from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'Case_Number',
            'Person_name',
            'Identity_Document_Number',
            'Date_of_Birth',
            'Date_of_Symptoms',
            'Date_of_Confirmation',
        ]
        widgets = {
        'Date_of_Birth': forms.DateInput(attrs={'type':'date'}),
        'Date_of_Symptoms':forms.DateInput(attrs={'type':'date'}), 
        'Date_of_Confirmation':forms.DateInput(attrs={'type':'date'}), 
        }
    