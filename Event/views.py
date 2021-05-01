from django.shortcuts import render
from .models import PersonalEvent, PublicEvent
from Case.models import Case
from .forms import PersonalEventForm
# Create your views here.

def add_personal_event(request, pk):
    if request.method == "GET":
        casepk = pk
        case = Case.objects.get(pk=casepk)
        form = PersonalEventForm(case=case)
        return render(request, "personal_event_create.html", {"form": form}, pk=casepk)
    else:
        # form submitted
        form = PersonalEventForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            casepk = pk
            case = Case.objects.get(pk=casepk)
            events = PublicEvent.objects.filter(name=data["name"], location=data["location"], date=data["date"])
            # accounting for sse
            event = None
            if len(events) == 0:
                event = PublicEvent.objects.create() # not completed
            else:
                event = events[0]
                num = events[0].number_of_cases + 1
                events[0].update(number_of_cases=num)
            PersonalEvent.objects.create(**{
                'event': event, 
                'case': case, 
                'description': data['description']
            })
            return redirect("./")
        else:
            clear_errors = form.errors.get("__all__")
            return render(request, "personal_event_create.html", {"form": form, "clear_errors": clear_errors})