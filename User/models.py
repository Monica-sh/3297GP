from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.

class UserProfileInfo(models.Model):
    '''
    This model is an extension of the django provided User model for authentication. 
    '''
    # user, as provided by django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # maxlength = minlength = 6
    CHP_staff_number = models.CharField(max_length=6, validators=[MinLengthValidator(6)])

    def __str__(self):     
        return self.user.username