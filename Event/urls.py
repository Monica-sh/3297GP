from django.urls import path

from Event import views

urlpatterns = [
    path(
        'create_location/<slug:pk>', 
        views.add_personal_event, 
        name="create-event"
    ), 
]