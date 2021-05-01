from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import TemplateView
from Case.models import *
from Event.models import *

import urllib 
import requests
import json
import datetime

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class ResultView(TemplateView):
    template_name = 'case_detail.html'

    def get_context_data(self, **kwargs): 
        case = self.get_queryset()
        context = super().get_context_data(**kwargs)
       
        context["case"] = case
        
        context["event_list"] = PersonalEvent.objects.filter(case = case)
    
        return context

        """
        context Info for front-end:
            case object
                Case_Number
                Person_name
                Identity_Document_Number
                Date_of_Birth
                Date_of_Symptons
                Date_of_Confirmation
            event_list QuerySet >
                elements as PersonalEvent (go through as list)
                    description
                    event (PublicEvent)
                        name
                        location
                        address
                        xCoord
                        yCoord
                        date
        """

    def get_queryset(self):
        search_Case_Number = self.request.GET.get('Case_Number') # with html: search box input case number

        try:
            case = Case.objects.get(Case_Number = search_Case_Number)
            return case
        except ObjectDoesNotExist:
            # no case with this number: raise error #TODO
            raise Warning("No case found")
            return None