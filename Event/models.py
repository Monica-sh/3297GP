from django.db import models
from Case.models import Case
# Create your models here.

class PublicEvent(models.Model):
    '''
    public event is unique 
    at a certain location on a certain date, it includes no description
    '''

    # venue name, for example, a restaurant name
    name = models.CharField(max_length=200)

    # venue location
    location = models.CharField(max_length=200)

    # venue address, get from api
    address = models.CharField(max_length=200, null=True, blank=True)

    # x and y coordinates of location
    xCoord = models.FloatField(null=True, blank=True)

    yCoord = models.FloatField(null=True, blank=True)

    # date of event
    date = models.DateField()

    # number of cases in the event, should be modified whenever there is a change in personal events to this event
    number_of_cases = models.IntegerField(default=0)


class PersonalEvent(models.Model):
    '''
    personal event is uniquelly mapped to a person and an event, it includes description
    '''
    event = models.ForeignKey(PublicEvent, on_delete=models.CASCADE)

    case = models.ForeignKey(Case, on_delete=models.CASCADE)

    description = models.CharField(max_length=200)