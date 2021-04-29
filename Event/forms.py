from django import forms
from django.core.exceptions import ValidationError
from .models import PersonalEvent, PublicEvent
from .utils import DateUtils
import datetime

class PersonalEventForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.case = kwargs.pop('case')
        super().__init__(*args, **kwargs)
    name = forms.CharField(error_messages={"required":"Cannot be empty! "})
    location = forms.CharField(error_messages={"required":"Cannot be empty! "})
    date = forms.DateField(error_messages={"required":"Cannot be empty! "})
    description = forms.CharField(required=False)
    
    def clean_date(self):
        val = self.cleaned_data.get("date")

        if not DateUtils.in_between(val, case.Date_of_Symptons + datetime.timedelta(days=-14), case.Date_of_Confirmation):
            ValidationError("Date out of range! ")
        else:
            return val
    
    # def clean_location(self):
    #     # check whether the location can be found
    #     pass