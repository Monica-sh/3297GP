from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView,CreateView,View

# Create your views here.
from .forms import CaseForm
from .models import Case
from Event.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class ResultView(LoginRequiredMixin,ListView):

    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = Case
    template_name = 'Case/templates/results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Case.objects.filter(Case_Number__icontains = query)
        return object_list 


@login_required(login_url = "login" )
def case_create_view(request):
    form = CaseForm(request.POST or None)
    if form.is_valid():
        new_case = form.save()
        form = CaseForm()
        context = {
        'form':form
        }
        return redirect("../../case_detail?Case_Number=" + new_case.Case_Number)
    else:
        return render(request,'Case/templates/Case_form.html',{'form':form})
