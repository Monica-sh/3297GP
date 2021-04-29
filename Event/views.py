from django.shortcuts import render
from .models import PersonalEvent, PublicEvent
from Case.models import Case
from .forms import PersonalEventForm
# Create your views here.

def add_personal_event(request):
    if request.method == "GET":
        casepk = request.GET['pk']
        case = Case.objects.filter(pk=casepk)
        form = PersonalEventForm(case=case)
        return render(request, "personal_event_creat.html", {"form": form})
    else:
        