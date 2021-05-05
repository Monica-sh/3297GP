from django.shortcuts import render, redirect
from .models import PersonalEvent, PublicEvent
from Case.models import Case
from .forms import PersonalEventForm
from django.contrib.auth.decorators import login_required
import json
import requests
# Create your views here.

@login_required(login_url = "login" )
def add_personal_event(request, pk):
    casepk = pk
    case = Case.objects.get(pk=casepk)
    if request.method == "GET":
        form = PersonalEventForm(case)
        return render(request, "personal_event_create.html", {"form": form})
    else:
        print("POST")
        print(request.POST)
        # form submitted
        form = PersonalEventForm(case, request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(case)
            events = PublicEvent.objects.filter(name=data["name"], location=data["location"], date=data["date"])
            # accounting for sse
            event = None
            ### Retrive data from api
            try:
                response = requests.get('https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?','q=' + data["location"])
                raw_data = {}
                raw_data = response.json()
                print(raw_data[0])
            except:
                return render(request, "personal_event_create.html", {"form": form})
            ###
            if len(events) == 0:
                add_public_event = {
                    'name': data['name'], 
                    'location': data["location"], 
                    'date': data["date"], 
                    'address' : raw_data[0]['addressEN'],
                    'xCoord' : raw_data[0]['x'],
                    'yCoord' : raw_data[0]['y'],
                    'number_of_cases': 1
                }
                event = PublicEvent.objects.create(**add_public_event) # not completed
            else:
                event = events[0]
                num = events[0].number_of_cases + 1
                PublicEvent.objects.filter(pk=event.pk).update(number_of_cases=num)

            add_personal_event = {
                    'event': event, 
                    'case': case, 
                    'description': data['description']
                }
            print(add_personal_event)
            PersonalEvent.objects.create(**add_personal_event)
            return redirect("../../case_detail?Case_Number=" + case.Case_Number)
        else:
            clear_errors = form.errors.get("__all__")
            return render(request, "personal_event_create.html", {"form": form, "clear_errors": clear_errors})