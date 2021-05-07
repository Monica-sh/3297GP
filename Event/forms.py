from django import forms
from django.core.exceptions import ValidationError
from .models import PersonalEvent, PublicEvent
from .utils import DateUtils
import datetime
from .utils import APISender, APIBuilder

class PersonalEventForm(forms.Form):
    def __init__(self, case=None, *args, **kwargs):
        self.case = case
        super(PersonalEventForm, self).__init__(*args, **kwargs)
    name = forms.CharField(label="Event Name", error_messages={"required":"Cannot be empty! "})
    location = forms.CharField(label="Event Venue", error_messages={"required":"Cannot be empty! "})
    address = forms.CharField(required=False, widget = forms.HiddenInput())
    xCoord = forms.FloatField(required=False, widget = forms.HiddenInput())
    yCoord = forms.FloatField(required=False, widget = forms.HiddenInput())
    date = forms.DateField(label="Event Date", widget=forms.DateInput(attrs={'type':'date'}), error_messages={"required":"Cannot be empty! "})
    description = forms.CharField(required=False)
    
    def clean_date(self):
        val = self.cleaned_data.get("date")

        if not DateUtils.in_between(val, self.case.Date_of_Symptoms + datetime.timedelta(days=-14), self.case.Date_of_Confirmation):
            raise ValidationError("Date out of range! ")
        else:
            print("validation passed! ")
            return val
    
    def clean(self):
        '''check whether the location can be found'''
        super(forms.Form, self).clean()
        location = self.cleaned_data.get("location")
        ok, response = APISender.send_request(APIBuilder(location))  # send api query
        if not ok:
            raise ValidationError("GeoData Retrieval failed, please submit again! ")
        elif len(response) == 0:
            raise ValidationError("GeoData not found, please check the location name! ")
        else:
            r = response[0]
            self.cleaned_data['address'] = r['addressEN']
            self.cleaned_data['xCoord'] = r['x']
            self.cleaned_data['yCoord'] = r['y']
            print("GeoData Retrieval passed! ")
            return self.cleaned_data