  
import uuid
from django.db import models
from django.urls import reverse

class Case(models.Model):
    Case_Number = models.DecimalField(max_digits =10,decimal_places =0,unique = True)
    Person_name = models.CharField(max_length=30)
    Identity_Document_Number = models.CharField(max_length=10)
    Date_of_Birth = models.CharField(max_length=30)
    Date_of_Symptons = models.CharField(max_length=30)
    Date_of_Confirmation = models.CharField(max_length=30)
    id = models.UUIDField(
        primary_key=True,
        default = uuid.uuid4,
        editable=False)
        
    class Meta:
        ordering = ['Case_Number']

    def __str__(self):
        return self.Case_Number

    def get_absolute_url(self):
        return reverse('case_detail',args = [str(self.id)])
