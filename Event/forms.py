from django import forms
from django.core.exceptions import ValidationError
from .models import PersonalEvent, PublicEvent
from .utils import DateUtils
import datetime

class PersonalEventForm(forms.Form):
    def __init__(self, case=None, *args, **kwargs):
        self.case = case
        super(PersonalEventForm, self).__init__(*args, **kwargs)
    name = forms.CharField(error_messages={"required":"Cannot be empty! "})
    location = forms.CharField(error_messages={"required":"Cannot be empty! "})
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), error_messages={"required":"Cannot be empty! "})
    description = forms.CharField(required=False)
    
    def clean_date(self):
        val = self.cleaned_data.get("date")

        if not DateUtils.in_between(val, self.case.Date_of_Symptoms + datetime.timedelta(days=-14), self.case.Date_of_Confirmation):
            raise ValidationError("Date out of range! ")
        else:
            print("validation passed! ")
            return val
    
    # def clean_location(self):
    #     # check whether the location can be found
    #     pass