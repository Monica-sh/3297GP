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
            'Date_of_Symptons',
            'Date_of_Confirmation',
        ]
    
    '''def clean_Case_Number(self):
        return self.cleaned_data['Case_Number'].upper()'''