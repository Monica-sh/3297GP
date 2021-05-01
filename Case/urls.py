from django.urls import path

from . import views
from Case.views import Case_Detail_View

urlpatterns = [
    path('finding_case_results/',views.ResultView.as_view(),name = 'finding_case_results'),
    path('case_create/',views.CaseCreateView.as_view(),name = 'case_create'),
    # path('<uuid:pk>',Case_Detail_View,name = 'case_detail'),

]