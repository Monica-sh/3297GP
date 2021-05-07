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
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home_page')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render (request,'User/templates/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url = "login" )
def home_view(request,*args,**kwargs):
    context = {}
    return render(request,'home.html',context)

class ResultView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
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