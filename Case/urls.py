from django.urls import path

from . import views
from Case.views import Case_Detail_View

urlpatterns = [
    path('case_results/',views.ResultView.as_view(),name = 'case_results'),
    #path('case_create/',views.CaseCreateView.as_view(),name = 'case_create'),
    path('case_create/', views.case_create_view ,name = 'case_create')
    # path('<uuid:pk>',Case_Detail_View,name = 'case_detail'),

]