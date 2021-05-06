from django.urls import path

from Event import views

urlpatterns = [
    path(
        'create_event/<uuid:pk>', 
        views.add_personal_event, 
        name="create-event"
    ), 

    path('sse_result_list/', 
        views.SSEResultsListView.as_view(), 
        name="sse-detail"
    ), 

    path('sse_detail/<slug:pk>', 
        views.add_personal_event, 
        name="sse-detail"
    ), 
]