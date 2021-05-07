from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import PersonalEvent, PublicEvent
from Case.models import Case
from .forms import PersonalEventForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
import datetime
from .utils import SSEPersonalEventData
# Create your views here.

@login_required(login_url = "login" )
def add_personal_event(request, pk):
    casepk = pk
    case = Case.objects.get(pk=casepk)
    if request.method == "GET":
        form = PersonalEventForm(case)
        return render(request, "personal_event_create.html", {"form": form})
    else:
        # form submitted
        form = PersonalEventForm(case, request.POST)
        if form.is_valid():
            data = form.cleaned_data
            events = PublicEvent.objects.filter(name=data["name"], location=data["location"], date=data["date"])
            # accounting for sse
            event = None
            if len(events) == 0:
                add_public_event = {
                    'name': data['name'], 
                    'location': data["location"], 
                    'date': data["date"], 
                    'address' : data['address'],
                    'xCoord' : data['xCoord'],
                    'yCoord' : data['yCoord'],
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
            PersonalEvent.objects.create(**add_personal_event)
            return redirect("../../case_detail?Case_Number=" + case.Case_Number)
        else:
            clear_errors = form.errors.get("__all__")
            return render(request, "personal_event_create.html", {"form": form, "clear_errors": clear_errors})


class SSEResultsListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = PublicEvent
    template_name = 'sse_results.html'

    # override this method
    def get_queryset(self):
        try:
            start_date = datetime.datetime.strptime(self.request.GET.get('StartDate'), '%Y-%m-%d')
        except:
            start_date = datetime.datetime(1997, 1, 1)

        try:
            end_date = datetime.datetime.strptime(self.request.GET.get('EndDate'), '%Y-%m-%d')
        except:
            end_date = datetime.datetime.now()
        object_list = PublicEvent.objects.filter(date__range=(start_date, end_date), number_of_cases__gt=6)
        return object_list


class SSEDetailListView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    template_name = 'sse_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        public_event = PublicEvent.objects.get(pk=self.kwargs['pk'])
        context['public_event'] = public_event
        personal_event_list = PersonalEvent.objects.filter(event=public_event)
        context['personal_event_data_list'] = SSEPersonalEventData.list_convert(personal_event_list)
        return context