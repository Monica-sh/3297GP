from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView,CreateView,View

# Create your views here.
from .forms import CaseForm
from .models import Case
from Event.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class ResultView(LoginRequiredMixin, ListView):
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

'''
class CaseCreateView(View):
    form_class = CaseForm
    template_name = 'Case/templates/Case_form.html'

    def get (self,request):
        return render(request,self.template_name,{'form':self.form_class()})
    
    def post (self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_case = form.save()
            # new_case = Case.objects.get(pk=new_case_pk)
            return redirect("../../case_detail?Case_Number=" + new_case.Case_Number)
        else:
            return render(request,self.template_name,{'form':form})
'''

@login_required(login_url = "login")
def Case_Detail_View(request,pk):

    obj = Case.objects.get(id=pk)
    event_list = PersonalEvent.objects.filter(case = obj)

    Data = {
            'case': obj,
            'event_list': event_list,
    }

    return render(request,'../templates/case_detail.html', Data) #TODO: Monica connect to result page
