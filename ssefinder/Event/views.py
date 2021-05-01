from django.shortcuts import render, redirect
from .models import PersonalEvent, PublicEvent
from Case.models import Case
from .forms import PersonalEventForm
# Create your views here.

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
            if len(events) == 0:
                add_public_event = {
                    'name': data['name'], 
                    'location': data["location"], 
                    'date': data["date"], 
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