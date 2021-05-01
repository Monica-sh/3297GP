  
import uuid
from django.db import models
from django.urls import reverse

class Case(models.Model):
    Case_Number = models.CharField(max_length=30,unique = True)
    Person_name = models.CharField(max_length=30)
    Identity_Document_Number = models.CharField(max_length=10)
    Date_of_Birth = models.DateField()
    Date_of_Symptons = models.DateField()
    Date_of_Confirmation = models.DateField()
    id = models.UUIDField(
        primary_key=True,
        default = uuid.uuid4,
        editable=False)
        
    class Meta:
        ordering = ['Case_Number']

    def __str__(self):
        return self.Case_Number

    def get_absolute_url(self):
        return reverse('case_detail_page',args = [str(self.id)])
