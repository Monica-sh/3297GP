from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView,CreateView,View

# Create your views here.
from .forms import CaseForm
from .models import Case
from Event.models import *


class ResultView(ListView):
    model = Case
    template_name = 'Case/templates/results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Case.objects.filter(Case__icontains = query)
        return object_list

class CaseCreateView(View):
    form_class = CaseForm
    template_name = 'Case/templates/Case_form.html'

    def get (self,request):
        return render(request,self.template_name,{'form':self.form_class()})
    def post (self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_case = form.save()
            return redirect(new_case)
        else:
            return render(request,self.template_name,{'form':form})

def Case_Detail_View(request,pk):

    obj = Case.objects.get(id=pk)
    event_list = PersonalEvent.objects.filter(case = obj)

    # Case_Number = obj.Case_Number
    # Person_name = obj.Person_name
    # Identity_Document_Number = obj.Identity_Document_Number
    # Date_of_Birth = obj.Date_of_Birth
    # Date_of_Symptons = obj.Date_of_Symptons
    # Date_of_Confirmation = obj.Date_of_Confirmation 

    # Data = {
    #         'Case_Number': Case_Number,
    #         'Person_name': Person_name,
    #         'Identity_Document_Number': Identity_Document_Number,
    #         'Date_of_Birth': Date_of_Birth,
    #         'Date_of_Symptons' : Date_of_Symptons,
    #         'Date_of_Confirmation' : Date_of_Confirmation,
    # }

    Data = {
            'case': obj,
            'event_list': event_list,
    }

    return render(request,'../templates/case_detail.html', Data) #TODO: Monica connect to result page

'''
def case_create_view(request):
    form = CaseForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CaseForm()
    context = {
        'form':form
    }
    return render(request,'Case/templates/case_view.html',context )
    '''