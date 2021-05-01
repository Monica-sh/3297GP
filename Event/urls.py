from django.urls import path

from Event import views

urlpatterns = [
    path(
        'create_event/<uuid:pk>', 
        views.add_personal_event, 
        name="create-event"
    ), 
]